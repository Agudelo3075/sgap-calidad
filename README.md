# SGAP — Sistema de Gestión de Asistencia y Pagos
## Plan de Aseguramiento de Calidad de Software (SQA) y Suite Automatizada con JUnit 5

**Institución Universitaria EAM**  
**Facultad de Ingeniería — Programa de Ingeniería de Software**  
**Asignatura:** Ingeniería de Software II (ISII) — Pruebas y Calidad de Software  
**Docente Evaluador:** Mg. David Cano Baquero  

---

### 👥 Integrantes y Desarrolladores
* **Jhoan Sebastián Agudelo Mejía** (`sebastian.agudelo@eam.edu.co`)
* **Juan Pablo Bedoya Payán** (`juanp.bedoya@eam.edu.co`)

---

## 📋 1. Descripción del Proyecto
**SGAP** es una solución informática ligera de alta fiabilidad diseñada para sistematizar, estandarizar y auditar dos procesos operativos críticos en academias formativas (escuelas deportivas de fútbol, natación, artes marciales y academias musicales):
1. **Control de Asistencia y Prevención Temprana de Deserción:** Registro diario sin duplicidad en estados `PRESENTE`, `TARDE`, `AUSENTE` y `JUSTIFICADO`; cómputo ponderado de porcentajes donde las llegadas tarde suman a favor y las excusas médicas se descuentan de la base evaluable; alerta temprana al acudiente al registrar $\ge 3$ ausencias consecutivas cronológicas; y detección alfabética de alumnos en riesgo académico ($< 80.0\%$).
2. **Liquidación Financiera y Semáforo de Cartera:** Liquidación diaria de mora al 0.5% con blindaje institucional de tope máximo del 15% calculada con exactitud bancaria mediante `java.math.BigDecimal` y redondeo `HALF_UP` (mitigación del riesgo financiero R4); descuento comercial de 2 meses por matrícula anual anticipada (10 mensualidades pagan 12 meses); y semáforo preventivo de cobro (`AL_DIA`, `POR_VENCER` en ventana de 3 días previos, y `EN_MORA`).

---

## 🛠️ 2. Requisitos del Sistema y Entorno Técnico
* **Java Development Kit (JDK):** Versión 17 LTS o superior (OpenJDK / Eclipse Temurin).
* **Gestor de Construcción:** Apache Maven 3.8+ (se incluye wrapper ejecutable `./mvnw` y `mvnw.cmd`).
* **Framework de Pruebas:** JUnit Jupiter 5.10.2 con soporte para pruebas parametrizadas.
* **Plugin de Ejecución:** Maven Surefire Plugin 3.1.2.

---

## 🚀 3. Instrucciones de Compilación y Ejecución ("Sin Preguntas")

El proyecto está 100% estandarizado bajo Maven para que cualquier docente o evaluador pueda compilar, probar y ejecutar de forma inmediata.

### A. Ejecutar la Suite de Pruebas Automatizadas (92 Tests en JUnit 5)
En la raíz del proyecto, ejecute en su terminal:

**En Linux / macOS:**
```bash
./mvnw test
```
*(Si tiene Maven instalado globalmente en su sistema: `mvn test`)*

**En Windows (PowerShell o CMD):**
```cmd
.\mvnw.cmd test
```
*(Si tiene Maven instalado globalmente en su sistema: `mvn test`)*

> **Resultado Esperado:** 
> `Tests run: 92, Failures: 0, Errors: 0, Skipped: 0`  
> `BUILD SUCCESS` (Tiempo aprox: 3.5 a 5 segundos).

---

### B. Compilar y Empaquetar el Archivo JAR Ejecutable
```bash
./mvnw clean package
```
El binario ejecutable se generará en la carpeta `target/`:
```bash
java -jar target/sgap-aceptacion-1.0.0.jar
```

---

### C. Ejecutar la Consola Interactiva Directamente con Maven
```bash
./mvnw compile exec:java -Dexec.mainClass="co.edu.eam.sgap.AplicacionSGAP"
```

---

### D. Compilación y Ejecución Manual Alternativa (Sin Maven)
Si por alguna razón no desea utilizar Maven, puede compilar directamente con el compilador estándar de Java:

**En Linux / macOS:**
```bash
mkdir -p out
javac -encoding UTF-8 -d out $(find src/main/java -name "*.java")
java -cp out AplicacionSGAP
```

**En Windows (PowerShell):**
```powershell
mkdir out
javac -encoding UTF-8 -d out (Get-ChildItem -Recurse -Filter *.java src/main/java).FullName
java -cp out AplicacionSGAP
```

---

## 💻 4. Catálogo de Comandos de la Consola SGAP

Al iniciar la aplicación, se dispone de los siguientes 10 comandos (escriba `ayuda` para recordarlos o `salir` para terminar la sesión):

| Comando y Sintaxis | Descripción y Reglas de Negocio | Ejemplo de Uso |
| :--- | :--- | :--- |
| `registrar nombre;AAAA-MM-DD;ESTADO` | Registra asistencia diaria (`PRESENTE`, `TARDE`, `AUSENTE`, `JUSTIFICADO`). Rechaza duplicados el mismo día. | `registrar Ana;2026-11-01;PRESENTE` |
| `corregir nombre;AAAA-MM-DD;ESTADO` | Corrige o rectifica un registro previamente almacenado. | `corregir Ana;2026-11-01;JUSTIFICADO` |
| `porcentaje nombre` | Calcula el % acumulado y valida si cumple el mínimo institucional (80.0%). | `porcentaje Ana` |
| `alerta nombre` | Informa si el alumno acumula $\ge 3$ ausencias consecutivas cronológicas. | `alerta Pedro` |
| `riesgo` | Lista en orden alfabético los estudiantes con asistencia $< 80.0\%$. | `riesgo` |
| `asistentes AAAA-MM-DD` | Cuantifica el aforo real de la jornada (`PRESENTE` y `TARDE`). | `asistentes 2026-11-01` |
| `recargo mensualidad;diasDeMora` | Liquida el recargo diario al 0.5% aplicando tope del 15%. | `recargo 100000;40` &rarr; `$15000.00` |
| `total mensualidad;diasDeMora` | Liquida el valor total a pagar (Mensualidad + Recargo). | `total 100000;10` &rarr; `$105000.00` |
| `anual mensualidad` | Liquida matrícula anual con descuento (10 mensualidades pagan 12). | `anual 100000` &rarr; `$1000000.00` |
| `estadopago vencimiento;hoy` | Determina semáforo: `AL_DIA`, `POR_VENCER` (ventana 3 días) o `EN_MORA`. | `estadopago 2026-11-10;2026-11-08` |
| `ayuda` / `salir` | Muestra el menú de comandos / Finaliza la aplicación. | `ayuda` |

---

## 📂 5. Estructura del Repositorio

```text
sgap-aceptacion/
├── pom.xml                                   # Configuración de Maven, plugins y dependencias JUnit 5
├── mvnw / mvnw.cmd                           # Wrappers de Maven para ejecución portable sin instalación previa
├── README.md                                 # Guía técnica completa de compilación y ejecución
├── ISII_Grupo1_Entregable.pdf                # DOCUMENTO FORMAL PDF DEL PLAN DE ASEGURAMIENTO DE CALIDAD
├── Documento_Entregable_Final.html           # Fuente estructurada HTML/CSS del informe
├── SUSTENTACION_15_MINUTOS.md                # Guion oficial y cronograma minuto a minuto para el video
├── src/
│   ├── main/java/
│   │   ├── AplicacionSGAP.java               # Punto de entrada / Interfaz CLI de consola interactiva
│   │   └── co/edu/eam/sgap/
│   │       ├── CalculadoraMensualidad.java   # Lógica financiera (BigDecimal, tope 15%, semáforo)
│   │       ├── EstadoPago.java               # Enum tipado: AL_DIA, POR_VENCER, EN_MORA
│   │       ├── PruebasSGAP.java              # Validador autónomo de verificación de la guía 1
│   │       └── asistencia/
│   │           ├── ControlAsistencia.java    # Lógica de asistencia, porcentajes, alertas y riesgo
│   │           ├── RegistroAsistencia.java   # Java Record inmutable de registro
│   │           └── EstadoAsistencia.java     # Enum: PRESENTE, TARDE, AUSENTE, JUSTIFICADO
│   └── test/java/co/edu/eam/sgap/
│       ├── CalculadoraMensualidadTest.java   # 33 pruebas unitarias y parametrizadas (@CsvSource)
│       ├── CriteriosAceptacionSGAPTest.java  # 9 pruebas BDD de Criterios de Aceptación (Dado-Cuando-Entonces)
│       ├── AplicacionSGAPTest.java           # 14 pruebas de integración de consola y manejo de errores
│       └── asistencia/
│           └── ControlAsistenciaTest.java    # 36 pruebas de lógica de asistencia, rachas y ordenamiento
└── target/                                   # Artefactos compilados y reportes de Surefire
```

---

## 📊 6. Métricas de Calidad de la Suite Automatizada

* **Total de Pruebas Automatizadas:** 92 casos de prueba.
* **Fallos / Errores:** 0 (100% de éxito).
* **Cobertura de Ramas (Branch Coverage):** 100% en la capa de lógica de negocio (`CalculadoraMensualidad` y `ControlAsistencia`).
* **Tiempo Promedio de Ejecución:** Menor a 4.0 segundos en Surefire.
