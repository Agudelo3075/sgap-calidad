#!/bin/bash
# Wrapper Maven portátil para SGAP
MVN_EXEC=""
if command -v mvn >/dev/null 2>&1; then
    MVN_EXEC="mvn"
elif [ -x "$HOME/.m2/wrapper/dists/apache-maven-3.10.0/dae9a06d/bin/mvn" ]; then
    MVN_EXEC="$HOME/.m2/wrapper/dists/apache-maven-3.10.0/dae9a06d/bin/mvn"
else
    FOUND=$(find "$HOME/.m2" /usr/share/maven /opt/maven -name mvn -type f -perm /111 2>/dev/null | head -n 1)
    if [ -n "$FOUND" ]; then
        MVN_EXEC="$FOUND"
    fi
fi

if [ -z "$MVN_EXEC" ]; then
    echo "Maven no encontrado. Instale Maven o agreguelo al PATH." >&2
    exit 1
fi

# Si se ejecuta en entorno con repo local en /tmp/myrepo y no se especificó otro, usarlo
if [ -d "/tmp/myrepo" ] && [[ "$*" != *"-Dmaven.repo.local"* ]]; then
    exec "$MVN_EXEC" -Dmaven.repo.local=/tmp/myrepo "$@"
else
    exec "$MVN_EXEC" "$@"
fi
