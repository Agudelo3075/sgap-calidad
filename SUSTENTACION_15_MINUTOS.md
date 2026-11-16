# 🎙️ GUION OFICIAL Y CRONOGRAMA DE SUSTENTACIÓN EN VIDEO (15 MINUTOS)
## Plan de Aseguramiento de Calidad de Software (SQA) — Proyecto SGAP
### Institución Universitaria EAM — Ingeniería de Software II (ISII)
**Docente Evaluador:** Mg. David Cano Baquero  

---

## 👥 DATOS DEL EQUIPO Y CONDICIONES OBLIGATORIAS
* **Integrante 1:** Jhoan Sebastián Agudelo Mejía
* **Integrante 2:** Juan Pablo Bedoya Payán
* **Tiempo asignado:** 7 a 15 minutos (Planificado con precisión para 13 a 14 minutos).
* **Modalidad de Entrega:** Video pregrabado alojado en **Google Drive** (compartido con permisos de lectura para el docente) o en **YouTube en modo Oculto (Unlisted)**.

> [!IMPORTANT]
> **REGLAS DE ORO DEL DOCENTE PARA EL VIDEO:**
> 1. **Cámara a medio cuerpo obligatoria:** Ambos integrantes deben aparecer en cámara visible a medio cuerpo en sus intervenciones.
> 2. **Participación equitativa obligatoria:** Ambos integrantes deben hablar activamente durante el video (50% del tiempo cada uno). *Integrante que no aparece o no habla, no recibe calificación.*
> 3. **Demostración en vivo:** Es obligatorio compartir pantalla y ejecutar en vivo la terminal ejecutando las pruebas con Maven (`./mvnw test`) y mostrando la aplicación funcionando.
> 4. **Verificación de permisos:** Antes de enviar el correo, probar el enlace del video en una pestaña de incógnito para verificar que abra sin solicitar inicio de sesión ni permisos restringidos.

---

## ⏱️ CRONOGRAMA MINUTO A MINUTO (DISTRIBUCIÓN EQUITATIVA)

| Intervalo | Tiempo | Responsable | Sección del Trabajo | Apoyo Visual en Pantalla |
| :---: | :---: | :--- | :--- | :--- |
| **1** | 0:00 – 1:30 | **Jhoan Sebastián** | Saludo, presentación formal y contexto del negocio SGAP | Portada del PDF / Cámara a medio cuerpo |
| **2** | 1:30 – 3:30 | **Juan Pablo** | Estandarización técnica, Maven y requisitos (RF-01 a RF-10) | Estructura de carpetas en IDE y `pom.xml` |
| **3** | 3:30 – 5:30 | **Jhoan Sebastián** | **Etapa 1:** Métodos de prueba (BVA en mora R4 y Grafo McCabe) | Código `CalculadoraMensualidad` y diagrama CFG |
| **4** | 5:30 – 7:30 | **Juan Pablo** | **Etapa 2:** Plan de pruebas, matriz RTM y Bitácora de Defectos | Matriz de 16 Casos de prueba y Bug Tracking |
| **5** | 7:30 – 10:30 | **Ambos (Jhoan & Juan Pablo)** | **Etapa 3:** **Demostración en Vivo (Live Demo):** Maven Surefire y Consola | Terminal en vivo: `./mvnw test` (92 tests) y CLI SGAP |
| **6** | 10:30 – 12:30 | **Juan Pablo** | **Etapa 4:** Calidad: ISO 25010, autoevaluación CMMI y DoD | Sección de calidad del PDF: 3 características y DoD |
| **7** | 12:30 – 14:00 | **Jhoan Sebastián & Juan Pablo** | Conclusiones, lecciones aprendidas, dictamen y despedida | Ambos en cámara a medio cuerpo |

---

## 🗣️ GUION TEXTUAL PASO A PASO (QUÉ DECIR EXACTAMENTE)

### 📌 PARTE 1: INTRODUCCIÓN Y CONTEXTO DEL PROYECTO (0:00 – 1:30)
* **Voz:** Jhoan Sebastián Agudelo Mejía
* **En pantalla:** *Jhoan en cámara a medio cuerpo + Portada del documento `ISII_Grupo1_Entregable.pdf`.*

> **Jhoan Sebastián:**  
> *"Un cordial saludo para el profesor David Cano Baquero y para todos los presentes. Mi nombre es Jhoan Sebastián Agudelo Mejía y junto a mi compañero Juan Pablo Bedoya Payán, conformamos el equipo de desarrollo y aseguramiento de calidad del proyecto **SGAP: Sistema de Gestión de Asistencia y Pagos**, correspondiente a la asignatura Ingeniería de Software II de la Institución Universitaria EAM.*  
>  
> *Para contextualizar el proyecto, SGAP nace de una necesidad operativa muy tangible en academias deportivas y escuelas formativas de música: erradicar el control artesanal en planillas de papel o libros dispersos de Excel, los cuales provocan deserción inadvertida de alumnos y constantes disputas económicas por cobros de mora desmedidos.*  
>  
> *SGAP unifica dos pilares esenciales: primero, el control riguroso de asistencia diaria con estados de Presente, Tarde, Ausente y Justificado, emitiendo alertas tempranas ante ausencias consecutivas para evitar la pérdida de estudiantes. Y segundo, la liquidación transparente de mensualidades, aplicando un recargo diario por mora protegido con un tope institucional estricto del 15%.*  
>  
> *A continuación, mi compañero Juan Pablo explicará la estandarización técnica del código y el refinamiento de nuestros requisitos funcionales."*

---

### 📌 PARTE 2: ESTANDARIZACIÓN TÉCNICA Y REQUISITOS (1:30 – 3:30)
* **Voz:** Juan Pablo Bedoya Payán
* **En pantalla:** *Juan Pablo en cámara a medio cuerpo + Estructura de paquetes en el IDE y tabla de RF-01 a RF-10.*

> **Juan Pablo:**  
> *"Muchas gracias, Sebastián. Saludo cordial, profesor David.*  
>  
> *Al asumir este proyecto, nuestro primer reto como analistas de calidad fue la **estandarización arquitectónica mediante Apache Maven**. Transformamos el código base organizándolo bajo los estándares internacionales `src/main/java` y `src/test/java`, configurando en el archivo `pom.xml` las dependencias modernas de **JUnit Jupiter 5.10.2** y el plugin **Maven Surefire 3.1.2**.*  
>  
> *Asimismo, retomamos los requisitos de la guía anterior y los refinamos y ampliamos formalmente a **10 Requisitos Funcionales rigurosamente verificables (RF-01 al RF-10)**:*  
> * Destacamos **RF-01 y RF-06**, que garantizan la unicidad de asistencia diaria mediante excepciones controladas y permiten la rectificación de registros.  
> * **RF-02**, que protege al alumno reconociendo las llegadas tarde a su favor y descontando las excusas médicas del divisor base evaluable.  
> * **RF-03**, que dispara la alerta al acudiente al registrar tres o más ausencias injustificadas seguidas.  
> * Y **RF-04 y RF-05**, que estructuran la liquidación de cartera con tope de mora y una ventana de semaforización de tres días.*  
>  
> *Ahora Sebastián profundizará en la Etapa 1: diseño de pruebas mediante caja negra y caja blanca."*

---

### 📌 PARTE 3: MÉTODOS DE PRUEBA: CAJA NEGRA Y CAJA BLANCA (3:30 – 5:30)
* **Voz:** Jhoan Sebastián Agudelo Mejía
* **En pantalla:** *Jhoan en cámara + Código de `CalculadoraMensualidad.java` y Grafo de Flujo (CFG).*

> **Jhoan Sebastián:**  
> *"Gracias, Juan Pablo. En la **Etapa 1** investigamos y aplicamos formalmente las técnicas de diseño de pruebas:*  
>  
> *En **Caja Negra**, implementamos Particiones en Clases de Equivalencia y **Análisis de Valores Límite (BVA)** sobre tres requisitos centrales. Quiero enfatizar la mitigación del **Riesgo Crítico R4**: en sistemas financieros, usar tipos de coma flotante como `double` o `float` es inaceptable porque la representación IEEE 754 genera imprecisiones acumulativas de centavos. En SGAP blindamos los cálculos usando `BigDecimal` con escala a 2 decimales y redondeo formal `RoundingMode.HALF_UP`.*  
>  
> *Sometimos el tope de mora del 15% a pruebas en las fronteras críticas: evaluamos el día 29 con 14.5%, el día 30 en la frontera exacta del 15.0%, y los días 31 y 40, comprobando que la tasa se congele inquebrantablemente en el 15.0%.*  
>  
> *En **Caja Blanca**, seleccionamos el método real `calcularRecargoPorMora` en Java. Modelamos su **Grafo de Flujo de Control (CFG)** con 10 nodos y 12 aristas. Calculamos la **Complejidad Ciclomática de Thomas McCabe**, obteniendo un $V(G) = 4$, verificado por aristas y nodos ($12 - 10 + 2 = 4$), por nodos predicado ($3 + 1 = 4$) y por regiones planas. Diseñamos un caso de prueba documentado para cada uno de los 4 caminos independientes del conjunto base.*  
>  
> *Doy paso a Juan Pablo para la Etapa 2 de planificación y trazabilidad."*

---

### 📌 PARTE 4: PLAN DE PRUEBAS, TRAZABILIDAD Y REGISTRO DE DEFECTOS (5:30 – 7:30)
* **Voz:** Juan Pablo Bedoya Payán
* **En pantalla:** *Juan Pablo en cámara + Documento PDF mostrando el Plan de Pruebas, la tabla RTM y la bitácora de bugs.*

> **Juan Pablo:**  
> *"Gracias, Sebastián. En la **Etapa 2**, estructuramos nuestro Plan de Pruebas bajo las directrices de los estándares internacionales **IEEE 829** y la moderna norma **ISO/IEC/IEEE 29119-3:2021**.*  
>  
> *Nuestro plan formal, de 3 páginas de extensión, especifica el alcance, la exclusión de bases de datos externas en esta fase, los criterios de entrada y suspensión, y fija un criterio de salida inquebrantable: 100% de pruebas aprobadas sin fallos y cobertura superior al 90% en la capa de negocio.*  
>  
> *Documentamos exhaustivamente **16 Casos de Prueba (CP-01 al CP-16)** con precondiciones, pasos, datos de entrada, salidas esperadas y su estado final de aprobación. Construimos la **Matriz de Trazabilidad de Requisitos (RTM)**, garantizando una relación bidireccional entre los 10 requisitos funcionales, las clases Java y los tests.*  
>  
> *Asimismo, mantuvimos una **Bitácora de Defectos Reales (Bug Tracking Log)**, registrando y resolviendo 4 defectos críticos: desde la corrección del redondeo decimal bancario (BUG-01) y la validación relacional de tope (BUG-02), hasta el manejo de entradas en blanco en consola (BUG-03) y la garantía de ordenamiento cronológico en Streams para el cálculo de rachas continuas (BUG-04).*  
>  
> *A continuación, pasamos al momento central de nuestra sustentación: la **Demostración Práctica en Vivo** de la suite automatizada y el software funcionando."*

---

### 📌 PARTE 5: DEMOSTRACIÓN PRÁCTICA EN VIVO (LIVE DEMO) (7:30 – 10:30)
* **Voz:** Ambos (Turnos alternados en vivo)
* **En pantalla:** *Compartir pantalla completa con Terminal de comandos abierta y clara.*

> **Jhoan Sebastián (Toma el control de la terminal):**  
> *"Vamos a comprobar en vivo la ejecución de nuestra suite automatizada. Como el docente puede corroborar, nos encontramos en la raíz del repositorio. Ejecutamos el comando:*  
> `sh ./mvnw test`  
> *(o `mvn test`). Observen cómo Maven compila y Surefire ejecuta las 4 clases de prueba...*  
>  
> *¡Listo! Miren el reporte de Surefire:*  
> * *`CriteriosAceptacionSGAPTest`: 9 pruebas BDD aprobadas.*  
> * *`CalculadoraMensualidadTest`: 33 pruebas unitarias y parametrizadas aprobadas.*  
> * *`AplicacionSGAPTest`: 14 pruebas de integración de consola aprobadas.*  
> * *`ControlAsistenciaTest`: 36 pruebas de lógica de asistencia aprobadas.*  
>  
> *Total:* **92 pruebas ejecutadas, 0 Fallures, 0 Errors, 0 Skipped en tan solo 3.8 segundos. Éxito del 100%.**  
>  
> *Ahora Juan Pablo demostrará el funcionamiento en vivo de la aplicación en consola."*

> **Juan Pablo (Ejecuta la consola interactiva):**  
> *"Empaquetamos y ejecutamos la consola interactiva con:*  
> `java -cp target/classes co.edu.eam.sgap.AplicacionSGAP`  
>  
> *1. Escribimos `ayuda` y vemos el despliegue del catálogo de comandos.*  
> *2. Registramos asistencia: `registrar Carlos;2026-11-01;PRESENTE`. El sistema responde: OK.*  
> *3. Intentamos duplicar: `registrar Carlos;2026-11-01;TARDE`. El sistema intercepta amigablemente: ERROR: Ya existe un registro de Carlos para esa fecha.*  
> *4. Probamos el cálculo financiero: `recargo 100000;10`. Nos liquida $5000.00.*  
> *5. Probamos el tope institucional: `recargo 100000;45`. Nos liquida exactamente $15000.00, protegiendo al cliente.*  
> *6. Escribimos `estadopago 2026-11-10;2026-11-08` y nos confirma: POR_VENCER.*  
>  
> *El sistema responde de manera inmediata y con total solidez defensiva."*

---

### 📌 PARTE 6: CALIDAD DEL SOFTWARE: ISO 25010, CMMI Y DEFINITION OF DONE (10:30 – 12:30)
* **Voz:** Juan Pablo Bedoya Payán
* **En pantalla:** *Juan Pablo en cámara + Sección de Calidad del documento PDF.*

> **Juan Pablo:**  
> *"En la **Etapa 4**, evaluamos la calidad de SGAP a la luz de marcos y estándares de la industria:*  
>  
> *1. **Modelo ISO/IEC 25010:** Seleccionamos tres características esenciales:*  
> * *Adecuación Funcional:* Garantizando completitud y exactitud en los cómputos contables con `BigDecimal`.*  
> * *Fiabilidad:* Tolerancia a fallos comprobada en 92 tests y recuperación limpia ante excepciones de consola.*  
> * *Mantenibilidad:* Arquitectura desacoplada en tres módulos independientes con alta testabilidad.*  
>  
> *2. **Nivel de Madurez CMMI:** Siendo rigurosos y honestos, ubicamos a nuestro equipo en el **Nivel 2 de Madurez (Gestionado)**. Planificamos las pruebas, versionamos en Git, gestionamos requerimientos con trazabilidad y controlamos defectos en cada ciclo. Para ascender al **Nivel 3 (Definido)**, nuestro plan de acción contempla institucionalizar estas plantillas a nivel organizacional, integrar pipelines de CI/CD con GitHub Actions y fijar políticas de cobertura obligatoria.*  
>  
> *3. **Definición de Terminado (DoD):** Redactamos 7 condiciones obligatorias para aceptar un incremento: código limpio sin advertencias, compilación exitosa en Maven, 100% de tests verdes en JUnit 5, cobertura de ramas $\ge 90\%$, criterios BDD aprobados, revisión de código por pares (Peer Review) y documentación actualizada.*  
>  
> *Doy paso a Sebastián para el cierre de nuestra sustentación."*

---

### 📌 PARTE 7: CONCLUSIONES, LECCIONES APRENDIDAS Y CIERRE (12:30 – 14:00)
* **Voz:** Jhoan Sebastián Agudelo Mejía & Juan Pablo Bedoya Payán (Cámara compartida a medio cuerpo)
* **En pantalla:** *Ambos integrantes visibles en cámara a medio cuerpo.*

> **Jhoan Sebastián:**  
> *"Para concluir, este trabajo nos deja lecciones fundamentales de ingeniería: comprobamos que las pruebas funcionales tradicionales centradas en valores intermedios ocultan los defectos más graves, y que son las técnicas formales de Valores Límite y Cobertura de Ramas las que verdaderamente blindan un software.*  
>  
> *Asimismo, reafirmamos que el aseguramiento de calidad no es una tarea accesoria al final del proyecto, sino un pilar arquitectónico que debe regir cada línea de código desde la concepción de los requisitos.*  
>  
> *Con base en las **92 pruebas automatizadas ejecutadas con 0 fallos**, emitimos un dictamen de aceptación unánime para el sistema SGAP.*  
>  
> *Agradecemos al profesor David Cano Baquero por su orientación y quedamos a su entera disposición para cualquier inquietud.*  
>  
> *¡Muchas gracias!"*

> **Juan Pablo:**  
> *"Muchas gracias a todos por su atención."*
