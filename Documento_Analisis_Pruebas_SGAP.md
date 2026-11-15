# DOCUMENTO DE ANÁLISIS DE PRUEBAS DE SOFTWARE Y CRITERIOS DE ACEPTACIÓN
## Sistema de Gestión de Asistencia y Pagos (SGAP)
**Institución Universitaria EAM**  
**Facultad de Ingeniería — Programa de Ingeniería de Software**  
**Asignatura:** Aseguramiento de Calidad de Software / Pruebas de Software

---

### 👥 Integrantes y Autores:
* **Jhoan Sebastián Agudelo Mejía**
* **Juan Pablo Bedoya Payán**

**Fecha:** Noviembre de 2026  
**Entorno Técnico:** Java 17 LTS | Apache Maven 3.10 | JUnit Jupiter 5.10.2 | Surefire 3.1.2  

---

## 1. RESUMEN EJECUTIVO
El presente informe documenta de manera exhaustiva el proceso de aseguramiento de calidad, estandarización técnica con Apache Maven, diseño de pruebas unitarias y de integración bajo JUnit 5, especificación formal de Criterios de Aceptación (BDD) y análisis arquitectónico aplicado al software **SGAP** (Sistema de Gestión de Asistencia y Pagos para academias deportivas y musicales).

Durante la semana de trabajo asignada, el equipo conformado por **Jhoan Sebastián Agudelo Mejía** y **Juan Pablo Bedoya Payán**:
1. Transformó el código asignado (originalmente dependiente de compilaciones manuales) en un proyecto estructurado bajo los estándares de **Apache Maven** (`src/main/java`, `src/test/java`, `pom.xml`).
2. Diseñó e implementó una suite automatizada de **92 casos de prueba**, logrando **0 fallos, 0 errores** y una tasa de éxito del 100%.
3. Formalizó **9 Criterios de Aceptación del Negocio** utilizando la sintaxis de Desarrollo Guiado por Comportamiento (BDD: Dado-Cuando-Entonces).
4. Alcanzó una **cobertura del 100% de las ramas de decisión** en la lógica de negocio (asistencia, cómputo porcentual, alertas preventivas, liquidación de moras y estados de cobro).
5. Analizó a fondo la mitigación del riesgo financiero **R4**, validando la precisión decimal con `BigDecimal` y redondeo `HALF_UP`.

---

## 2. INTRODUCCIÓN Y CONTEXTO DEL SISTEMA SGAP

### 2.1 Descripción de la Necesidad del Negocio
Las academias formativas (escuelas de fútbol, natación, artes marciales, danza o música) tradicionalmente administran la asistencia y la facturación de mensualidades mediante formatos físicos en papel o libros manuales de Excel. Este método genera tres problemas críticos:
* **Deserción no detectada a tiempo:** Cuando un estudiante comienza a acumular inasistencias continuas, el personal administrativo suele enterarse semanas después, perdiendo la oportunidad de intervenir con el acudiente antes del retiro definitivo.
* **Cobros conflictivos o desproporcionados:** Las mensualidades pagadas fuera de fecha generan discusiones sobre el recargo diario y las fechas de vencimiento.
* **Injusticia académica en excusas médicas:** La falta de un cálculo ponderado que diferencie una inasistencia injustificada de una debidamente soportada perjudica injustamente el porcentaje de permanencia del alumno.

### 2.2 Propósito y Alcance del Software
SGAP es una solución informática ligera que unifica:
1. **Control de Asistencia:** Registro de estados `PRESENTE`, `TARDE`, `AUSENTE` y `JUSTIFICADO`; cálculo automático de porcentajes; alerta preventiva al acudiente tras 3 inasistencias consecutivas; y detección de alumnos en riesgo (< 80%).
2. **Control Financiero:** Tasa de recargo por mora del 0.5% diario con blindaje institucional de tope máximo del 15%; descuento comercial por pronto pago anual (se cobran 10 meses en lugar de 12); y semáforo preventivo de cartera (`AL_DIA`, `POR_VENCER` en ventana de 3 días, `EN_MORA`).

---

## 3. MATRIZ DE RIESGOS DE SOFTWARE (RISK-BASED TESTING)

Para maximizar el impacto de la campaña de pruebas, se construyó una matriz formal de riesgos de negocio y técnicos:

| ID | Riesgo Identificado | Severidad | Probabilidad | Impacto en la Academia | Control / Mitigación en Pruebas |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **R1** | Deserción inadvertida de estudiantes por fallas en la alerta de inasistencias. | **Alta** | Media | Pérdida de clientes e ingresos recurrentes. | Pruebas de rachas continuas y verificación del disparador en 3 ausencias. |
| **R2** | Perjuicio injusto en porcentaje por inasistencias justificadas o retardos. | **Alta** | Alta | Reclamaciones de acudientes y desmotivación. | Aserciones de exclusión de `JUSTIFICADO` en la base y cómputo favorable de `TARDE`. |
| **R3** | Inconsistencia de aforo por duplicidad de registros en la misma jornada. | **Media** | Alta | Métricas falsas de ocupación de canchas/salones. | Pruebas de rechazo con `IllegalStateException` ante registro duplicado. |
| **R4** | Errores en cálculo de mensualidades, moras desmedidas o pérdida de centavos. | **Crítica** | Media | Pérdidas financieras o contingencias legales por cobro indebido. | Análisis de Valores Límite en el tope del 15% y precisión con `BigDecimal`. |
| **R5** | Bloqueo o caída del sistema (Crash) por entradas de texto corruptas en consola. | **Media** | Alta | Interrupción de operaciones y pérdida de confianza. | Pruebas de robustez ante fechas malformadas, cadenas vacías y argumentos faltantes. |

### 3.1 Análisis Especial del Riesgo Financiero R4
El enunciado del sistema enfatiza el riesgo R4. En sistemas informáticos construidos sobre Java, la utilización de tipos de datos en punto flotante (`float`, `double`) es inapropiada para transacciones económicas, ya que la representación binaria (IEEE 754) no puede representar con exactitud fracciones decimales cotidianas como $0.1$ o $0.005$, generando discrepancias acumulativas de centavos.

`CalculadoraMensualidad` implementa una solución de nivel profesional:
* Utiliza `java.math.BigDecimal` para todos los montos y tasas.
* Aplica `RoundingMode.HALF_UP` fijando la escala en 2 decimales.
* Impone un tope del 15% mediante comparación matemática (`tasa.compareTo(TOPE_RECARGO) > 0`).

Nuestras pruebas unitarias parametrizadas validaron exhaustivamente este comportamiento tanto en enteros como en valores con decimales periódicos.

---

## 4. ESPECIFICACIÓN DE CRITERIOS DE ACEPTACIÓN (BDD)

Se formalizaron 9 criterios de aceptación bajo la sintaxis **Dado - Cuando - Entonces** (Given - When - Then):

### CA-01: Registro diario de asistencia sin duplicidad en la misma jornada
* **Dado:** Un estudiante activo en la academia deportiva o de música.
* **Cuando:** El docente registra su asistencia en una fecha determinada.
* **Entonces:** El sistema guarda el estado y rechaza de inmediato cualquier segundo intento de registro para ese mismo estudiante en esa misma fecha, lanzando un mensaje de advertencia.

### CA-02: Las llegadas tarde cuentan a favor de la asistencia del estudiante
* **Dado:** Un estudiante que presenta asistencias puntuales y llegadas tarde (`TARDE`).
* **Cuando:** Se calcula su porcentaje de asistencia acumulado.
* **Entonces:** Las llegadas tarde se suman íntegramente como asistencias cumplidas sin rebajar el porcentaje del estudiante.

### CA-03: Excusas médicas justificadas no perjudican el promedio del alumno
* **Dado:** Un estudiante que asiste a clases y presenta una inasistencia debidamente justificada con excusa (`JUSTIFICADO`).
* **Cuando:** El sistema calcula su porcentaje de asistencia.
* **Entonces:** Dicha clase se descuenta del divisor total exigible (base evaluable), garantizando que su promedio no sufra detrimento por causas médicas o de fuerza mayor.

### CA-04: Alerta temprana al acudiente por 3 inasistencias injustificadas consecutivas
* **Dado:** Un estudiante matriculado en la academia.
* **Cuando:** Acumula cronológicamente 3 o más ausencias consecutivas sin justificación (`AUSENTE`).
* **Entonces:** El sistema dispara una alerta prioritaria dirigida al acudiente para intervenir oportunamente antes de la deserción.

### CA-05: Detección y reporte alfabético de estudiantes en riesgo académico (< 80%)
* **Dado:** Un grupo de estudiantes registrados en el sistema.
* **Cuando:** El administrador o docente solicita el listado de estudiantes en riesgo.
* **Entonces:** El sistema genera la lista de aquellos cuyo porcentaje de asistencia sea estrictamente inferior al 80.0%, presentándolos en orden alfabético.

### CA-06: Consulta y auditoría de aforo diario (asistencias efectivas)
* **Dado:** Una jornada académica con registros en diversos estados.
* **Cuando:** El docente consulta la cantidad de asistentes en dicha fecha.
* **Entonces:** El sistema cuantifica exclusivamente a los alumnos presentes físicamente (`PRESENTE` y `TARDE`), excluyendo a ausentes y justificados.

### CA-07: Cobro justo de recargo por mora con tope institucional del 15%
* **Dado:** Una mensualidad vencida sujeta a recargo diario del 0.5%.
* **Cuando:** Se calcula el monto de mora para cualquier cantidad de días transcurridos.
* **Entonces:** El recargo aumenta linealmente hasta alcanzar el 15.0% de la mensualidad (día 30) y se congela permanentemente en dicho tope a partir del día 31 en adelante.

### CA-08: Descuento por pago anual anticipado (10 mensualidades pagan 12)
* **Dado:** Un usuario que desea cancelar el año lectivo completo por adelantado.
* **Cuando:** Solicita la liquidación de la anualidad.
* **Entonces:** El sistema liquida exactamente 10 mensualidades ordinarias, otorgando 2 meses de descuento por pronto pago.

### CA-09: Notificación y clasificación del estado de pago con ventana de 3 días
* **Dado:** Una fecha de corte y la fecha de consulta actual.
* **Cuando:** El sistema compara ambas fechas.
* **Entonces:** Clasifica el cobro como `AL_DIA` si faltan más de 3 días; como `POR_VENCER` si faltan entre 0 y 3 días; y como `EN_MORA` si la fecha de vencimiento ya expiró.

---

## 5. DISEÑO DE CASOS DE PRUEBA (CAJA NEGRA Y CAJA BLANCA)

### 5.1 Partición en Clases de Equivalencia (Equivalence Partitioning)
* **Mensualidad:**
  * Clase Válida: Monto mayor a cero (`$80.000`, `$120.000,50`).
  * Clases Inválidas: Monto igual a cero, montos negativos (`-$50.000`), valor nulo (`null`).
* **Días de Mora:**
  * Clase Válida Sin Mora: `0` días.
  * Clase Válida Proporcional: `1` a `29` días.
  * Clase Válida Topada: `30` días o más.
  * Clase Inválida: Números enteros negativos (`-1`).
* **Estados de Asistencia:**
  * Clases Válidas: `PRESENTE`, `TARDE`, `AUSENTE`, `JUSTIFICADO`.
  * Clases Inválidas: Cadenas arbitrarias, valores nulos.
* **Nombres:**
  * Clase Válida: Cadenas alfanuméricas con caracteres válidos.
  * Clases Inválidas: `null`, cadena vacía `""`, cadenas con espacios en blanco únicamente `"   "`.

### 5.2 Análisis de Valores Límite (Boundary Value Analysis - BVA)
* **Frontera de Mora (Tope del 15%):**
  * Día 29: $29 \times 0.5\% = 14.5\%$ (Justo antes de la frontera).
  * Día 30: $30 \times 0.5\% = 15.0\%$ (Límite superior exacto de la tasa lineal).
  * Día 31: Aplica tope $15.0\%$ (Primer valor fuera del límite lineal).
  * Días 40, 100, 365: Se mantiene congelado en $15.0\%$.
* **Frontera de Alerta de Ausencias:**
  * 2 ausencias seguidas: Sin alerta (`requiereAlertaAcudiente = false`).
  * 3 ausencias seguidas: Alerta activada (`requiereAlertaAcudiente = true`).
* **Frontera de Estados de Pago (Ventana de 3 días):**
  * 4 días antes del vencimiento: `AL_DIA`.
  * 3 días antes del vencimiento: `POR_VENCER` (Límite de entrada a la ventana de aviso).
  * 0 días (Hoy = Vencimiento): `POR_VENCER`.
  * 1 día después del vencimiento: `EN_MORA`.
* **Frontera de Asistencia Mínima (80.0%):**
  * $79.99\%$: No cumple el mínimo.
  * $80.00\%$: Cumple exactamente el mínimo institucional.

### 5.3 Pruebas de Robustez y Manejo Defensivo
* **División por cero:** Se verificó que cuando un alumno solo registra faltas justificadas, la base exigible resultante es 0. El código previene la excepción aritmética y devuelve limpiamente $0.0\%$.
* **Orden cronológico garantizado:** Se verificó que si las asistencias se introducen en fechas desordenadas (ej. día 4, día 1, día 3, día 2), el Stream de `registrosDe()` ordena cronológicamente los registros antes de calcular rachas consecutivas.

---

## 6. ARQUITECTURA DE LA SUITE DE PRUEBAS EN MAVEN (JUNIT 5)

### 6.1 Configuración de `pom.xml`
```xml
<dependencies>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-api</artifactId>
        <version>5.10.2</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-params</artifactId>
        <version>5.10.2</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-engine</artifactId>
        <version>5.10.2</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```

### 6.2 Clases de Prueba Implementadas
1. **`co.edu.eam.sgap.CalculadoraMensualidadTest` (33 tests):**  
   Pruebas unitarias agrupadas con `@Nested`, usando `@ParameterizedTest`, `@CsvSource` y `@ValueSource` para evaluar recargos, pagos totales, pagos anuales y estados semafóricos.
2. **`co.edu.eam.sgap.asistencia.ControlAsistenciaTest` (36 tests):**  
   Pruebas exhaustivas para registro, normalización de cadenas (`trim`), duplicidad, conteos, cálculo porcentual, verificación de mínimo, ausencias consecutivas, alertas y ordenamiento alfabético en listas de riesgo.
3. **`co.edu.eam.sgap.AplicacionSGAPTest` (14 tests):**  
   Pruebas de integración sobre la consola de usuario, comprobando el procesamiento de los 10 comandos, parsing de fechas, manejo de entradas inválidas y captura de excepciones con mensajes amigables.
4. **`co.edu.eam.sgap.CriteriosAceptacionSGAPTest` (9 tests):**  
   Suite BDD de alto nivel orientada al cliente que comprueba punto por punto los 9 Criterios de Aceptación institucionales.

---

## 7. RESULTADOS DE EJECUCIÓN Y COBERTURA

### 7.1 Métrica Oficial de Maven Surefire
```text
-------------------------------------------------------
 T E S T S
-------------------------------------------------------
Running co.edu.eam.sgap.CriteriosAceptacionSGAPTest
Tests run: 9, Failures: 0, Errors: 0, Skipped: 0
Running co.edu.eam.sgap.CalculadoraMensualidadTest
Tests run: 33, Failures: 0, Errors: 0, Skipped: 0
Running co.edu.eam.sgap.AplicacionSGAPTest
Tests run: 14, Failures: 0, Errors: 0, Skipped: 0
Running co.edu.eam.sgap.asistencia.ControlAsistenciaTest
Tests run: 36, Failures: 0, Errors: 0, Skipped: 0

Results:
Tests run: 92, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

### 7.2 Métricas de Cobertura
* **Cobertura de Sentencias (Statement Coverage):** **100%** de los métodos y líneas de la capa de lógica de negocio (`CalculadoraMensualidad`, `ControlAsistencia`, `EstadoPago`, `EstadoAsistencia`, `RegistroAsistencia`).
* **Cobertura de Ramas (Branch Coverage):** **100%** de las condiciones lógicas y bifurcaciones (validaciones de parámetros nulos, fronteras de mora, filtros de estado y ordenamientos).

---

## 8. EVALUACIÓN CRÍTICA DEL SOFTWARE Y OPORTUNIDADES DE MEJORA

### 8.1 Fortalezas del Código Base
* **Seguridad de tipos e inmutabilidad:** El uso de Java Records para `RegistroAsistencia` garantiza que los datos no puedan ser alterados una vez creados.
* **Precisión monetaria:** Implementación matemática con `BigDecimal` y `RoundingMode.HALF_UP`.
* **Programación funcional moderna:** Empleo de Streams de Java para filtrado y ordenamiento de registros.

### 8.2 Limitaciones y Hoja de Ruta para SGAP 2.0
1. **Persistencia Volátil:** Los registros residen en una lista en memoria (`ArrayList`). Al cerrar la consola se pierde la información.  
   * *Mejora:* Integrar persistencia relacional con PostgreSQL o SQLite mediante Spring Data JPA.
2. **Restricción a una clase diaria:** La validación actual impide que un alumno tome dos asignaturas diferentes el mismo día (ej. guitarra y canto).  
   * *Mejora:* Incorporar `idClase` o `asignatura` en `RegistroAsistencia`.
3. **Acoplamiento en la Capa de Presentación:** `AplicacionSGAP` combina lectura, parseo, lógica y salida en un solo método switch.  
   * *Mejora:* Migrar hacia una arquitectura limpia (Clean Architecture / Hexagonal) con una API REST y frontend web interactivo.

---

## 9. DICTAMEN FINAL DE ACEPTACIÓN

Con base en la evidencia técnica recopilada a través de **92 casos de prueba automatizados ejecutados sin fallos**, los evaluadores emiten concepto unánime de:

> ### ✅ APROBADO Y ACEPTADO
> El sistema SGAP satisface rigurosamente todos los requerimientos funcionales, de control de asistencia y de liquidación de pagos estipulados para su versión de consola.

---

### Firmas de Responsabilidad:

```text
__________________________________             __________________________________
Jhoan Sebastián Agudelo Mejía                  Juan Pablo Bedoya Payán
Estudiante de Ingeniería de Software          Estudiante de Ingeniería de Software
Institución Universitaria EAM                  Institución Universitaria EAM
```

