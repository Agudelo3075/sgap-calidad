# 🎙️ GUION OFICIAL Y CRONOGRAMA DE SUSTENTACIÓN EN VIDEO (15 MINUTOS)
## Plan de Aseguramiento de Calidad de Software (SQA) — Proyecto SGAP
### Institución Universitaria EAM — Facultad de Ingeniería — Ingeniería de Software II (ISII)
**Docente Evaluador:** Mg. David Cano Baquero  

---

## 👥 DATOS DEL EQUIPO Y CONDICIONES OBLIGATORIAS
* **Integrante 1:** Jhoan Sebastián Agudelo Mejía
* **Integrante 2:** Juan Pablo Bedoya Payán
* **Tiempo asignado:** 7 a 15 minutos (Estructurado con precisión pedagógica para 13 a 14 minutos).
* **Modalidad de Entrega:** Video pregrabado alojado en **Google Drive** (compartido con permisos de lectura para el docente) o en **YouTube en modo Oculto (Unlisted)**.

> [!IMPORTANT]
> **REGLAS DE ORO DEL DOCENTE PARA EL VIDEO:**
> 1. **Cámara a medio cuerpo obligatoria:** Ambos integrantes deben aparecer en cámara visible a medio cuerpo en sus respectivas intervenciones (no solo la cara o un avatar).
> 2. **Participación equitativa obligatoria:** Ambos integrantes deben hablar activamente durante el video (50% del tiempo cada uno). *Integrante que no aparece o no habla, no recibe calificación.*
> 3. **Explicación con valor añadido (No leer el documento):** Lo que dice el documento PDF se debe usar como punto de partida para **explicar el porqué, el cómo se investigó, qué anomalía resolvieron y qué implicaciones de ingeniería tiene**. Si el documento dice que algo es "riguroso", en el video se explica con datos técnicos exactos por qué es riguroso.
> 4. **Demostración técnica en vivo:** Es obligatorio compartir pantalla y ejecutar en vivo en la terminal las pruebas con Maven (`./mvnw test`) mostrando los 92 tests en verde y una pequeña interacción con la consola de SGAP.
> 5. **Verificación de permisos:** Probar el enlace del video en una ventana privada o de incógnito antes de enviar el correo final.

---

## ⏱️ CRONOGRAMA MINUTO A MINUTO (DISTRIBUCIÓN EQUITATIVA 50% / 50%)

| Intervalo | Tiempo | Responsable | Sección del Trabajo | Enfoque de Explicación Añadida (Valor Agregado) | Apoyo Visual en Pantalla |
| :---: | :---: | :--- | :--- | :--- | :--- |
| **1** | 0:00 – 1:30 | **Jhoan Sebastián** | Presentación y Contexto del Negocio SGAP | Por qué las academias quiebran por Excel y planillas en papel; el impacto humano y financiero. | Cámara a medio cuerpo + Portada del PDF |
| **2** | 1:30 – 3:30 | **Juan Pablo** | Estandarización Maven y Requisitos (RF-01 a RF-10) | Por qué se pasó de compilación manual a Maven; por qué Records inmutables; refinamiento de ambigüedades. | Estructura en IDE + `pom.xml` + Tabla de Requisitos |
| **3** | 3:30 – 5:30 | **Jhoan Sebastián** | **Etapa 1:** Métodos de Prueba (Caja Negra y Caja Blanca) | Por qué BVA en mora (días 29, 30, 31); por qué la trampa de IEEE 754 en `double`; deducción matemática de McCabe $V(G)=4$. | Código `CalculadoraMensualidad` + Diagrama CFG |
| **4** | 5:30 – 7:30 | **Juan Pablo** | **Etapa 2:** Plan de Pruebas, Trazabilidad y Defectos Reales | Por qué ISO 29119-3 y no un simple checklist; trazabilidad bidireccional; autopsia técnica de los 4 bugs reales resueltos. | Plan de pruebas + Tabla RTM + Bug Tracker |
| **5** | 7:30 – 10:30 | **Ambos en Vivo** | **Etapa 3:** **Demostración en Vivo (Live Demo):** Maven y Consola | Explicación de qué hace Surefire en 3.8s por debajo; demostración interactiva en consola de casos límite y defensivos. | Terminal en pantalla completa en vivo |
| **6** | 10:30 – 12:30 | **Juan Pablo** | **Etapa 4:** Calidad: ISO 25010, CMMI y Definition of Done | Por qué adecuación, fiabilidad y mantenibilidad; por qué honestamente Nivel 2 CMMI y no Nivel 3; el rol de la DoD. | Sección de calidad del PDF + DoD con 7 condiciones |
| **7** | 12:30 – 14:00 | **Ambos** | Conclusiones, Lecciones Aprendidas y Cierre | La falacia de las pruebas intermedias; la calidad como cultura de proceso continuo; veredicto final. | Ambos en cámara a medio cuerpo |

---

## 🗣️ GUION TEXTUAL PASO A PASO (QUÉ DECIR EXACTAMENTE)

---

### 📌 PARTE 1: INTRODUCCIÓN Y CONTEXTO DEL PROYECTO (0:00 – 1:30)
* **Voz:** Jhoan Sebastián Agudelo Mejía
* **En pantalla:** *Jhoan visible en cámara a medio cuerpo. Comparte pantalla mostrando la portada formal de `ISII_Grupo1_Entregable.pdf`.*
* **Tono:** Seguro, profesional, académico y pausado.

> **Jhoan Sebastián:**  
> *"Muy buenos días / tardes, profesor David Cano Baquero. Mi nombre es Jhoan Sebastián Agudelo Mejía y junto con mi compañero Juan Pablo Bedoya Payán, conformamos el equipo de aseguramiento de calidad del proyecto **SGAP: Sistema de Gestión de Asistencia y Pagos**, correspondiente a la asignatura Ingeniería de Software II de la Institución Universitaria EAM.*  
>  
> *En el documento entregable formalizamos el Plan de Calidad de SGAP, pero en esta sustentación queremos ir más allá de lo que está escrito y explicarle **las decisiones de ingeniería, las justificaciones técnicas y los hallazgos reales** que obtuvimos durante el proceso.*  
>  
> *Para entender el valor de este software, debemos ubicarnos en la realidad operativa de las academias formativas (escuelas de fútbol, artes marciales, natación o academias de música). Tradicionalmente, estas instituciones gestionan su operación en planillas de papel o en libros de Excel compartidos. ¿Qué ocurre en la práctica? Identificamos dos problemas críticos:*  
> * *Primero, **la deserción silenciosa:** cuando un estudiante empieza a faltar de manera continua, el docente o la administración solo se percatan semanas después, cuando el acudiente llama a retirar al alumno. Ya es tarde para intervenir.*  
> * *Segundo, **los conflictos económicos por liquidaciones arbitrarias:** cuando un padre paga con retraso, la recepcionista cobra recargos a criterio personal o sumando intereses desproporcionados, lo que provoca discusiones y pérdida de clientes.*  
>  
> *SGAP no es un simple programa de consola: es un motor de negocio diseñado para blindar financieramente a la academia y detectar a tiempo el riesgo de deserción mediante reglas algorítmicas estrictas.*  
>  
> *A continuación, mi compañero Juan Pablo explicará cómo transformamos el código base mediante estandarización arquitectónica y cómo desambiguamos los requisitos funcionales."*

---

### 📌 PARTE 2: ESTANDARIZACIÓN TÉCNICA Y REQUISITOS (1:30 – 3:30)
* **Voz:** Juan Pablo Bedoya Payán
* **En pantalla:** *Juan Pablo visible en cámara a medio cuerpo. Comparte pantalla mostrando la estructura de carpetas en el IDE, el archivo `pom.xml` y el catálogo de requisitos RF-01 al RF-10.*

> **Juan Pablo:**  
> *"Muchas gracias, Sebastián. Saludo cordial, profesor David.*  
>  
> *Al asumir este proyecto, nuestro primer diagnóstico como analistas de calidad fue que el código asignado dependía de scripts y compilaciones manuales desarticuladas, sin un gestor formal del ciclo de vida del software. Esto constituía una mala práctica porque impedía la reproducibilidad de las compilaciones en otros entornos.*  
>  
> *Por tanto, nuestra primera decisión de arquitectura fue **estandarizar el proyecto bajo Apache Maven 3.10**:*  
> * *Reorganizamos las fuentes bajo la convención internacional `src/main/java` y `src/test/java`.*  
> * *Configuramos en el `pom.xml` la versión moderna de **JUnit Jupiter 5.10.2**, junto con el plugin **Maven Surefire 3.1.2**.*  
> * *A nivel de código en Java 17 LTS, aprovechamos los **Java Records** para `RegistroAsistencia`. En el documento mencionamos que esto aporta inmutabilidad, pero quiero explicar **por qué es crucial en calidad**: al ser inmutable por diseño de la JVM, garantizamos que una vez registrada una asistencia con su fecha y estado, ningún método externo ni hilo concurrente pueda modificar sus campos mediante efectos colaterales (side effects), protegiendo la integridad histórica de las auditorías.*  
>  
> *En cuanto a los requisitos, tomamos los 5 iniciales de la guía anterior y los ampliamos a **10 Requisitos Funcionales (RF-01 al RF-10)**. Pero no fue solo añadir funciones, sino **eliminar ambigüedades de lenguaje natural**:*  
> * *Por ejemplo, en el **RF-01**, el requisito decía 'registrar asistencia'. Nosotros lo refinamos técnicamente exigiendo que si se intenta registrar al mismo estudiante dos veces en la misma jornada, el sistema no sobreescriba en silencio, sino que arroje una excepción explícita `IllegalStateException` preservando el estado original.*  
> * *En el **RF-02**, desambiguamos el cálculo porcentual: aclaramos que una llegada 'TARDE' suma 100% como asistencia cumplida porque el alumno presenció la clase, y que una falta 'JUSTIFICADA' por excusa médica no se cuenta como inasistencia, sino que **se sustrae formalmente del divisor total evaluable**. Si un alumno tuvo 3 clases y justificó 1 médica, su porcentaje se calcula sobre base 2, evitando castigarlo injustamente.*  
> * *Y en el **RF-03**, fijamos con rigor que la alerta temprana al acudiente se dispara cuando la racha de ausencias injustificadas es estrictamente mayor o igual a 3 en orden cronológico.*  
>  
> *Ahora Sebastián profundizará en la Etapa 1: las técnicas de caja negra y caja blanca aplicadas a la lógica de negocio."*

---

### 📌 PARTE 3: MÉTODOS DE PRUEBA: CAJA NEGRA Y CAJA BLANCA (3:30 – 5:30)
* **Voz:** Jhoan Sebastián Agudelo Mejía
* **En pantalla:** *Jhoan en cámara + Código de `CalculadoraMensualidad.java`, tabla de valores límite y diagrama del Grafo de Flujo de Control (CFG).*

> **Jhoan Sebastián:**  
> *"Gracias, Juan Pablo. En la **Etapa 1**, el documento presenta la investigación teórica de particiones de equivalencia, valores límite (BVA), tablas de decisión y cobertura de McCabe. Pero aquí queremos explicar **por qué nuestras pruebas son verdaderamente rigurosas y qué problemas profundos resolvieron**.*  
>  
> *Empecemos por el **Riesgo Crítico Financiero R4: Errores en mensualidades y moras**. En el documento afirmamos que usar tipos flotantes como `double` o `float` en software financiero es inaceptable. ¿Por qué?*  
> * *Porque en arquitectura de computadores, el estándar binario IEEE 754 no puede representar de forma finita fracciones decimales cotidianas como $0.5\%$ ($0.005$) o divisiones entre 3. Si liquidáramos recargos con `double`, la máquina genera números como `1500.0000000000002`.*  
> * *En una academia de 500 alumnos facturando mensualmente, esos residuos decimales acumulan discrepancias en el arqueo contable y generan contingencias legales. Por eso en `CalculadoraMensualidad` forzamos el uso de `java.math.BigDecimal` y establecimos la regla de redondeo formal `RoundingMode.HALF_UP` fijada a dos decimales exactos.*  
>  
> *¿Por qué decimos que nuestro **Análisis de Valores Límite (BVA)** es riguroso?*  
> * *Porque no nos quedamos en probar un valor cómodo como '10 días de mora'. Nos fuimos a las fronteras exactas de transición matemática:*  
>   * *Probamos el **día 29**, donde la tasa lineal aplica $29 \times 0.5\% = 14.5\%$ (justo antes del tope).*  
>   * *Probamos el **día 30**, la frontera crítica exacta donde la tasa alcanza el $15.0\%$.*  
>   * *Probamos el **día 31**, el primer valor fuera del dominio lineal, verificando que la función conmute y se congele en el tope.*  
>   * *Y probamos casos extremos como **40 y 100 días**, comprobando que el recargo siga congelado permanentemente en el 15%.*  
>  
> *Pasando a **Caja Blanca**, seleccionamos el método real `calcularRecargoPorMora` en Java. En pantalla pueden observar el Grafo de Flujo de Control que modelamos, compuesto por 10 nodos y 12 aristas dirigidas.*  
> * *Para determinar el número exacto de pruebas necesarias, calculamos la **Complejidad Ciclomática de Thomas McCabe**. Y la verificamos por tres caminos matemáticos independientes:*  
>   * *1. Por fórmula de aristas y nodos: $V(G) = E - N + 2P = 12 - 10 + 2(1) = 4$.*  
>   * *2. Por nodos predicado o puntos de decisión condicional: tenemos 3 condicionales (`mensualidad <= 0`, `diasMora < 0`, y `tasa > TOPE_RECARGO`). Por tanto: $V(G) = \text{Predicados} + 1 = 3 + 1 = 4$.*  
>   * *3. Y por regiones planas del grafo: 3 regiones cerradas más 1 región abierta exterior = 4.*  
> * *Esto no es teoría abstracta: nos dio la certeza científica de que existen exactamente **4 caminos linealmente independientes**. Diseñamos un caso de prueba documentado para cada camino (camino de error por mensualidad negativa, camino de error por días negativos, camino de cálculo proporcional sin tope, y camino de aplicación de tope). Con esto garantizamos el 100% de cobertura de sentencias y el 100% de cobertura de ramas.*  
>  
> *Doy paso a Juan Pablo para explicar la Etapa 2 de planificación y gestión de defectos."*

---

### 📌 PARTE 4: PLAN DE PRUEBAS, TRAZABILIDAD Y REGISTRO DE DEFECTOS (5:30 – 7:30)
* **Voz:** Juan Pablo Bedoya Payán
* **En pantalla:** *Juan Pablo en cámara + Documento PDF mostrando el Plan de Pruebas IEEE 829 / ISO 29119-3, la Matriz RTM y la tabla de Bug Tracking.*

> **Juan Pablo:**  
> *"Gracias, Sebastián. En la **Etapa 2**, adoptamos los estándares internacionales **IEEE 829** y la moderna norma **ISO/IEC/IEEE 29119-3:2021** para formular nuestro Plan de Pruebas de 3 páginas.*  
>  
> *Queremos explicar por qué un plan de calidad bajo esta norma es muy distinto a un simple checklist de tareas:*  
> * *En primer lugar, porque la norma 29119-3 exige **declarar taxativamente qué se prueba y qué se excluye formalmente del alcance**. En nuestro caso, excluimos la persistencia en bases de datos relacionales externas (como PostgreSQL) porque en esta versión arquitectónica el sistema opera en memoria. Al excluirlo justificadamente, evitamos que problemas de conectividad o de red falseen o enmascaren los resultados de las pruebas de lógica de negocio.*  
> * *En segundo lugar, definimos **Criterios de Salida y Aprobación inquebrantables**: fijamos que para dar por aprobado el software, el 100% de los casos de prueba debían pasar en verde, con cero fallos, cero errores, y con una cobertura de ramas superior al 90% en el dominio.*  
>  
> *Documentamos **16 Casos de Prueba (CP-01 al CP-16)** con precondiciones, pasos y aserciones. Pero lo más valioso fue la construcción de la **Matriz de Trazabilidad de Requisitos (RTM)**:*  
> * *La RTM nos dio **trazabilidad bidireccional**: nos aseguró que cada uno de los 10 requisitos funcionales tuviera al menos un caso de prueba asociado (evitando 'requisitos huérfanos'), y a la inversa, que cada prueba automatizada en JUnit tuviera una justificación directa en las necesidades del cliente (evitando 'pruebas huérfanas' que consumen tiempo de cómputo sin aportar valor).*  
>  
> *Asimismo, mantuvimos una **Bitácora de Defectos Reales (Bug Tracking Log)** donde documentamos los errores encontrados y corregidos durante el ciclo de vida del proyecto:*  
> * *El **BUG-01:** la discrepancia decimal por el uso inicial de primitivos `double` en recargos, solucionada migrando a `BigDecimal`.*  
> * *El **BUG-02:** el riesgo del operador de frontera en el tope de mora, blindado con `compareTo`.*  
> * *El **BUG-03:** caídas por `NullPointerException` si el usuario enviaba nombres vacíos o espacios en la consola, resuelto con validación defensiva mediante `.trim()` e `isBlank()`.*  
> * *Y el **BUG-04:** un defecto sutil pero crítico: si el docente ingresaba asistencias en fechas desordenadas (por ejemplo el día 4, luego el día 1, y luego el día 2), el conteo de ausencias consecutivas fallaba porque leía en orden de inserción. Lo solucionamos forzando un Stream con `.sorted(Comparator.comparing(RegistroAsistencia::fecha))` antes de evaluar las rachas continuas.*  
>  
> *Ahora pasamos a la **Demostración Práctica en Vivo**, donde comprobaremos en la terminal la ejecución de nuestra suite automatizada y el comportamiento del software."*

---

### 📌 PARTE 5: DEMOSTRACIÓN PRÁCTICA EN VIVO (LIVE DEMO) (7:30 – 10:30)
* **Voz:** Ambos (Turnos en vivo con acciones coordinadas)
* **En pantalla:** *Compartir pantalla completa con Terminal de comandos abierta y visible con texto grande.*

> **Jhoan Sebastián (Toma el control de la terminal):**  
> *"Profesor David, en este momento estamos compartiendo la terminal en vivo, ubicados en la raíz del repositorio del proyecto `sgap-aceptacion`.*  
>  
> *Para cumplir la directriz de la Etapa 3 sobre automatización, ejecutamos la suite oficial mediante el wrapper de Maven:*  
> `sh ./mvnw test -o`  
> *(o `mvn test`).*  
>  
> *[EJECUTA EL COMANDO Y DEJA VER EL LOG DE SUREFIRE]*  
>  
> *Analicemos lo que acaba de suceder por debajo en solo **3.8 segundos**:*  
> * *El plugin **Maven Surefire 3.1.2** reconoció el proveedor de **JUnit Jupiter**.*  
> * *Ejecutó `CalculadoraMensualidadTest` con sus **33 pruebas**, evaluando en milisegundos todas las combinaciones parametrizadas con `@CsvSource`.*  
> * *Ejecutó `ControlAsistenciaTest` con **36 pruebas**, verificando unicidad, correcciones y rachas.*  
> * *Ejecutó `AplicacionSGAPTest` con **14 pruebas**, testeando la consola como prueba de sistema.*  
> * *Y ejecutó `CriteriosAceptacionSGAPTest` con **9 pruebas BDD**, validando los escenarios Dado-Cuando-Entonces.*  
>  
> *Resultado oficial:* **92 pruebas ejecutadas, 0 Fallures, 0 Errors, 0 Skipped. Éxito del 100% y BUILD SUCCESS.**  
>  
> *Ahora mi compañero Juan Pablo va a lanzar la aplicación interactiva para comprobar cómo responde la consola ante casos de frontera y manejo defensivo."*

> **Juan Pablo (Ejecuta la consola en la terminal):**  
> *"Lanzamos la consola compilada con:*  
> `java -cp target/classes co.edu.eam.sgap.AplicacionSGAP`  
>  
> *1. Escribimos `ayuda`:*  
> * *El sistema despliega el menú con los 10 comandos estructurados.*  
>  
> *2. Vamos a comprobar el **Requisito RF-01 de Unicidad**:*  
> * *Escribo: `registrar Carlos;2026-11-01;PRESENTE` &rarr; El sistema responde: `OK`.*  
> * *Ahora intentamos registrar al mismo Carlos el mismo día: `registrar Carlos;2026-11-01;TARDE`.*  
> * *Observen la respuesta: `ERROR: Ya existe un registro de Carlos para 2026-11-01`. El sistema interceptó la excepción de dominio y emitió un mensaje claro sin colapsar.*  
>  
> *3. Comprobemos el **Requisito RF-04 y RF-05 de Mora Financiera y Fronteras**:*  
> * *Simulemos un retraso de 10 días: `recargo 100000;10` &rarr; El sistema liquida: `Recargo por mora: 5000.00` (el 0.5% diario).*  
> * *Ahora probemos un caso con 45 días de retraso: `recargo 100000;45`.*  
> * *Si fuera lineal, cobraría $22.500; pero el sistema responde exactamente: `Recargo por mora: 15000.00`. Demostramos en vivo que el tope del 15% está activo y protegiendo al usuario.*  
>  
> *4. Probemos el **Semáforo de Pagos**:*  
> * *Escribo: `estadopago 2026-11-10;2026-11-08` &rarr; Faltan 2 días para el corte, y el sistema clasifica: `Estado del pago: POR_VENCER`.*  
>  
> *Escribimos `salir` y la aplicación termina de forma limpia.*  
> *Como se evidencia, la aplicación es robusta, rápida y cumple estrictamente las reglas de negocio."*

---

### 📌 PARTE 6: CALIDAD DEL SOFTWARE: ISO 25010, CMMI Y DEFINITION OF DONE (10:30 – 12:30)
* **Voz:** Juan Pablo Bedoya Payán
* **En pantalla:** *Juan Pablo en cámara + Documento PDF en la Sección de Calidad (ISO 25010, CMMI y las 7 condiciones de la DoD).*

> **Juan Pablo:**  
> *"En la **Etapa 4**, evaluamos SGAP a la luz de los modelos y estándares de calidad de la industria:*  
>  
> *1. **Modelo de Calidad ISO/IEC 25010:** Seleccionamos tres características que justificamos técnicamente para este tipo de software:*  
> * * **Adecuación Funcional:** No basta con que el software tenga muchas pantallas; evaluamos la **corrección funcional**, asegurando que los cálculos matemáticos con `BigDecimal` liquiden exactamente los centavos reales sin desfalcos.*  
> * * **Fiabilidad:** Con su subcaracterística de **tolerancia a fallos**, demostrada en cómo la aplicación intercepta fechas malformadas o argumentos incompletos sin generar 'crash' en la consola.*  
> * * **Mantenibilidad:** Medida por la **modularidad y la testabilidad**. El desacoplamiento entre `CalculadoraMensualidad`, `ControlAsistencia` y `AplicacionSGAP` permite que mañana podamos cambiar la interfaz de consola por una API REST en Spring Boot o una app web sin tocar una sola línea de la lógica de negocio.*  
>  
> *2. **Nivel de Madurez CMMI v2.0 (Autoevaluación Honesta):**  
> *En la guía se nos pidió ubicarnos con honestidad. Nos calificamos en el **Nivel 2 de Madurez (Gestionado / Managed)**. ¿Por qué no en Nivel 3?*  
> * *Porque un ingeniero debe actuar con integridad ética: en nuestro proyecto aplicamos gestión de requisitos con trazabilidad, control riguroso de versiones con Git, planificación formal de pruebas y monitoreo de defectos. Eso es exactamente Nivel 2.*  
> * *Pero no somos Nivel 3 todavía porque estas prácticas las gestionamos a nivel de nuestro equipo de proyecto; aún no están institucionalizadas como una política corporativa estandarizada para toda la facultad o la universidad.*  
> * *Para ascender al **Nivel 3 (Definido)**, propusimos un plan de acción concreto: convertir nuestras plantillas de prueba en activos de proceso reutilizables, integrar tuberías de CI/CD automáticas con GitHub Actions y fijar umbrales organizacionales obligatorios de cobertura de ramas mayores al 90%.*  
>  
> *3. **Definición de Terminado (Definition of Done - DoD):**  
> *En Scrum, una funcionalidad no está lista cuando el desarrollador dice 'ya programé el método'. Redactamos **7 condiciones obligatorias y verificables**: código limpio según estándares Java, compilación limpia en Maven, 100% de tests verdes en JUnit 5, cobertura de ramas $\ge 90\%$, criterios BDD cumplidos, revisión cruzada de código por pares (Peer Review) donde ninguno hace commit a `main` sin la aprobación del otro, y manuales actualizados.*  
>  
> *Doy paso a Sebastián para las conclusiones y cierre de la sustentación."*

---

### 📌 PARTE 7: CONCLUSIONES, LECCIONES APRENDIDAS Y CIERRE (12:30 – 14:00)
* **Voz:** Jhoan Sebastián Agudelo Mejía & Juan Pablo Bedoya Payán (Ambos visibles en cámara a medio cuerpo)
* **En pantalla:** *Cámara compartida con ambos integrantes visibles.*

> **Jhoan Sebastián:**  
> *"Para concluir nuestra sustentación, queremos compartir las dos lecciones aprendidas más significativas que nos deja este proyecto:*  
>  
> *La primera es **la falacia de las pruebas con valores intermedios**. En el taller inicial vimos cómo probar la edad 25 hacía pasar un código que en realidad estaba roto para la edad 18; y en SGAP comprobamos que probar 10 o 15 días de mora jamás habría descubierto si el tope del 15% funcionaba o no. Son las técnicas formales de Análisis de Valores Límite y Cobertura de Caminos de McCabe las que verdaderamente exponen los defectos antes de que lleguen a producción.*  
>  
> *La segunda lección es que **la calidad no es un evento que se hace al final del desarrollo**, sino una disciplina arquitectónica que debe estar presente desde el modelado inmutable de datos, la selección de tipos numéricos adecuados y la automatización continua en cada commit.*  
>  
> *Con base en las **92 pruebas automatizadas ejecutadas con 0 fallos**, emitimos un dictamen unánime de aprobación técnica para el sistema SGAP.*  
>  
> *Agradecemos al profesor David Cano Baquero por su exigencia y acompañamiento durante este semestre.*  
>  
> *¡Muchísimas gracias por su atención!"*

> **Juan Pablo:**  
> *"Muchas gracias, profesor, y quedamos atentos a cualquier inquietud o retroalimentación."*
