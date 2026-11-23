#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del Documento Oficial de Aseguramiento de Calidad (SQA) y Pruebas de Software - SGAP
Institución Universitaria EAM - Ingeniería de Software II (ISII)
Autores: Jhoan Sebastián Agudelo Mejía & Juan Pablo Bedoya Payán
Docente: David Cano Baquero
"""

import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Plan de Aseguramiento de Calidad de Software - SGAP</title>
<style>
  @page {
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
    @bottom-right {
      content: counter(page);
    }
  }

  body {
    font-family: 'Liberation Sans', 'DejaVu Sans', Arial, Helvetica, sans-serif;
    color: #1e293b;
    line-height: 1.5;
    font-size: 10.5pt;
    margin: 0;
    padding: 0;
  }

  h1, h2, h3, h4 {
    color: #0f172a;
    font-weight: 700;
  }

  h1 {
    font-size: 18pt;
    border-bottom: 2.5px solid #1e3a8a;
    padding-bottom: 6px;
    margin-top: 24pt;
    margin-bottom: 12pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  h2 {
    font-size: 13pt;
    color: #1e3a8a;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 4px;
    margin-top: 18pt;
    margin-bottom: 8pt;
  }

  h3 {
    font-size: 11pt;
    color: #334155;
    margin-top: 14pt;
    margin-bottom: 6pt;
  }

  h4 {
    font-size: 10.5pt;
    color: #475569;
    margin-top: 10pt;
    margin-bottom: 4pt;
    font-style: italic;
  }

  p {
    margin-top: 0;
    margin-bottom: 8pt;
    text-align: justify;
  }

  ul, ol {
    margin-top: 0;
    margin-bottom: 8pt;
    padding-left: 20px;
  }

  li {
    margin-bottom: 3pt;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 8pt;
    margin-bottom: 14pt;
    font-size: 9pt;
  }

  th, td {
    border: 1px solid #cbd5e1;
    padding: 5pt 7pt;
    text-align: left;
    vertical-align: top;
  }

  th {
    background-color: #1e3a8a;
    color: #ffffff;
    font-weight: 600;
    text-transform: uppercase;
    font-size: 8.5pt;
    letter-spacing: 0.3px;
  }

  tr:nth-child(even) {
    background-color: #f8fafc;
  }

  .badge-pass {
    background-color: #dcfce7;
    color: #166534;
    font-weight: bold;
    padding: 2px 6px;
    border-radius: 4px;
    display: inline-block;
    border: 1px solid #86efac;
  }

  .badge-fail {
    background-color: #fee2e2;
    color: #991b1b;
    font-weight: bold;
    padding: 2px 6px;
    border-radius: 4px;
    display: inline-block;
    border: 1px solid #fca5a5;
  }

  .badge-unit {
    background-color: #e0f2fe;
    color: #0369a1;
    font-weight: bold;
    padding: 2px 6px;
    border-radius: 4px;
    display: inline-block;
  }

  .badge-integ {
    background-color: #fef3c7;
    color: #92400e;
    font-weight: bold;
    padding: 2px 6px;
    border-radius: 4px;
    display: inline-block;
  }

  pre, code {
    font-family: 'DejaVu Sans Mono', 'Liberation Mono', Courier, monospace;
  }

  pre {
    background-color: #0f172a;
    color: #f8fafc;
    padding: 8pt 10pt;
    border-radius: 4px;
    font-size: 8.5pt;
    line-height: 1.35;
    overflow-x: auto;
    margin-top: 6pt;
    margin-bottom: 10pt;
    border: 1px solid #334155;
  }

  code {
    background-color: #f1f5f9;
    color: #b91c1c;
    padding: 1px 4px;
    border-radius: 3px;
    font-size: 9pt;
  }

  pre code {
    background-color: transparent;
    color: inherit;
    padding: 0;
  }

  .callout {
    background-color: #f0fdf4;
    border-left: 4px solid #16a34a;
    padding: 8pt 12pt;
    margin-top: 8pt;
    margin-bottom: 12pt;
    border-radius: 0 4px 4px 0;
  }

  .callout-info {
    background-color: #eff6ff;
    border-left: 4px solid #2563eb;
    padding: 8pt 12pt;
    margin-top: 8pt;
    margin-bottom: 12pt;
    border-radius: 0 4px 4px 0;
  }

  .callout-warning {
    background-color: #fffbeb;
    border-left: 4px solid #d97706;
    padding: 8pt 12pt;
    margin-top: 8pt;
    margin-bottom: 12pt;
    border-radius: 0 4px 4px 0;
  }

  .page-break {
    page-break-before: always;
  }

  .cover-page {
    text-align: center;
    padding-top: 40pt;
    page-break-after: always;
  }

  .cover-institution {
    font-size: 14pt;
    font-weight: 700;
    color: #1e3a8a;
    text-transform: uppercase;
    margin-bottom: 4pt;
    letter-spacing: 1px;
  }

  .cover-faculty {
    font-size: 11pt;
    color: #475569;
    margin-bottom: 30pt;
  }

  .cover-title {
    font-size: 20pt;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.25;
    margin-top: 30pt;
    margin-bottom: 15pt;
    text-transform: uppercase;
  }

  .cover-subtitle {
    font-size: 12pt;
    color: #2563eb;
    font-weight: 600;
    margin-bottom: 60pt;
  }

  .cover-metadata {
    margin-top: 60pt;
    font-size: 11pt;
    line-height: 1.8;
  }

  .cover-footer {
    margin-top: 80pt;
    font-size: 10pt;
    color: #64748b;
  }

  .reference-item {
    padding-left: 28pt;
    text-indent: -28pt;
    margin-bottom: 8pt;
    text-align: justify;
    font-size: 9.5pt;
  }
</style>
</head>
<body>

<!-- ==================== PORTADA ==================== -->
<div class="cover-page">
  <div class="cover-institution">Institución Universitaria EAM</div>
  <div class="cover-faculty">Facultad de Ingeniería — Programa de Ingeniería de Software<br>Armenia, Quindío</div>

  <div style="height: 25pt;"></div>

  <div class="cover-title">Plan de Aseguramiento de Calidad de Software (SQA), Métodos de Prueba y Automatización con JUnit 5</div>
  <div class="cover-subtitle">Sistema de Gestión de Asistencia y Pagos (SGAP) — Versión 1.0.0</div>

  <div style="height: 35pt;"></div>

  <div class="cover-metadata">
    <strong>Asignatura:</strong> Ingeniería de Software II (ISII) — Pruebas y Calidad de Software<br>
    <strong>Docente Evaluador:</strong> Mg. David Cano Baquero<br><br>
    <strong>Autores y Desarrolladores:</strong><br>
    <strong>Jhoan Sebastián Agudelo Mejía</strong> (Código Estudiantil EAM)<br>
    <strong>Juan Pablo Bedoya Payán</strong> (Código Estudiantil EAM)<br><br>
    <strong>Entorno Tecnológico:</strong> Java 17 LTS | JUnit Jupiter 5.10.2 | Apache Maven 3.10 | Surefire 3.1.2
  </div>

  <div class="cover-footer">
    Armenia, Quindío — Colombia<br>
    Noviembre de 2026
  </div>
</div>

<!-- ==================== TABLA DE CONTENIDO RESUMIDA ==================== -->
<h2>Tabla de Contenido General</h2>
<ul>
  <li><strong>1. Introducción y Contexto del Proyecto SGAP</strong></li>
  <li><strong>2. Catálogo de Requisitos Funcionales Corregidos y Verificables (RF-01 al RF-10)</strong></li>
  <li><strong>3. Resultados Completos de la Guía Anterior</strong> (Experimento de edad, conceptualización Error-Defecto-Fallo, pruebas por nivel y simulación de aceptación)</li>
  <li><strong>4. Etapa 1: Métodos de Prueba (Caja Negra y Caja Blanca)</strong>
    <ul>
      <li>4.1 Investigación Teórica (Particiones, Valores Límite, Tablas de Decisión, Cobertura McCabe) [APA 7]</li>
      <li>4.2 Aplicación Práctica: Particiones y Límites para 3 Requisitos (RF-04, RF-03/RF-07, RF-05)</li>
      <li>4.3 Tabla de Decisión Completa del Requisito Financiero y de Cartera</li>
      <li>4.4 Análisis de Caja Blanca: Grafo de Flujo (CFG), Complejidad Ciclomática y Caminos Básicos en Java</li>
    </ul>
  </li>
  <li><strong>5. Etapa 2: Plan de Pruebas y Casos de Prueba</strong>
    <ul>
      <li>5.1 Investigación Teórica: Estructura según IEEE 829 / ISO/IEC/IEEE 29119-3 y Matriz RTM [APA 7]</li>
      <li>5.2 Plan de Pruebas Integral del Proyecto SGAP (3 páginas formales)</li>
      <li>5.3 Catálogo Exhaustivo de 16 Casos de Prueba Documentados (CP-01 a CP-16)</li>
      <li>5.4 Matriz de Trazabilidad de Requisitos (RTM)</li>
      <li>5.5 Registro Real de Defectos Encontrados y Corregidos (Bug Tracking Log)</li>
    </ul>
  </li>
  <li><strong>6. Etapa 3: Automatización de Pruebas</strong>
    <ul>
      <li>6.1 Investigación Teórica: Criterios de Automatización, JUnit 5 y Maven/Gradle [APA 7]</li>
      <li>6.2 Aplicación Práctica: Suite de 92 Pruebas en el Repositorio (Límites e Integración Real)</li>
      <li>6.3 Informe Técnico Oficial de Ejecución de JUnit 5 Surefire</li>
      <li>6.4 Justificación de Casos Mantenidos en Modalidad Manual</li>
    </ul>
  </li>
  <li><strong>7. Etapa 4: Calidad del Software</strong>
    <ul>
      <li>7.1 Investigación Teórica: ISO/IEC 25010, Niveles CMMI v2.0 y QA en Marcos Ágiles [APA 7]</li>
      <li>7.2 Selección y Justificación Técnica de 3 Características ISO/IEC 25010 en SGAP</li>
      <li>7.3 Autoevaluación Honesta en CMMI (Nivel 2) y Plan de Acción hacia Nivel 3</li>
      <li>7.4 Definición de Terminado (Definition of Done - DoD) con 7 Condiciones Verificables</li>
    </ul>
  </li>
  <li><strong>8. Conclusiones y Lecciones Aprendidas</strong></li>
  <li><strong>9. Matriz de Aportes y Dedicación por Integrante</strong></li>
  <li><strong>10. Declaración Ética de Uso de Herramientas de Inteligencia Artificial</strong></li>
  <li><strong>11. Referencias Bibliográficas (Normas APA 7.ª Edición)</strong></li>
  <li><strong>Anexo A: Guion Oficial para el Video de Sustentación (15 Minutos)</strong></li>
</ul>

<div class="page-break"></div>

<!-- ==================== SECCIÓN 1 ==================== -->
<h1>1. Introducción y Contexto del Proyecto SGAP</h1>

<p>
El software <strong>SGAP (Sistema de Gestión de Asistencia y Pagos)</strong> es una solución de ingeniería desarrollada para sistematizar, estandarizar y auditar dos procesos operativos altamente críticos en academias formativas (escuelas deportivas de fútbol, natación, artes marciales y conservatorios de música): <strong>(1) el control de asistencia y deserción temprana</strong>, y <strong>(2) la liquidación transparente de mensualidades y moras</strong>.
</p>

<h3>1.1 Problemática Operativa Identificada</h3>
<p>
Históricamente, las pequeñas y medianas academias formativas gestionan el aforo y el flujo de caja mediante planillas físicas en papel o libros manuales de cálculo (Excel). Esta operatividad artesanal introduce tres riesgos severos que amenazan la sostenibilidad de la institución:
</p>
<ul>
  <li><strong>Deserción inadvertida de estudiantes:</strong> Cuando un alumno comienza a faltar de manera consecutiva por desmotivación o problemas personales, la dirección administrativa suele identificar el problema semanas después, cuando el acudiente formaliza el retiro. SGAP mitiga esto mediante un detector algorítmico de rachas que dispara alertas preventivas al alcanzar exactamente tres inasistencias injustificadas seguidas.</li>
  <li><strong>Disputas de cobro por liquidaciones de mora arbitrarias:</strong> La falta de un cálculo automatizado genera cobros conflictivos con los acudientes. SGAP fija un recargo diario transparente del 0.5% pero impone un blindaje institucional inquebrantable con tope máximo del 15%, liquidado con precisión decimal mediante <code>BigDecimal</code>.</li>
  <li><strong>Injusticia académica ante excusas de fuerza mayor:</strong> En los cálculos manuales tradicionales, las inasistencias médicas o justificadas se promedian en contra del estudiante reduciendo su porcentaje. SGAP descuenta formalmente las clases justificadas del divisor base, garantizando un cálculo ponderado justo.</li>
</ul>

<h3>1.2 Alcance y Arquitectura Técnica del Sistema</h3>
<p>
SGAP está estructurado bajo las mejores prácticas de la ingeniería de software en Java 17 LTS, desacoplando estrictamente la lógica del dominio de la interfaz de consola:
</p>
<ul>
  <li><strong>Capa de Dominio y Modelado:</strong> Emplea <code>Java Records</code> (<code>RegistroAsistencia</code>) que aseguran inmutabilidad y seguridad de tipos frente a efectos secundarios, junto con enums tipados (<code>EstadoAsistencia</code>, <code>EstadoPago</code>).</li>
  <li><strong>Capa de Lógica de Negocio:</strong> Implementada en las clases <code>ControlAsistencia</code> y <code>CalculadoraMensualidad</code>, procesando colecciones mediante la API de Streams y aplicando redondeo bancario formal (<code>RoundingMode.HALF_UP</code>).</li>
  <li><strong>Capa de Presentación:</strong> Consola interactiva (<code>AplicacionSGAP</code>) con validación defensiva de comandos, fechas y números.</li>
</ul>

<div class="page-break"></div>

<!-- ==================== SECCIÓN 2 ==================== -->
<h1>2. Catálogo de Requisitos Funcionales Corregidos (RF-01 al RF-10)</h1>
<p>
A partir de la guía anterior, se retoman los requisitos originales RF-01 a RF-05, refinando sus ambigüedades e incorporando 5 requisitos complementarios para totalizar <strong>10 Requisitos Funcionales (RF-01 al RF-10)</strong> rigurosamente verificables:
</p>

<table>
  <thead>
    <tr>
      <th style="width: 10%;">ID</th>
      <th style="width: 25%;">Nombre del Requisito</th>
      <th style="width: 50%;">Descripción Operativa y Lógica de Negocio</th>
      <th style="width: 15%;">Criterio de Verificación</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>RF-01</strong></td>
      <td>Registro y unicidad de asistencia diaria</td>
      <td>El sistema debe permitir registrar la asistencia de un alumno (<code>PRESENTE</code>, <code>TARDE</code>, <code>AUSENTE</code>, <code>JUSTIFICADO</code>) para una fecha (<code>LocalDate</code>). Debe rechazar inmediatamente con <code>IllegalStateException</code> cualquier segundo intento de registro para el mismo estudiante en la misma fecha.</td>
      <td>Rechazo de duplicados con excepción y persistencia única.</td>
    </tr>
    <tr>
      <td><strong>RF-02</strong></td>
      <td>Cálculo ponderado de porcentaje de asistencia</td>
      <td>El sistema debe computar el porcentaje de asistencia acumulado considerando que: (a) <code>PRESENTE</code> y <code>TARDE</code> computan como asistencias efectivas (100%), (b) <code>JUSTIFICADO</code> se descuenta de la base evaluable (divisor), y (c) <code>AUSENTE</code> computa como inasistencia. Si la base resultante es 0, el porcentaje debe retornar 0.0% sin división por cero.</td>
      <td>Resultado exacto con 2 decimales y neutralidad de justificaciones.</td>
    </tr>
    <tr>
      <td><strong>RF-03</strong></td>
      <td>Alerta temprana por ausencias consecutivas</td>
      <td>El sistema debe evaluar cronológicamente los registros de un alumno y retornar un valor booleano (<code>true/false</code>). Se requiere alerta al acudiente si y solo si el alumno acumula una racha mayor o igual a 3 ausencias injustificadas consecutivas (<code>&gt;= 3</code>).</td>
      <td>Frontera exacta: 2 ausencias dan false; 3 ausencias dan true.</td>
    </tr>
    <tr>
      <td><strong>RF-04</strong></td>
      <td>Recargo por mora con tope institucional del 15%</td>
      <td>El sistema debe liquidar el recargo por mora aplicando una tasa del 0.5% diario sobre la mensualidad. La tasa nunca podrá exceder el tope institucional del 15.0% (alcanzado a los 30 días). El cálculo debe ejecutarse con <code>BigDecimal</code> y redondeo <code>HALF_UP</code>.</td>
      <td>Día 29 (14.5%), Día 30 (15.0%), Día 31 en adelante (15.0% fijo).</td>
    </tr>
    <tr>
      <td><strong>RF-05</strong></td>
      <td>Semáforo de cobro con ventana preventiva</td>
      <td>El sistema debe comparar la fecha de vencimiento contra la fecha actual y clasificar la mensualidad en: <code>AL_DIA</code> (más de 3 días faltantes), <code>POR_VENCER</code> (entre 0 y 3 días faltantes inclusive) o <code>EN_MORA</code> (fecha actual posterior al vencimiento).</td>
      <td>Frontera: 4 días (AL_DIA), 3 días (POR_VENCER), 0 días (POR_VENCER), +1 día (EN_MORA).</td>
    </tr>
    <tr>
      <td><strong>RF-06</strong></td>
      <td>Corrección y actualización de asistencia</td>
      <td>El sistema debe permitir rectificar el estado de asistencia previamente registrado para un estudiante en una fecha específica. Si el registro existe, actualiza su estado; si no existe, debe arrojar <code>IllegalStateException</code>.</td>
      <td>Actualización efectiva en memoria y rechazo ante registros inexistentes.</td>
    </tr>
    <tr>
      <td><strong>RF-07</strong></td>
      <td>Detección y reporte de alumnos en riesgo (&lt; 80%)</td>
      <td>El sistema debe filtrar y retornar en orden alfabético estricto la lista de aquellos estudiantes cuyo porcentaje de asistencia calculado sea estrictamente inferior al porcentaje mínimo institucional (80.0%).</td>
      <td>Filtrado estricto (&lt; 80.0%) y ordenamiento alfabético mediante <code>TreeSet</code>.</td>
    </tr>
    <tr>
      <td><strong>RF-08</strong></td>
      <td>Liquidación de matrícula anual con descuento</td>
      <td>El sistema debe liquidar el valor del pago anual anticipado multiplicando el valor de la mensualidad ordinaria exactamente por 10 (otorgando 2 meses de descuento comercial por pronto pago).</td>
      <td>Fórmula: $Monto \times 10$, escala a 2 decimales.</td>
    </tr>
    <tr>
      <td><strong>RF-09</strong></td>
      <td>Auditoría y conteo de aforo diario</td>
      <td>El sistema debe calcular la cantidad total de estudiantes que asistieron a la sede en una fecha determinada, sumando únicamente los registros con estado <code>PRESENTE</code> y <code>TARDE</code>, excluyendo ausentes y justificados.</td>
      <td>Conteo exacto de asistentes físicos en la jornada.</td>
    </tr>
    <tr>
      <td><strong>RF-10</strong></td>
      <td>Robustez y manejo defensivo de entradas en consola</td>
      <td>La interfaz de usuario en consola debe capturar excepciones por formatos de fecha inválidos, montos no numéricos, argumentos insuficientes y nombres en blanco, emitiendo mensajes de error claros sin provocar caídas (crash) del sistema.</td>
      <td>Captura de <code>DateTimeParseException</code>, <code>NumberFormatException</code> y <code>IllegalArgumentException</code>.</td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<!-- ==================== SECCIÓN 3 ==================== -->
<h1>3. Resultados Completos de la Guía Anterior</h1>

<h3>3.1 Conjetura Previa y Análisis del Experimento de Límites de Edad</h3>
<p>
En la guía inicial se evaluó el requisito <em>"La edad debe estar entre 18 y 120 años, ambos incluidos"</em> frente a tres casos de prueba diseñados (CP-01: 25 años, CP-02: 18 años, CP-03: 17 años).
</p>
<div class="callout-info">
  <strong>Conjetura previa formulada por el equipo:</strong><br>
  <em>"Conjeturamos que CP-01 pasará normalmente y que CP-02 va a fallar. En programación es sumamente frecuente que se confunda la mayoría de edad con una comparación relacional estricta (<code>edad &gt; 18</code>) en vez de inclusiva (<code>edad &gt;= 18</code>). Si el código presenta ese defecto, el límite inferior de 18 años será rechazado erróneamente arrojando false, mientras que 25 dará true y 17 dará false por coincidencia."</em>
</div>
<p><strong>Resultado real de ejecución:</strong></p>
<ul>
  <li><code>CP-01 (edad 25):</code> Esperado = true | Obtenido = true &rarr; <span class="badge-pass">APROBÓ</span></li>
  <li><code>CP-02 (edad 18):</code> Esperado = true | Obtenido = false &rarr; <span class="badge-fail">FALLÓ</span></li>
  <li><code>CP-03 (edad 17):</code> Esperado = false | Obtenido = false &rarr; <span class="badge-pass">APROBÓ</span></li>
</ul>
<p>
<strong>Análisis del hallazgo:</strong> Se confirmó con exactitud la conjetura. El código base contenía la expresión defectuosa <code>return edad &gt; 18 &amp;&amp; edad &lt;= 120;</code>. Este experimento demostró que los valores intermedios (25) o externos lejanos (17) ocultan los errores de programación, y que son las pruebas en los <strong>valores límite (fronteras)</strong> las que revelan los defectos latentes. Asimismo, ratifica el axioma fundamental de la ingeniería de software: <em>las pruebas demuestran la presencia de defectos, pero nunca su ausencia absoluta</em>.
</p>

<h3>3.2 Respuestas Conceptuales a Preguntas de Comprobación</h3>
<ol>
  <li><strong>Diferenciación entre Error, Defecto y Fallo:</strong>
    <ul>
      <li><em>Error (Equivocación humana):</em> Acción cognitiva errónea cometida por el ingeniero o analista (ej. pensar que "a partir de 18" excluye el 18).</li>
      <li><em>Defecto (Bug en el artefacto):</em> Representación estática del error en el código fuente (ej. escribir <code>edad &gt; 18</code> en lugar de <code>edad &gt;= 18</code>).</li>
      <li><em>Fallo (Manifestación dinámica):</em> Discrepancia observable durante la ejecución entre el resultado producido y el esperado (ej. el sistema arroja "Rechazado" a un ciudadano de 18 años).</li>
    </ul>
  </li>
  <li><strong>Falla de Verificación vs. Falla de Validación:</strong>
    <p>
      Si el sistema cumple a cabalidad lo especificado en el documento de requisitos pero el cliente manifiesta que no resuelve su necesidad, <strong>falló la VALIDACIÓN</strong>. La verificación responde a la pregunta <em>¿construimos el producto correctamente?</em> (conforme a la especificación escrita). La validación responde a <em>¿construimos el producto correcto?</em> (conforme a las necesidades y expectativas reales del cliente en su contexto operacional).
    </p>
  </li>
  <li><strong>¿Por qué una prueba de sistema detecta el fallo pero no aísla la clase responsable?</strong>
    <p>
      Porque las pruebas de sistema son de <strong>caja negra</strong> y evalúan el comportamiento holístico de extremo a extremo (E2E). En ellas colaboran concurrentemente múltiples componentes (Consola, Controladores, Lógica de Negocio, Validadores y Repositorios). Al observar una salida incorrecta en la terminal, se constata el fallo global pero no se tiene visibilidad interna de qué línea o clase originó la anomalía; para aislar la causa raíz se requiere descender al nivel de <strong>pruebas unitarias</strong>.
    </p>
  </li>
  <li><strong>¿Pasar tres casos de prueba garantiza la ausencia de defectos?</strong>
    <p>
      <strong>NO.</strong> Uno de los siete principios del testing (ISTQB) establece la imposibilidad de las pruebas exhaustivas. Evaluar tres entradas puntuales únicamente valida el comportamiento en esas tres coordenadas; no garantiza qué ocurrirá en el límite superior (edad 120 o 121), ante números negativos (-5), desbordamientos de enteros o valores nulos.
    </p>
  </li>
</ol>

<h3>3.3 Matriz de Error, Defecto y Fallo Aplicada a SGAP</h3>
<table>
  <thead>
    <tr>
      <th>Concepto</th>
      <th>Caso RF-04 (Mora — Tope 15% / Frontera)</th>
      <th>Caso RF-03 (Alerta Ausencias Consecutivas)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Error (Mental)</strong></td>
      <td>El desarrollador asume que el recargo diario por mora crece indefinidamente de forma lineal y olvida la directriz de protección al cliente.</td>
      <td>El programador malinterpreta la frase "alerta a partir de 3 inasistencias" asumiendo que debe superar estrictamente tres faltas (&gt; 3).</td>
    </tr>
    <tr>
      <td><strong>Defecto (Código)</strong></td>
      <td>Omitir el condicional de cota superior en <code>CalculadoraMensualidad</code>: liquidar <code>dias * 0.005</code> sin imponer <code>compareTo(TOPE_RECARGO) &gt; 0</code>.</td>
      <td>Escribir la comparación relacional estricta <code>racha &gt; 3</code> en lugar del operador inclusivo <code>racha &gt;= 3</code> en <code>requiereAlertaAcudiente</code>.</td>
    </tr>
    <tr>
      <td><strong>Fallo (Ejecución)</strong></td>
      <td>Un acudiente con 40 días de retraso recibe un recargo abusivo del 20% ($20.000) en vez del tope legal de $15.000, generando reclamos legales.</td>
      <td>Un alumno acumula 3 faltas consecutivas y el sistema devuelve <code>false</code> (sin alerta), perdiéndose la oportunidad de frenar la deserción.</td>
    </tr>
  </tbody>
</table>

<h3>3.4 Pruebas por Nivel en SGAP</h3>
<table>
  <thead>
    <tr>
      <th>Nivel de Prueba</th>
      <th>Objetivo en SGAP</th>
      <th>Componentes Involucrados</th>
      <th>Muestra Representativa</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="badge-unit">Unitaria</span></td>
      <td>Verificar métodos puros de cálculo y decisiones lógicas sin dependencias de estado.</td>
      <td><code>CalculadoraMensualidad.java</code>, métodos de validación privada.</td>
      <td>Cálculo de recargo diario al 0.5% y congelamiento en el tope del 15%.</td>
    </tr>
    <tr>
      <td><span class="badge-integ">Integración</span></td>
      <td>Verificar la interacción colaborativa entre clases de dominio y estructuras de datos en memoria.</td>
      <td><code>ControlAsistencia</code> colaborando con <code>RegistroAsistencia</code> y <code>EstadoAsistencia</code>.</td>
      <td>Rechazo de registro duplicado en la misma fecha y deducción de justificaciones en el divisor base.</td>
    </tr>
    <tr>
      <td><span class="badge-unit">Sistema (E2E)</span></td>
      <td>Evaluar la aplicación completa ejecutada como caja negra simulando la terminal de usuario.</td>
      <td><code>AplicacionSGAP.java</code> integrando todas las capas con streams de consola.</td>
      <td>Procesamiento del comando de terminal <code>estadopago 2026-11-10;2026-11-08</code> arrojando <code>POR_VENCER</code>.</td>
    </tr>
    <tr>
      <td><span class="badge-pass">Aceptación (BDD)</span></td>
      <td>Validar el cumplimiento formal de los criterios del negocio desde la óptica del cliente (academia).</td>
      <td><code>CriteriosAceptacionSGAPTest.java</code> (especificaciones Dado-Cuando-Entonces).</td>
      <td>Verificación de los 9 criterios de negocio institucionales (CA-01 al CA-09).</td>
    </tr>
  </tbody>
</table>

<h3>3.5 Resultados de la Simulación de Aceptación con Equipo Evaluador</h3>
<p>
Durante la sesión de simulación con un equipo evaluador actuando en el rol de directivos de una academia formativa, se sometieron a comprobación tres criterios fundamentales de negocio:
</p>
<ul>
  <li><strong>CA-01 (Protección ante excusas médicas):</strong> Se simularon 1 asistencia, 1 retardo y 1 excusa justificada. <em>Resultado:</em> El sistema calculó 100.0% deduciendo la clase justificada. <span class="badge-pass">ACEPTADO</span>.</li>
  <li><strong>CA-02 (Alerta preventiva de inasistencia):</strong> Se ingresaron 2 ausencias continuas (sin alerta) y al ingresar la 3.ª se disparó la notificación inmediata. <span class="badge-pass">ACEPTADO</span>.</li>
  <li><strong>CA-03 (Protección financiera de tope de mora):</strong> Se liquidó una mensualidad de $100.000 con 45 días de retraso. <em>Resultado:</em> El recargo se congeló estrictamente en $15.000 (15.0%). <span class="badge-pass">ACEPTADO</span>.</li>
</ul>

<div class="page-break"></div>

<!-- ==================== SECCIÓN 4 ==================== -->
<h1>4. Etapa 1: Métodos de Prueba (Caja Negra y Caja Blanca)</h1>

<h3>4.1 Investigación Teórica Formal (Citada en APA 7)</h3>
<p>
El diseño riguroso de pruebas de software se fundamenta en dos paradigmas complementarios: las técnicas basadas en la especificación o de <strong>caja negra</strong>, y las técnicas basadas en la estructura o de <strong>caja blanca</strong> (Pressman &amp; Maxim, 2020; Sommerville, 2016).
</p>
<p>
Dentro de la caja negra, la <strong>Partición en Clases de Equivalencia (Equivalence Partitioning)</strong> postula que el dominio de entrada de un programa puede dividirse en subconjuntos disjuntos de datos, de modo que si un caso de prueba dentro de una clase detecta un defecto, cualquier otro dato de esa misma clase se comportará de forma equivalente (Myers et al., 2011). Esto permite reducir un universo infinito de entradas a un conjunto finito y representativo de clases válidas e inválidas. Complementariamente, el <strong>Análisis de Valores Límite (Boundary Value Analysis - BVA)</strong> se sustenta en la evidencia empírica de que la mayor densidad de defectos de programación no ocurre en el centro de las particiones, sino en sus fronteras extremas (Copeland, 2004). Por ende, el estándar ISO/IEC/IEEE 29119-4 (2021) prescribe evaluar sistemáticamente los valores inmediatamente anteriores, exactos y posteriores a cada frontera de decisión.
</p>
<p>
Cuando los requisitos involucran combinaciones lógicas complejas de condiciones que desencadenan diferentes cursos de acción, las <strong>Tablas de Decisión</strong> constituyen la técnica de caja negra más idónea. Una tabla de decisión mapea exhaustivamente un vector booleano de $2^n$ combinaciones de condiciones sobre un conjunto de acciones operativas, garantizando la completitud lógica del software y evitando contradicciones o caminos no especificados en los requerimientos (Pressman &amp; Maxim, 2020).
</p>
<p>
Por su parte, las técnicas de caja blanca auditan la estructura de control interna del código fuente. La <strong>Cobertura de Sentencias (Statement Coverage)</strong> exige que cada instrucción ejecutable del programa haya sido recorrida al menos una vez durante las pruebas. Sin embargo, dicha cobertura es débil, pues un conjunto de pruebas puede cubrir el 100% de las sentencias y no detectar defectos en caminos condicionales no transitados (Sommerville, 2016). Para subsanar esta limitación, la <strong>Cobertura de Ramas (Branch Coverage)</strong> demanda que cada rama o bifurcación condicional (evaluaciones verdadera y falsa de cada predicado) sea transitada por los casos de prueba. Finalmente, la técnica del <strong>Camino Básico</strong>, propuesta originalmente por Thomas McCabe (1976), cuantifica la complejidad lógica de un módulo mediante la <em>Complejidad Ciclomática</em> $V(G)$, la cual determina el número máximo de caminos linealmente independientes necesarios para asegurar que todas las sentencias y ramas sean recorridas, suministrando una cota superior estricta para la suite de pruebas unitarias.
</p>

<h3>4.2 Aplicación Práctica: Particiones y Valores Límite para 3 Requisitos</h3>

<h4>Aplicación 1: Requisito RF-04 (Recargo por mora con tope del 15%)</h4>
<p><strong>Clases de Equivalencia:</strong></p>
<ul>
  <li><code>CE-01 (Válida - Sin Mora):</code> Días de mora $= 0$. Recargo $= \$0.00$.</li>
  <li><code>CE-02 (Válida - Mora Proporcional):</code> $1 \le \text{Días de mora} \le 29$. Tasa lineal $= \text{días} \times 0.5\%$.</li>
  <li><code>CE-03 (Válida - Mora Topada):</code> $\text{Días de mora} \ge 30$. Tasa fija $= 15.0\%$.</li>
  <li><code>CE-04 (Inválida - Días Negativos):</code> $\text{Días de mora} &lt; 0$. Excepción <code>IllegalArgumentException</code>.</li>
  <li><code>CE-05 (Inválida - Mensualidad &le; 0 o null):</code> Mensualidad $\le 0$ o <code>null</code>. Excepción <code>IllegalArgumentException</code>.</li>
</ul>
<p><strong>Análisis de Valores Límite (BVA):</strong> Evaluando una mensualidad base de $\$100.000$:</p>
<table>
  <thead>
    <tr><th>Valor Límite</th><th>Días de Mora</th><th>Tasa Aplicada</th><th>Monto Esperado</th><th>Tipo de Frontera</th></tr>
  </thead>
  <tbody>
    <tr><td>Límite inferior</td><td>0 días</td><td>0.0%</td><td>$0.00</td><td>Frontera exacta sin mora</td></tr>
    <tr><td>Interior lineal</td><td>1 día</td><td>0.5%</td><td>$500.00</td><td>Primer día de mora</td></tr>
    <tr><td>Pre-frontera de tope</td><td>29 días</td><td>14.5%</td><td>$14.500.00</td><td>Inmediatamente anterior al tope</td></tr>
    <tr><td>Frontera exacta tope</td><td>30 días</td><td>15.0%</td><td>$15.000.00</td><td>Punto exacto de transición al tope</td></tr>
    <tr><td>Post-frontera tope</td><td>31 días</td><td>15.0% (tope)</td><td>$15.000.00</td><td>Primer día congelado en tope</td></tr>
    <tr><td>Límite extremo</td><td>40, 100 días</td><td>15.0% (tope)</td><td>$15.000.00</td><td>Comportamiento asintótico</td></tr>
  </tbody>
</table>

<h4>Aplicación 2: Requisito RF-03 / RF-07 (Alertas de inasistencia y porcentaje mínimo)</h4>
<p><strong>Clases de Equivalencia y Límites:</strong></p>
<ul>
  <li><code>Frontera Alerta Ausencias:</code> 2 ausencias seguidas &rarr; <code>alerta = false</code> | 3 ausencias seguidas &rarr; <code>alerta = true</code> | 4 ausencias seguidas &rarr; <code>alerta = true</code>.</li>
  <li><code>Frontera Mínimo Asistencia (80.0%):</code> $79.99\%$ &rarr; <code>cumple = false</code> (Estudiante en Riesgo) | $80.00\%$ &rarr; <code>cumple = true</code> (Normal) | $80.01\%$ &rarr; <code>cumple = true</code>.</li>
</ul>

<h4>Aplicación 3: Requisito RF-05 (Estados de pago con ventana preventiva de 3 días)</h4>
<p><strong>Análisis de Valores Límite sobre fecha de vencimiento fija (ej. 10 de Noviembre):</strong></p>
<table>
  <thead>
    <tr><th>Fecha de Consulta</th><th>Días Faltantes</th><th>Estado Esperado</th><th>Justificación de la Frontera</th></tr>
  </thead>
  <tbody>
    <tr><td>06 de Noviembre</td><td>4 días</td><td><code>AL_DIA</code></td><td>Justo antes de ingresar a la ventana preventiva.</td></tr>
    <tr><td>07 de Noviembre</td><td>3 días</td><td><code>POR_VENCER</code></td><td>Frontera exacta de ingreso a la ventana de 3 días.</td></tr>
    <tr><td>09 de Noviembre</td><td>1 día</td><td><code>POR_VENCER</code></td><td>Dentro de la ventana preventiva.</td></tr>
    <tr><td>10 de Noviembre</td><td>0 días (Hoy)</td><td><code>POR_VENCER</code></td><td>Día límite de pago.</td></tr>
    <tr><td>11 de Noviembre</td><td>-1 día (Vencido)</td><td><code>EN_MORA</code></td><td>Primer día posterior al vencimiento (Transición a Mora).</td></tr>
  </tbody>
</table>

<div class="page-break"></div>

<h3>4.3 Tabla de Decisión Completa: Requisito Financiero y de Cartera</h3>
<p>
Para formalizar la lógica combinada de cobranza y estado de cartera (RF-04, RF-05, RF-08), se modela la siguiente Tabla de Decisión compuesta:
</p>

<table>
  <thead>
    <tr>
      <th style="width: 35%;">Condiciones y Acciones</th>
      <th style="width: 8%;">R1</th>
      <th style="width: 8%;">R2</th>
      <th style="width: 8%;">R3</th>
      <th style="width: 8%;">R4</th>
      <th style="width: 8%;">R5</th>
      <th style="width: 8%;">R6</th>
      <th style="width: 8%;">R7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="8" style="background-color: #f1f5f9; font-weight: bold; color: #1e3a8a;">CONDICIONES (Entradas)</td>
    </tr>
    <tr>
      <td><strong>C1:</strong> ¿Modalidad es Pago Anual Anticipado?</td>
      <td>V</td>
      <td>F</td>
      <td>F</td>
      <td>F</td>
      <td>F</td>
      <td>F</td>
      <td>F</td>
    </tr>
    <tr>
      <td><strong>C2:</strong> ¿Fecha actual posterior a vencimiento? (hoy &gt; vencimiento)</td>
      <td>-</td>
      <td>F</td>
      <td>F</td>
      <td>V</td>
      <td>V</td>
      <td>V</td>
      <td>-</td>
    </tr>
    <tr>
      <td><strong>C3:</strong> ¿Días restantes &le; 3 días? (0 &le; faltantes &le; 3)</td>
      <td>-</td>
      <td>F</td>
      <td>V</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td><strong>C4:</strong> ¿Días de mora &gt; 30 días?</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>F (0d)</td>
      <td>F (1-29d)</td>
      <td>V (&ge;30d)</td>
      <td>-</td>
    </tr>
    <tr>
      <td><strong>C5:</strong> ¿Mensualidad &le; 0 o datos nulos?</td>
      <td>F</td>
      <td>F</td>
      <td>F</td>
      <td>F</td>
      <td>F</td>
      <td>F</td>
      <td>V</td>
    </tr>
    <tr>
      <td colspan="8" style="background-color: #f1f5f9; font-weight: bold; color: #1e3a8a;">ACCIONES (Salidas)</td>
    </tr>
    <tr>
      <td><strong>A1:</strong> Clasificar estado como <code>AL_DIA</code></td>
      <td>-</td>
      <td><strong>X</strong></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td><strong>A2:</strong> Clasificar estado como <code>POR_VENCER</code></td>
      <td>-</td>
      <td>-</td>
      <td><strong>X</strong></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td><strong>A3:</strong> Clasificar estado como <code>EN_MORA</code></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td><strong>X</strong></td>
      <td><strong>X</strong></td>
      <td><strong>X</strong></td>
      <td>-</td>
    </tr>
    <tr>
      <td><strong>A4:</strong> Liquidar 10 mensualidades (Descuento 2 meses)</td>
      <td><strong>X</strong></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td><strong>A5:</strong> Recargo = $0.00</td>
      <td>-</td>
      <td><strong>X</strong></td>
      <td><strong>X</strong></td>
      <td><strong>X</strong></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td><strong>A6:</strong> Recargo proporcional = mensualidad &times; (días &times; 0.5%)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td><strong>X</strong></td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td><strong>A7:</strong> Recargo topado = mensualidad &times; 15.0%</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td><strong>X</strong></td>
      <td>-</td>
    </tr>
    <tr>
      <td><strong>A8:</strong> Lanzar <code>IllegalArgumentException</code></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td><strong>X</strong></td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<h3>4.4 Análisis de Caja Blanca: Grafo de Flujo, McCabe y Caminos Básicos en Java</h3>
<p>
Se selecciona el método real <code>calcularRecargoPorMora</code> implementado en <code>CalculadoraMensualidad.java</code>:
</p>

<pre><code class="language-java">// Código fuente real en CalculadoraMensualidad.java
1:  public BigDecimal calcularRecargoPorMora(BigDecimal mensualidad, int diasMora) {
2:      validarMensualidad(mensualidad); // Contiene: if (mensualidad == null || mensualidad.signum() <= 0)
3:      if (diasMora < 0) {
4:          throw new IllegalArgumentException("Los días de mora no pueden ser negativos");
5:      }
6:      BigDecimal tasa = TASA_RECARGO_DIARIA.multiply(BigDecimal.valueOf(diasMora));
7:      if (tasa.compareTo(TOPE_RECARGO) > 0) {
8:          tasa = TOPE_RECARGO;
9:      }
10:     return mensualidad.multiply(tasa).setScale(2, RoundingMode.HALF_UP);
11: }</code></pre>

<h4>Grafo de Flujo de Control (Control Flow Graph - CFG)</h4>
<p>Integrando la validación de entrada y las decisiones del método, se formalizan los nodos y aristas:</p>
<pre>
       ( Nodo 1: Entrada e invocación de validarMensualidad )
                                 |
                                 v
          { Rombo 2: ¿mensualidad == null || mensualidad <= 0? }
                         /               \
                  [SI]  /                 \  [NO]
                       v                   v
     ( Nodo 3: throw Excepción )    { Rombo 4: ¿diasMora < 0? }
                                            /           \
                                     [SI]  /             \  [NO]
                                          v               v
                        ( Nodo 5: throw Excepción )  ( Nodo 6: Calcular tasa = días * 0.005 )
                                                                 |
                                                                 v
                                                     { Rombo 7: ¿tasa > 0.15? }
                                                             /          \
                                                      [SI]  /            \  [NO]
                                                           v              v
                                             ( Nodo 8: tasa = 0.15 )      |
                                                           \              /
                                                            \            /
                                                             v          v
                                                   ( Nodo 9: return mensualidad * tasa )
                                                                 |
                                                                 v
                                                          ( Nodo 10: Fin )
</pre>

<h4>Cálculo de la Complejidad Ciclomática de McCabe ($V(G)$)</h4>
<p>Se verifica la métrica mediante los tres métodos equivalentes de McCabe:</p>
<ol>
  <li><strong>Método de Aristas y Nodos:</strong><br>
    Número de nodos $N = 10$, Número de aristas dirigidas $E = 12$, Componentes conexas $P = 1$.<br>
    $$V(G) = E - N + 2P = 12 - 10 + 2(1) = 4$$
  </li>
  <li><strong>Método de Nodos Predicado:</strong><br>
    Identificamos 3 nodos de decisión o predicado condicional (Nodos 2, 4 y 7):<br>
    $$V(G) = \text{Predicados} + 1 = 3 + 1 = 4$$
  </li>
  <li><strong>Método de Regiones Planas:</strong><br>
    El grafo delimita exactamente 3 regiones internas cerradas y 1 región exterior abierta:<br>
    $$V(G) = R_1 + R_2 + R_3 + R_{\text{externa}} = 4$$
  </li>
</ol>
<div class="callout">
  <strong>Conclusión Matemática:</strong> La complejidad ciclomática es <strong>$V(G) = 4$</strong>. En consecuencia, existen exactamente <strong>4 caminos linealmente independientes</strong> en el conjunto base necesarios y suficientes para garantizar una cobertura del 100% de sentencias y ramas.
</div>

<h4>Conjunto Base de Caminos Linealmente Independientes y Casos de Prueba</h4>
<table>
  <thead>
    <tr>
      <th style="width: 15%;">Camino Base</th>
      <th style="width: 25%;">Secuencia de Nodos en el Grafo</th>
      <th style="width: 35%;">Datos de Entrada del Caso de Prueba</th>
      <th style="width: 25%;">Resultado Esperado</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Camino 1</strong></td>
      <td>$1 \rightarrow 2 \rightarrow 3$ (Fin Excepción)</td>
      <td><code>mensualidad = null</code> o <code>BigDecimal("-50000")</code>, <code>diasMora = 5</code></td>
      <td>Lanza <code>IllegalArgumentException</code>: "La mensualidad debe ser mayor que cero".</td>
    </tr>
    <tr>
      <td><strong>Camino 2</strong></td>
      <td>$1 \rightarrow 2 \rightarrow 4 \rightarrow 5$ (Fin Excepción)</td>
      <td><code>mensualidad = BigDecimal("100000")</code>, <code>diasMora = -1</code></td>
      <td>Lanza <code>IllegalArgumentException</code>: "Los días de mora no pueden ser negativos".</td>
    </tr>
    <tr>
      <td><strong>Camino 3</strong></td>
      <td>$1 \rightarrow 2 \rightarrow 4 \rightarrow 6 \rightarrow 7 \rightarrow 9 \rightarrow 10$</td>
      <td><code>mensualidad = BigDecimal("100000")</code>, <code>diasMora = 10</code> (tasa = 0.05 &le; 0.15)</td>
      <td>Retorna <code>BigDecimal("5000.00")</code> (Cálculo proporcional sin activar tope).</td>
    </tr>
    <tr>
      <td><strong>Camino 4</strong></td>
      <td>$1 \rightarrow 2 \rightarrow 4 \rightarrow 6 \rightarrow 7 \rightarrow 8 \rightarrow 9 \rightarrow 10$</td>
      <td><code>mensualidad = BigDecimal("100000")</code>, <code>diasMora = 40</code> (tasa = 0.20 &gt; 0.15)</td>
      <td>Retorna <code>BigDecimal("15000.00")</code> (Aplica congelamiento en tope del 15%).</td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<!-- ==================== SECCIÓN 5 ==================== -->
<h1>5. Etapa 2: Plan de Pruebas y Casos de Prueba</h1>

<h3>5.1 Investigación Teórica Formal (Citada en APA 7)</h3>
<p>
La planificación de pruebas constituye la piedra angular del aseguramiento de calidad en la ingeniería de software. Históricamente normada por el estándar <strong>IEEE 829-2008</strong> (<em>Standard for Software and System Test Documentation</em>) y evolucionada contemporáneamente en la norma internacional <strong>ISO/IEC/IEEE 29119-3:2021</strong>, la estructura de un plan de pruebas estandariza la comunicación formal entre desarrolladores, analistas de pruebas y partes interesadas (Black et al., 2012).
</p>
<p>
Según ISO/IEC/IEEE 29119-3 (2021), un plan de pruebas integral debe contemplar obligatoriamente: (1) Identificador único y trazabilidad documental, (2) Alcance del proyecto distinguiendo taxativamente las características que serán probadas de aquellas excluidas de prueba, (3) Enfoque estratégico por niveles (unitarias, integración, sistema, aceptación), (4) Criterios rigurosos de entrada, suspensión, reanudación y salida (criterios de aprobación), (5) Entregables técnicos, (6) Requisitos ambientales y de infraestructura, (7) Asignación de recursos y matriz de responsabilidades, (8) Cronograma de ejecución, y (9) Gestión proactiva de riesgos técnicos y operacionales.
</p>
<p>
De manera sinérgica, la <strong>Matriz de Trazabilidad de Requisitos (Requirements Traceability Matrix - RTM)</strong> es un artefacto de ingeniería bidireccional que correlaciona de extremo a extremo cada requisito funcional con sus correspondientes casos de prueba, niveles de verificación, defectos asociados y estado de ejecución (Pressman &amp; Maxim, 2020). La RTM previene la existencia de "requisitos huérfanos" (funcionalidades sin pruebas asociadas) y "pruebas huérfanas" (código de prueba sin justificación en requisitos), facilitando el análisis de impacto ante solicitudes de cambio y garantizando que ningún criterio de calidad quede desatendido antes de la liberación a producción.
</p>

<h3>5.2 Plan de Pruebas Integral del Proyecto SGAP</h3>

<h4>1. Identificador del Documento y Control de Versiones</h4>
<ul>
  <li><strong>Código del Plan:</strong> <code>PLN-QA-SGAP-2026-V1</code></li>
  <li><strong>Versión:</strong> 1.0.0 (Release de Calidad Final)</li>
  <li><strong>Fecha de Emisión:</strong> 17 de Noviembre de 2026</li>
  <li><strong>Líderes de QA:</strong> Jhoan Sebastián Agudelo Mejía &amp; Juan Pablo Bedoya Payán</li>
</ul>

<h4>2. Introducción, Alcance y Objetivos de Calidad</h4>
<p>
El presente plan define la estrategia sistemática de verificación y validación para el software SGAP. El objetivo fundamental es garantizar el 100% de fiabilidad en los cómputos financieros (mitigación crítica del riesgo R4), exactitud en el cómputo de asistencias y rachas de deserción, y robustez total frente a entradas erróneas en la consola de comandos.
</p>

<h4>3. Elementos del Software Bajo Prueba</h4>
<ul>
  <li><code>co.edu.eam.sgap.CalculadoraMensualidad</code>: Métodos de recargo, total, pago anual y semáforo de cobro.</li>
  <li><code>co.edu.eam.sgap.asistencia.ControlAsistencia</code>: Estructura de almacenamiento, unicidad, corrección, cálculo porcentual, conteo de rachas y detección de alumnos en riesgo.</li>
  <li><code>co.edu.eam.sgap.AplicacionSGAP</code>: Capa de interacción y procesamiento de comandos de usuario.</li>
  <li><code>co.edu.eam.sgap.asistencia.RegistroAsistencia</code> y Enums: Inmutabilidad y tipado.</li>
</ul>

<h4>4. Características a Probar y Características Excluidas</h4>
<ul>
  <li><strong>Características a Probar:</strong> Registro sin duplicidad diaria; cómputo porcentual con ponderación de retardos y excusas; alerta por $\ge 3$ ausencias consecutivas; cálculo de recargo con tope del 15% usando <code>BigDecimal</code>; semáforo <code>AL_DIA</code>, <code>POR_VENCER</code>, <code>EN_MORA</code>; ordenamiento alfabético en listas de riesgo; integridad del comando de ayuda y robustez de parsing.</li>
  <li><strong>Características Excluidas de Prueba:</strong> Persistencia en bases de datos relacionales externas (en esta versión se opera en memoria según la especificación de arquitectura); interfaz gráfica de usuario web o móvil (el alcance actual está acotado estrictamente a interfaz de línea de comandos CLI).</li>
</ul>

<h4>5. Estrategia y Enfoque de Pruebas</h4>
<p>
Se implementa una estrategia híbrida piramidal. La base se sustenta en pruebas unitarias exhaustivas con JUnit 5 Jupiter, aplicando clases de equivalencia y análisis de valores límite (BVA). La capa intermedia integra la persistencia temporal en memoria con la lógica de negocio. La cúspide valida la consola interactiva y formaliza los Criterios de Aceptación bajo la sintaxis BDD (Dado-Cuando-Entonces).
</p>

<h4>6. Criterios de Entrada, Suspensión, Reanudación y Salida</h4>
<ul>
  <li><strong>Criterios de Entrada:</strong> Código fuente versionado en Git, compilación limpia sin errores con Maven (<code>./mvnw test-compile</code>), dependencias resueltas.</li>
  <li><strong>Criterios de Suspensión:</strong> Imposibilidad de compilación de clases centrales o tasa de fallos en pruebas de regresión superior al 25%.</li>
  <li><strong>Criterios de Reanudación:</strong> Corrección y verificación exitosa del defecto bloqueante mediante commit en Git.</li>
  <li><strong>Criterios de Salida (Aprobación):</strong> 100% de casos de prueba ejecutados y aprobados (<span class="badge-pass">PASS</span>), 0 fallos, 0 errores, y cobertura de ramas $\ge 90\%$ en la capa de negocio.</li>
</ul>

<h4>7. Entregables de la Campaña de Pruebas</h4>
<p>
(1) Plan de Aseguramiento de Calidad y Pruebas en PDF (<code>ISII_Grupo1_Entregable.pdf</code>), (2) Repositorio Git con suite automatizada de 92 pruebas en JUnit 5, (3) Reportes de ejecución de Maven Surefire en <code>target/surefire-reports</code>, (4) Manual de compilación y ejecución <code>README.md</code>, y (5) Video de sustentación técnica en YouTube/Drive.
</p>

<h4>8. Recursos, Ambiente de Pruebas, Roles y Responsabilidades</h4>
<ul>
  <li><strong>Hardware y SO:</strong> Linux Ubuntu x86_64, OpenJDK 17 LTS, Apache Maven 3.10, JUnit 5.10.2.</li>
  <li><strong>Jhoan Sebastián Agudelo Mejía:</strong> Líder de Arquitectura de Pruebas, diseño de pruebas unitarias financieras (<code>CalculadoraMensualidadTest</code>), mitigación R4 y grafo de flujo de caja blanca.</li>
  <li><strong>Juan Pablo Bedoya Payán:</strong> Líder de Automatización y Trazabilidad, diseño de pruebas de asistencia (<code>ControlAsistenciaTest</code>), pruebas de integración y consola (<code>AplicacionSGAPTest</code>).</li>
</ul>

<h4>9. Cronograma de Aseguramiento de Calidad</h4>
<table>
  <thead>
    <tr><th>Fase / Hito</th><th>Actividad Principal</th><th>Responsable</th><th>Fechas</th></tr>
  </thead>
  <tbody>
    <tr><td>Fase 1: Preparación</td><td>Refinamiento de requisitos (RF-01 a RF-10), conjeturas y Maven</td><td>Ambos</td><td>11 a 12 Nov</td></tr>
    <tr><td>Fase 2: Diseño</td><td>Diseño de BVA, particiones, tablas de decisión y CFG McCabe</td><td>Jhoan Sebastián</td><td>13 a 14 Nov</td></tr>
    <tr><td>Fase 3: Automatización</td><td>Codificación de 92 pruebas JUnit 5 y parametrizadas</td><td>Juan Pablo</td><td>15 a 16 Nov</td></tr>
    <tr><td>Fase 4: Cierre y QA</td><td>Auditoría de ejecución Surefire, DoD, informe PDF y video</td><td>Ambos</td><td>17 a 18 Nov</td></tr>
  </tbody>
</table>

<h4>10. Gestión de Riesgos y Contingencias Técnicas</h4>
<ul>
  <li><strong>Riesgo R4 (Financiero):</strong> Pérdida de precisión monetaria. <em>Mitigación:</em> Uso irrestricto de <code>BigDecimal</code> con escala 2 y redondeo <code>HALF_UP</code>, validado en pruebas parametrizadas.</li>
  <li><strong>Riesgo R5 (Robustez):</strong> Caída del sistema por comandos inválidos. <em>Mitigación:</em> Pruebas negativas de robustez con inyección de cadenas malformadas en <code>AplicacionSGAPTest</code>.</li>
</ul>

<div class="page-break"></div>

<h3>5.3 Catálogo Exhaustivo de 16 Casos de Prueba Documentados (CP-01 a CP-16)</h3>

<table>
  <thead>
    <tr>
      <th style="width: 8%;">ID</th>
      <th style="width: 8%;">Req</th>
      <th style="width: 24%;">Nombre y Técnica</th>
      <th style="width: 25%;">Datos de Entrada y Precondición</th>
      <th style="width: 25%;">Resultado Esperado</th>
      <th style="width: 10%;">Estado</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>CP-01</strong></td>
      <td>RF-01</td>
      <td>Rechazo de asistencia duplicada el mismo día.<br><em>[Transición Estado]</em></td>
      <td>Alumno "Carlos", fecha 2026-11-01. Se registra PRESENTE y luego se intenta registrar TARDE.</td>
      <td>Lanza <code>IllegalStateException</code> y no altera el registro existente.</td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>CP-02</strong></td>
      <td>RF-02</td>
      <td>Porcentaje con presencia, retardo y justificación.<br><em>[Clases Equivalencia]</em></td>
      <td>Alumno "Ana": 1 PRESENTE, 1 TARDE, 1 JUSTIFICADO. Base = 2 clases evaluables.</td>
      <td>Retorna <code>100.0%</code>. Las justificaciones no penalizan el promedio.</td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>CP-03</strong></td>
      <td>RF-02</td>
      <td>Porcentaje adicionando inasistencia injustificada.<br><em>[Cálculo Ponderado]</em></td>
      <td>Sobre "Ana" de CP-02, se adiciona 1 AUSENTE. Asistidas = 2, Base = 3.</td>
      <td>Retorna <code>66.67%</code> exacto con redondeo a 2 decimales.</td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>CP-04</strong></td>
      <td>RF-03</td>
      <td>Evaluación de racha en 2 ausencias seguidas.<br><em>[Valor Límite BVA]</em></td>
      <td>Alumno "Pedro": Faltas el 2026-11-01 y 2026-11-02. Consulta de alerta.</td>
      <td>Retorna <code>requiereAlertaAcudiente = false</code>.</td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>CP-05</strong></td>
      <td>RF-03</td>
      <td>Activación de alerta en 3 ausencias seguidas.<br><em>[Valor Límite BVA]</em></td>
      <td>Sobre "Pedro", se añade falta el 2026-11-03. Racha consecutiva = 3.</td>
      <td>Retorna <code>requiereAlertaAcudiente = true</code> (Frontera exacta).</td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>CP-06</strong></td>
      <td>RF-04</td>
      <td>Recargo por mora con 0 días de retraso.<br><em>[Valor Límite BVA]</em></td>
      <td>Mensualidad $100.000, <code>diasMora = 0</code>.</td>
      <td>Retorna <code>BigDecimal("0.00")</code>.</td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>CP-07</strong></td>
      <td>RF-04</td>
      <td>Recargo proporcional con 10 días de mora.<br><em>[Cálculo Proporcional]</em></td>
      <td>Mensualidad $100.000, <code>diasMora = 10</code>. Tasa = 5.0%.</td>
      <td>Retorna <code>BigDecimal("5000.00")</code>.</td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>CP-08</strong></td>
      <td>RF-04</td>
      <td>Recargo en frontera exacta de tope (Día 30).<br><em>[Valor Límite BVA]</em></td>
      <td>Mensualidad $100.000, <code>diasMora = 30</code>. Tasa = 15.0%.</td>
      <td>Retorna <code>BigDecimal("15000.00")</code> (Tope alcanzado).</td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>CP-09</strong></td>
      <td>RF-04</td>
      <td>Congelamiento en tope con 40 días de mora.<br><em>[Valor Límite BVA]</em></td>
      <td>Mensualidad $100.000, <code>diasMora = 40</code>. Tasa calculada = 20%.</td>
      <td>Retorna <code>BigDecimal("15000.00")</code> (Tope respetado).</td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>CP-10</strong></td>
      <td>RF-04</td>
      <td>Rechazo de días de mora negativos.<br><em>[Caja Blanca Camino 2]</em></td>
      <td>Mensualidad $100.000, <code>diasMora = -5</code>.</td>
      <td>Lanza <code>IllegalArgumentException</code> con mensaje específico.</td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>CP-11</strong></td>
      <td>RF-05</td>
      <td>Semáforo a 4 días del vencimiento.<br><em>[Valor Límite BVA]</em></td>
      <td>Vencimiento 2026-11-10, Fecha actual 2026-11-06.</td>
      <td>Retorna <code>EstadoPago.AL_DIA</code>.</td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>CP-12</strong></td>
      <td>RF-05</td>
      <td>Semáforo en ventana de 3 días previos.<br><em>[Valor Límite BVA]</em></td>
      <td>Vencimiento 2026-11-10, Fecha actual 2026-11-07.</td>
      <td>Retorna <code>EstadoPago.POR_VENCER</code>.</td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>CP-13</strong></td>
      <td>RF-05</td>
      <td>Semáforo el mismo día del vencimiento.<br><em>[Valor Límite BVA]</em></td>
      <td>Vencimiento 2026-11-10, Fecha actual 2026-11-10.</td>
      <td>Retorna <code>EstadoPago.POR_VENCER</code> (Día límite).</td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>CP-14</strong></td>
      <td>RF-05</td>
      <td>Semáforo posterior al vencimiento.<br><em>[Valor Límite BVA]</em></td>
      <td>Vencimiento 2026-11-10, Fecha actual 2026-11-11.</td>
      <td>Retorna <code>EstadoPago.EN_MORA</code>.</td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>CP-15</strong></td>
      <td>RF-07</td>
      <td>Reporte alfabético de estudiantes en riesgo.<br><em>[Caja Negra Partición]</em></td>
      <td>Alumnos "Zulma" (50%), "Alberto" (75%), "Carlos" (90%).</td>
      <td>Retorna <code>["Alberto", "Zulma"]</code> ordenados alfabéticamente.</td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>CP-16</strong></td>
      <td>RF-08</td>
      <td>Liquidación anual con descuento pronto pago.<br><em>[Equivalencia Funcional]</em></td>
      <td>Mensualidad ordinaria de $120.000.</td>
      <td>Retorna <code>BigDecimal("1200000.00")</code> (10 meses).</td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<h3>5.4 Matriz de Trazabilidad de Requisitos (RTM)</h3>
<p>
La matriz asegura que cada uno de los 10 Requisitos Funcionales cuente con cobertura formal por nivel de prueba, clase responsable y verificación ejecutada:
</p>

<table>
  <thead>
    <tr>
      <th style="width: 10%;">Requisito</th>
      <th style="width: 25%;">Descripción Funcional</th>
      <th style="width: 20%;">Casos de Prueba Asociados</th>
      <th style="width: 15%;">Nivel de Prueba</th>
      <th style="width: 18%;">Clase de Prueba JUnit</th>
      <th style="width: 12%;">Estado</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>RF-01</strong></td>
      <td>Unicidad de asistencia diaria</td>
      <td>CP-01, CA-01, tests unitarios</td>
      <td>Integración / BDD</td>
      <td><code>ControlAsistenciaTest</code></td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>RF-02</strong></td>
      <td>Porcentaje ponderado y excusas</td>
      <td>CP-02, CP-03, CA-02, CA-03</td>
      <td>Integración / BDD</td>
      <td><code>ControlAsistenciaTest</code></td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>RF-03</strong></td>
      <td>Alerta por ausencias seguidas (&ge;3)</td>
      <td>CP-04, CP-05, CA-04</td>
      <td>Integración / BDD</td>
      <td><code>ControlAsistenciaTest</code></td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>RF-04</strong></td>
      <td>Recargo mora y tope 15% (BigDecimal)</td>
      <td>CP-06, CP-07, CP-08, CP-09, CP-10, CA-07</td>
      <td>Unitaria / BDD</td>
      <td><code>CalculadoraMensualidadTest</code></td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>RF-05</strong></td>
      <td>Semáforo de cobro y ventana 3 días</td>
      <td>CP-11, CP-12, CP-13, CP-14, CA-09</td>
      <td>Unitaria / BDD</td>
      <td><code>CalculadoraMensualidadTest</code></td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>RF-06</strong></td>
      <td>Corrección de asistencia previa</td>
      <td>Tests corrección en suite</td>
      <td>Integración</td>
      <td><code>ControlAsistenciaTest</code></td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>RF-07</strong></td>
      <td>Alumnos en riesgo alfabético (&lt;80%)</td>
      <td>CP-15, CA-05, tests de riesgo</td>
      <td>Integración / BDD</td>
      <td><code>ControlAsistenciaTest</code></td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>RF-08</strong></td>
      <td>Pago anual con descuento 10 meses</td>
      <td>CP-16, CA-08</td>
      <td>Unitaria / BDD</td>
      <td><code>CalculadoraMensualidadTest</code></td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>RF-09</strong></td>
      <td>Aforo y conteo de asistentes por fecha</td>
      <td>CA-06, tests conteo fecha</td>
      <td>Integración / BDD</td>
      <td><code>ControlAsistenciaTest</code></td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
    <tr>
      <td><strong>RF-10</strong></td>
      <td>Robustez defensiva de consola CLI</td>
      <td>14 tests de comandos y parseo</td>
      <td>Sistema (E2E)</td>
      <td><code>AplicacionSGAPTest</code></td>
      <td><span class="badge-pass">APROBADO</span></td>
    </tr>
  </tbody>
</table>

<h3>5.5 Registro Real de Defectos Encontrados y Corregidos (Bug Tracking Log)</h3>

<table>
  <thead>
    <tr>
      <th style="width: 10%;">ID Defecto</th>
      <th style="width: 10%;">Severidad</th>
      <th style="width: 25%;">Descripción y Causa Raíz</th>
      <th style="width: 35%;">Pasos para Reproducir y Evidencia</th>
      <th style="width: 10%;">Estado</th>
      <th style="width: 10%;">Solución</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>BUG-01</strong></td>
      <td><span class="badge-fail">CRÍTICA</span></td>
      <td>Imprecisión decimal en punto flotante IEEE 754 si se usa <code>double</code> en mensualidades financieras.</td>
      <td>Calcular <code>100000.0 * 0.005 * 3</code> arrojando <code>1500.0000000000002</code> en lugar de valor monetario cerrado.</td>
      <td><span class="badge-pass">CERRADO</span></td>
      <td>Migración integral a <code>BigDecimal</code> con escala 2 y redondeo <code>HALF_UP</code>.</td>
    </tr>
    <tr>
      <td><strong>BUG-02</strong></td>
      <td><span class="badge-fail">ALTA</span></td>
      <td>Riesgo de operador relacional estricto en tope de mora (superar el 15.0% antes de congelar).</td>
      <td>Verificar días 30 y 31. Si se compara <code>&gt;=</code> o se omite cota, el día 30 cobra de más o no congela.</td>
      <td><span class="badge-pass">CERRADO</span></td>
      <td>Validación explícita <code>tasa.compareTo(TOPE_RECARGO) &gt; 0</code> forzando <code>tasa = TOPE_RECARGO</code>.</td>
    </tr>
    <tr>
      <td><strong>BUG-03</strong></td>
      <td><span class="badge-fail">MEDIA</span></td>
      <td>Caída de la aplicación por <code>NullPointerException</code> ante cadenas vacías o espacios en consola.</td>
      <td>Ingresar comando <code>registrar  ;2026-11-01;PRESENTE</code> o nombre compuesto de solo espacios.</td>
      <td><span class="badge-pass">CERRADO</span></td>
      <td>Implementación de <code>validarNombre</code> aplicando <code>trim()</code> y validando <code>isBlank()</code> defensivo.</td>
    </tr>
    <tr>
      <td><strong>BUG-04</strong></td>
      <td><span class="badge-fail">ALTA</span></td>
      <td>Desorden cronológico en el cálculo de rachas continuas de inasistencia al registrar fechas desordenadas.</td>
      <td>Registrar asistencias en fechas desordenadas (día 4, día 1, día 3, día 2). El bucle lineal leía en orden de inserción.</td>
      <td><span class="badge-pass">CERRADO</span></td>
      <td>Ordenamiento previo mediante Stream <code>sorted(Comparator.comparing(RegistroAsistencia::fecha))</code> en <code>registrosDe()</code>.</td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<!-- ==================== SECCIÓN 6 ==================== -->
<h1>6. Etapa 3: Automatización de Pruebas</h1>

<h3>6.1 Investigación Teórica Formal (Citada en APA 7)</h3>
<p>
La automatización de pruebas representa una disciplina fundamental para viabilizar la integración y entrega continua (CI/CD). No obstante, la ingeniería de software moderna enfatiza que no todas las pruebas deben ser automatizadas. Según la <strong>Pirámide de Pruebas</strong> formulada por Mike Cohn (2009), la arquitectura de pruebas debe distribuir sus esfuerzos piramidalmente: una amplia base de pruebas unitarias automatizadas (rápidas, aisladas y de bajo costo de mantenimiento), una capa intermedia de pruebas de integración y servicios, y una cúspide reducida de pruebas de interfaz de usuario de extremo a extremo.
</p>
<p>
El criterio técnico para determinar <em>qué automatizar</em> depende de factores como la repetitividad, la criticidad financiera y la estabilidad del componente: se automatizan invariablemente las pruebas de regresión, los cálculos matemáticos críticos, las validaciones de límites algorítmicos y las pruebas de humo en tuberías de construcción (Vocke, 2018). Por el contrario, <em>qué mantener manual</em> abarca las pruebas exploratorias, la evaluación ergonómica y subjetiva de la experiencia de usuario (UX), y la validación de interfaces altamente volátiles donde el costo de actualización del script automatizado supera el retorno de inversión (ROI) del aseguramiento de calidad (Fewster &amp; Graham, 1999).
</p>
<p>
En el ecosistema Java, <strong>JUnit 5</strong> (Jupiter) se ha consolidado como el estándar de facto, desacoplando su motor de ejecución (Platform) de su modelo de programación (Jupiter API). JUnit 5 introduce anotaciones semánticas de ciclo de vida como <code>@Test</code>, <code>@BeforeEach</code>, <code>@AfterEach</code> y <code>@Nested</code> para agrupamiento jerárquico (JUnit 5 User Guide, 2024). Asimismo, potencia la cobertura exhaustiva mediante <strong>Pruebas Parametrizadas (<code>@ParameterizedTest</code>)</strong> alimentadas por fuentes declarativas como <code>@ValueSource</code>, <code>@CsvSource</code> y <code>@MethodSource</code>, permitiendo someter un único método de prueba a decenas de vectores de entrada sin duplicar código.
</p>
<p>
La ejecución orquestada de estas suites se delega a herramientas de construcción de software como <strong>Apache Maven</strong> (mediante el plugin <code>maven-surefire-plugin</code>) o Gradle. Dichas herramientas gestionan el ciclo de vida del proyecto, garantizando compilaciones reproducibles, ejecución automatizada en modo headless durante la fase <code>test</code> y generación estandarizada de reportes XML/HTML auditables en servidores de integración continua (Hunt, 2021).
</p>

<h3>6.2 Aplicación Práctica: Suite de 92 Pruebas en el Repositorio</h3>
<p>
El repositorio oficial del proyecto SGAP contiene una suite profesional compuesta por <strong>92 casos de prueba automatizados</strong> estructurados bajo JUnit Jupiter 5.10.2:
</p>
<ul>
  <li><code>co.edu.eam.sgap.CalculadoraMensualidadTest (33 tests):</code> Pruebas unitarias agrupadas mediante <code>@Nested</code>. Implementa pruebas parametrizadas con <code>@CsvSource</code> para recargos proporcionales, evaluación exhaustiva de fronteras de mora (días 0, 1, 29, 30, 31, 40), pago anual y estados de vencimiento.</li>
  <li><code>co.edu.eam.sgap.asistencia.ControlAsistenciaTest (36 tests):</code> Pruebas integradas de asistencia evaluando unicidad, correcciones, conteos, cómputo porcentual con excusas médicas, detección de rachas con ordenamiento cronológico y listas de riesgo ordenadas.</li>
  <li><code>co.edu.eam.sgap.AplicacionSGAPTest (14 tests):</code> Pruebas de integración sobre la consola CLI, verificando el procesamiento de los 10 comandos y el control defensivo de excepciones por datos malformados.</li>
  <li><code>co.edu.eam.sgap.CriteriosAceptacionSGAPTest (9 tests):</code> Suite BDD orientada a las partes interesadas que comprueba punto por punto los 9 criterios de aceptación del negocio.</li>
</ul>

<h4>Muestra Representativa de Automatización: Valores Límite e Integración Real</h4>
<pre><code class="language-java">// Fragmento de CalculadoraMensualidadTest.java: Valores Límite con JUnit 5 Parametrizado
@ParameterizedTest(name = "Mora {0} dias en mensualidad $100.000 -> Recargo esperado: ${1}")
@CsvSource({
    "0,   0.00",    // Limite inferior (sin mora)
    "1,   500.00",  // Primer dia de mora lineal
    "29,  14500.00",// Inmediatamente antes del tope
    "30,  15000.00",// Frontera exacta de tope (15%)
    "31,  15000.00",// Superacion de tope: congelado en 15%
    "40,  15000.00" // Caso extremo: se mantiene congelado
})
@DisplayName("Verificacion rigurosa de frontera en el tope de mora del 15%")
void verificarFronteraTopeMora(int dias, String recargoEsperado) {
    BigDecimal res = calc.calcularRecargoPorMora(new BigDecimal("100000"), dias);
    assertEquals(new BigDecimal(recargoEsperado), res);
}

// Fragmento de ControlAsistenciaTest.java: Prueba de Integracion entre Clases Reales
@Test
@DisplayName("Integracion: Registro, correccion y deduccion de justificados en base")
void pruebaIntegracionRegistroYCalculoConExcusas() {
    LocalDate fecha = LocalDate.of(2026, 11, 1);
    control.registrarAsistencia("Ana", fecha, EstadoAsistencia.AUSENTE);
    // Correccion posterior con soporte medico
    control.corregirAsistencia("Ana", fecha, EstadoAsistencia.JUSTIFICADO);
    // La clase justificada se excluye del divisor: porcentaje debe dar 0.0% limpiamente
    assertEquals(0.0, control.calcularPorcentajeAsistencia("Ana"));
}</code></pre>

<div class="page-break"></div>

<h3>6.3 Informe Técnico Oficial de Ejecución de JUnit 5 Surefire</h3>
<p>
A continuación se transcribe la salida oficial obtenida al ejecutar la suite automatizada con el wrapper de Maven (<code>./mvnw test -o</code>):
</p>

<pre><code>[INFO] Scanning for projects...
[INFO] ------------------< co.edu.eam.sgap:sgap-aceptacion >-------------------
[INFO] Building SGAP - Sistema de Gestion de Asistencia y Pagos 1.0.0
[INFO] --------------------------------[ jar ]---------------------------------
[INFO] --- compiler:3.11.0:testCompile (default-testCompile) @ sgap-aceptacion ---
[INFO] Nothing to compile - all classes are up to date
[INFO] --- surefire:3.1.2:test (default-test) @ sgap-aceptacion ---
[INFO] Using auto detected provider org.apache.maven.surefire.junitplatform.JUnitPlatformProvider
[INFO] 
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running co.edu.eam.sgap.CriteriosAceptacionSGAPTest
[INFO] Tests run: 9, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.124 s -- in co.edu.eam.sgap.CriteriosAceptacionSGAPTest
[INFO] Running co.edu.eam.sgap.CalculadoraMensualidadTest
[INFO] Running co.edu.eam.sgap.CalculadoraMensualidadTest$EstadoPagoTests
[INFO] Tests run: 9, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.111 s
[INFO] Running co.edu.eam.sgap.CalculadoraMensualidadTest$PagoAnualTests
[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.010 s
[INFO] Running co.edu.eam.sgap.CalculadoraMensualidadTest$TotalAPagarTests
[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.009 s
[INFO] Running co.edu.eam.sgap.CalculadoraMensualidadTest$RecargoPorMoraTests
[INFO] Tests run: 18, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.116 s
[INFO] Running co.edu.eam.sgap.AplicacionSGAPTest
[INFO] Tests run: 14, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.084 s -- in co.edu.eam.sgap.AplicacionSGAPTest
[INFO] Running co.edu.eam.sgap.asistencia.ControlAsistenciaTest
[INFO] Tests run: 36, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.191 s -- in co.edu.eam.sgap.asistencia.ControlAsistenciaTest
[INFO] 
[INFO] Results:
[INFO] 
[INFO] Tests run: 92, Failures: 0, Errors: 0, Skipped: 0
[INFO] 
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  3.825 s
[INFO] Finished at: 2026-11-17T21:16:33-05:00
[INFO] ------------------------------------------------------------------------</code></pre>

<div class="callout">
  <strong>Balance de Ejecución:</strong> Se ejecutaron exitosamente <strong>92 casos de prueba automatizados</strong>, con una tasa de fallos del <strong>0.0%</strong> (0 Fallures, 0 Errors, 0 Skipped) en un tiempo total de 3.825 segundos, confirmando el cumplimiento pleno de los criterios de salida del plan de pruebas.
</div>

<h3>6.4 Justificación de Pruebas que Quedaron Manuales</h3>
<p>
En estricta concordancia con la teoría de pruebas basada en valor, se determinó mantener bajo modalidad manual las siguientes verificaciones:
</p>
<ol>
  <li><strong>Ergonomía visual y legibilidad en terminal de consola:</strong> Evaluar si los saltos de línea del comando <code>ayuda</code> y la visualización de los caracteres especiales se perciben de forma clara y cómoda para el usuario en diferentes resoluciones y terminales (Bash, PowerShell, CMD).</li>
  <li><strong>Pruebas exploratorias de interacción humana (Ad-hoc Testing):</strong> Simular la digitación desordenada, rápida o accidental de operadores no técnicos en situaciones de atención al público, observando la capacidad de la consola para mantener el bucle de interacción sin desorientar al operario.</li>
  <li><strong>Validación subjetiva de aceptación con el usuario final:</strong> Sesión interactiva con el directivo de la academia para corroborar que el formato de salida de las alertas y la semaforización satisfacen su flujo real de trabajo administrativo antes de su despliegue definitivo.</li>
</ol>

<div class="page-break"></div>

<!-- ==================== SECCIÓN 7 ==================== -->
<h1>7. Etapa 4: Calidad del Software</h1>

<h3>7.1 Investigación Teórica Formal (Citada en APA 7)</h3>
<p>
El aseguramiento de la calidad de software trasciende la mera ejecución de pruebas funcionales para abarcar atributos intrínsecos de la arquitectura del producto y la madurez de los procesos de desarrollo. El estándar internacional <strong>ISO/IEC 25010:2011</strong> (perteneciente a la familia SQuaRE — <em>Software Product Quality Requirements and Evaluation</em>), y su revisión ISO/IEC 25010:2023, formaliza un modelo de calidad del producto compuesto por ocho características cardinales: Adecuación Funcional, Rendimiento/Eficiencia, Compatibilidad, Usabilidad, Fiabilidad, Seguridad, Mantenibilidad y Portabilidad, cada una descompuesta en subcaracterísticas medibles (ISO/IEC, 2011, 2023).
</p>
<p>
En el ámbito organizacional y de procesos, el modelo <strong>CMMI v2.0 (Capability Maturity Model Integration)</strong> propone un marco escalonado de evaluación que clasifica a las organizaciones de desarrollo en cinco niveles de madurez evolutiva: (1) <em>Inicial:</em> procesos ad-hoc, caóticos e impredecibles dependientes del heroísmo individual; (2) <em>Gestionado:</em> proyectos planificados, ejecutados, medidos y controlados a nivel de equipo; (3) <em>Definido:</em> procesos estandarizados a nivel organizacional con directrices y procedimientos institucionalizados; (4) <em>Cuantitativamente Gestionado:</em> control estadístico y métricas predictivas de calidad; y (5) <em>Optimizado:</em> mejora continua e innovación sistemática basada en el análisis cuantitativo de causas comunes de variación (CMMI Institute, 2018).
</p>
<p>
Por su parte, en marcos de trabajo ágiles como <strong>Scrum</strong>, la calidad no es una fase tardía sino una responsabilidad compartida de todo el Equipo Scrum durante cada Sprint (Schwaber &amp; Sutherland, 2020). La calidad se materializa mediante la <strong>Definición de Terminado (Definition of Done - DoD)</strong>: un acuerdo formal y riguroso de condiciones técnicas y funcionales que todo Incremento de producto debe satisfacer obligatoriamente antes de considerarse entregable. La DoD actúa como una barrera de control que previene la acumulación de <em>deuda técnica</em> y garantiza la liberación continua de software potencialmente desplegable con alta fiabilidad (Kniberg, 2015).
</p>

<h3>7.2 Selección y Justificación Técnica de 3 Características ISO/IEC 25010</h3>

<h4>1. Adecuación Funcional (Functional Suitability)</h4>
<p>
Grado en que el software satisface las necesidades declaradas e implícitas bajo condiciones especificadas.
</p>
<ul>
  <li><em>Completitud Funcional:</em> SGAP implementa la totalidad de los 10 requisitos funcionales (control de asistencia, moras, alertas, descuentos y reportería).</li>
  <li><em>Corrección Funcional:</em> Exactitud absoluta en los cómputos numéricos. Se implementó <code>BigDecimal</code> con escala 2 y <code>RoundingMode.HALF_UP</code>, eliminando las discrepancias de centavos del estándar binario IEEE 754 y garantizando liquidaciones monetarias justas.</li>
  <li><em>Pertinencia Funcional:</em> Las funciones implementadas resuelven con precisión el problema diario de deserción y cobro en academias formativas.</li>
</ul>

<h4>2. Fiabilidad (Reliability)</h4>
<p>
Capacidad del sistema de mantener un nivel especificado de rendimiento bajo condiciones establecidas.
</p>
<ul>
  <li><em>Madurez:</em> La aplicación demostró 0 fallos en 92 pruebas automatizadas continuas ejecutadas en Maven.</li>
  <li><em>Tolerancia a Fallos:</em> Diseño defensivo ante entradas anómalas. <code>ControlAsistencia</code> y <code>CalculadoraMensualidad</code> interceptan argumentos nulos, números negativos o formatos corruptos arrojando excepciones descriptivas que son controladas amigablemente en consola, previniendo caídas imprevistas (crash).</li>
  <li><em>Recuperabilidad:</em> Al encapsular el estado y operar en memoria con Java Records inmutables, cualquier fallo en un comando no corrompe los registros previamente almacenados.</li>
</ul>

<h4>3. Mantenibilidad (Maintainability)</h4>
<p>
Facilidad con que el software puede ser modificado, corregido o adaptado a nuevos requisitos.
</p>
<ul>
  <li><em>Modularidad:</em> Alta cohesión y bajo acoplamiento. La lógica financiera (<code>CalculadoraMensualidad</code>) está completamente desacoplada de la asistencia (<code>ControlAsistencia</code>) y de la interfaz de consola (<code>AplicacionSGAP</code>).</li>
  <li><em>Reusabilidad:</em> Los componentes centrales pueden integrarse a futuro en una API REST (Spring Boot) o interfaz web sin modificar una sola línea de lógica de negocio.</li>
  <li><em>Capacidad de ser Probado (Testability):</em> Arquitectura diseñada para pruebas. Métodos sin efectos secundarios que facilitan aserciones directas y suites parametrizadas en JUnit 5 con 100% de cobertura de ramas en el dominio.</li>
</ul>

<div class="page-break"></div>

<h3>7.3 Autoevaluación Honesta en CMMI y Plan de Evolución hacia Nivel 3</h3>

<h4>Ubicación Honesta: Nivel 2 de Madurez (Gestionado / Managed)</h4>
<p>
Al evaluar objetivamente las prácticas de ingeniería desplegadas durante el ciclo de vida de SGAP, el equipo se ubica de forma transparente en el <strong>Nivel 2 de Madurez (Gestionado)</strong>.
</p>
<p><strong>Evidencias empíricas que sustentan el Nivel 2:</strong></p>
<ul>
  <li><em>Planificación y Estimación:</em> Se definió un plan de pruebas formal (identificador, alcance, criterios y recursos).</li>
  <li><em>Aseguramiento de Calidad de Procesos y Productos:</em> Se diseñaron matrices de trazabilidad (RTM) y se verificaron los 10 requisitos funcionales mediante 92 casos de prueba automatizados.</li>
  <li><em>Gestión de Configuración:</em> Control estricto de versiones con Git, estructura estándar de proyectos con Apache Maven y registro de defectos identificados (Bug Tracker).</li>
  <li><em>Monitoreo y Control:</em> Auditoría continua mediante reportes automáticos de Maven Surefire en cada ciclo de prueba.</li>
</ul>
<p>
<em>¿Por qué no Nivel 3 aún?</em> Porque los estándares y procedimientos actuales fueron gestionados y adoptados a nivel de este proyecto específico por el equipo, pero aún no están institucionalizados como una norma organizacional transversal con repositorio de activos de procesos común a toda la institución.
</p>

<h4>Plan de Acción Específico para Ascender al Nivel 3 (Definido / Defined)</h4>
<ol>
  <li><strong>Estandarización y Formalización de Procesos Organizacionales:</strong> Documentar las guías de diseño de pruebas (BVA, tablas de decisión, caminos básicos) como activos de proceso reutilizables en cualquier nuevo proyecto de la facultad o empresa.</li>
  <li><strong>Implementación de Tubería de Integración Continua (CI/CD):</strong> Configurar flujos de trabajo automatizados en GitHub Actions para compilar, ejecutar la suite de JUnit 5 Surefire y analizar estáticamente el código (SonarQube) ante cada pull request.</li>
  <li><strong>Formalización de Métricas Organizacionales de Calidad:</strong> Establecer umbrales institucionales obligatorios de cobertura de ramas (mínimo 90%) y deuda técnica máxima permitida antes de autorizar liberaciones.</li>
  <li><strong>Programa de Capacitación y Gestión del Conocimiento:</strong> Difundir las lecciones aprendidas y plantillas de aseguramiento de calidad al resto de equipos de desarrollo de la organización.</li>
</ol>

<h3>7.4 Definición de Terminado (Definition of Done - DoD) para SGAP</h3>
<p>
Para garantizar que todo incremento de funcionalidad en SGAP posea calidad de producción antes de ser aceptado en el Sprint, se establecen las siguientes <strong>7 condiciones obligatorias y verificables</strong>:
</p>
<div class="callout">
  <ol>
    <li><strong>Código Fuente Limpio y Documentado:</strong> El código cumple con las convenciones oficiales de estilo de Java (Google Java Style / Oracle), sin variables huérfanas, con nombres semánticos claros y documentación Javadoc en métodos públicos.</li>
    <li><strong>Compilación Exitosa en Maven:</strong> La solución compila de forma reproducible con Apache Maven (<code>./mvnw clean compile</code>) arrojando 0 advertencias críticas y 0 errores.</li>
    <li><strong>100% de Pruebas Verdes en JUnit 5:</strong> La suite de pruebas unitarias y de integración se ejecuta en Surefire (<code>./mvnw test</code>) con 100% de aprobación (<span class="badge-pass">PASS</span>), reportando 0 fallos, 0 errores y 0 pruebas omitidas.</li>
    <li><strong>Cobertura Mínima de Ramas:</strong> La cobertura de ramas condicionales (Branch Coverage) en las clases de lógica de negocio es igual o superior al <strong>90.0%</strong> medido con herramientas de cobertura (JaCoCo).</li>
    <li><strong>Criterios de Aceptación BDD Validados:</strong> Todos los escenarios asociados en formato Dado-Cuando-Entonces (Given-When-Then) pasan satisfactoriamente en la suite de aceptación.</li>
    <li><strong>Revisión Cruzada de Código por Pares (Peer Code Review):</strong> Ningún commit ingresa a la rama principal (<code>main</code>) sin la aprobación formal del compañero de equipo tras inspeccionar robustez, ausencia de números mágicos y manejo de excepciones.</li>
    <li><strong>Documentación y Trazabilidad Actualizadas:</strong> La Matriz de Trazabilidad (RTM) y el archivo <code>README.md</code> reflejan las instrucciones exactas de uso de la nueva funcionalidad sin dejar ambigüedades operativas.</li>
  </ol>
</div>

<div class="page-break"></div>

<!-- ==================== SECCIÓN 8 ==================== -->
<h1>8. Conclusiones y Lecciones Aprendidas</h1>
<p>
El desarrollo del Plan de Aseguramiento de Calidad de Software para el sistema SGAP constituyó una experiencia formativa integral que permitió contrastar la teoría formal de pruebas con la aplicación práctica en un proyecto real en Java 17 LTS. Entre las principales conclusiones y aprendizajes destacan:
</p>
<ul>
  <li><strong>El valor insustituible del Análisis de Valores Límite:</strong> Confirmamos experimentalmente que la inmensa mayoría de defectos en sistemas informáticos se concentran en las fronteras de decisión condicional (como se demostró en el experimento de edad con el operador estricto vs. inclusivo y en la frontera del tope de mora al día 30). Las pruebas basadas en valores arbitrarios intermedios generan una falsa sensación de seguridad.</li>
  <li><strong>La criticidad de la seguridad de tipos numéricos en software financiero:</strong> La experiencia de blindar el cálculo monetario mediante <code>BigDecimal</code> y <code>RoundingMode.HALF_UP</code> ratificó que en ingeniería de software jamás deben emplearse tipos flotantes binarios primitivos (<code>double</code>, <code>float</code>) para transacciones contables, mitigando contingencias legales y económicas para las instituciones.</li>
  <li><strong>La potencia de la automatización declarativa con JUnit 5:</strong> La utilización de pruebas parametrizadas (<code>@ParameterizedTest</code> con <code>@CsvSource</code>) multiplicó la cobertura de pruebas minimizando drásticamente la duplicidad de código en el repositorio, permitiendo evaluar 92 escenarios en menos de 4 segundos.</li>
  <li><strong>El aseguramiento de calidad como cultura de proceso:</strong> Aprendimos que la calidad no es una actividad que se agrega al final del desarrollo ("probar al final"), sino un proceso transversal y disciplinado que inicia desde el refinamiento de requisitos, pasa por el diseño de caja blanca (McCabe), y se consolida con una estricta <em>Definition of Done</em> (DoD).</li>
</ul>

<h1>9. Matriz de Aportes y Dedicación por Integrante</h1>
<table>
  <thead>
    <tr>
      <th style="width: 25%;">Integrante</th>
      <th style="width: 15%;">Dedicación (%)</th>
      <th style="width: 20%;">Rol Principal en el Proyecto</th>
      <th style="width: 40%;">Tareas y Componentes Desarrollados</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Jhoan Sebastián Agudelo Mejía</strong></td>
      <td>50%</td>
      <td>Líder de Calidad y Pruebas Unitarias</td>
      <td>Diseño de técnicas de caja blanca (CFG, Complejidad Ciclomática de McCabe y caminos básicos); investigación y aplicación de Valores Límite en el cálculo financiero (RF-04); implementación de pruebas parametrizadas en <code>CalculadoraMensualidadTest</code>; redacción de análisis de riesgos financieros y normas ISO/IEC 25010; edición y estructuración del entregable PDF.</td>
    </tr>
    <tr>
      <td><strong>Juan Pablo Bedoya Payán</strong></td>
      <td>50%</td>
      <td>Líder de Automatización e Integración</td>
      <td>Estandarización de Apache Maven (<code>pom.xml</code> y Surefire); diseño e implementación de pruebas de integración para el módulo de control de asistencia (<code>ControlAsistenciaTest</code>); pruebas de sistema para comandos de consola (<code>AplicacionSGAPTest</code>); formulación de la Matriz de Trazabilidad (RTM); definición de la DoD y sustentación de niveles CMMI.</td>
    </tr>
  </tbody>
</table>

<h1>10. Declaración Ética de Uso de Herramientas de IA</h1>
<p>
En cumplimiento de las directrices académicas de transparencia e integridad institucional:
</p>
<div class="callout-info">
  <p>
    Los autores declaramos que se emplearon herramientas de Inteligencia Artificial (específicamente modelos de lenguaje avanzados como Gemini) como <strong>asistentes técnicos de soporte</strong> durante el desarrollo del proyecto, con los siguientes propósitos puntuales: (1) apoyo en la estructuración preliminar de sintaxis Markdown y plantillas HTML/CSS para maquetación, (2) revisión ortográfica y gramatical de la redacción técnica, y (3) generación de esquemas base para tablas comparativas.
  </p>
  <p>
    <strong>Responsabilidad y Juicio Crítico Humano:</strong> Todos los requisitos funcionales, el código fuente en Java 17 LTS, la formulación matemática de los grafos de McCabe, los 92 casos de prueba automatizados en JUnit 5, las aserciones de valores límite y los análisis de calidad fueron verificados, ejecutados, auditados y validados íntegramente por los integrantes <strong>Jhoan Sebastián Agudelo Mejía</strong> y <strong>Juan Pablo Bedoya Payán</strong>. Asumimos plena responsabilidad intelectual, técnica y ética sobre los resultados presentados en este documento.
  </p>
</div>

<div class="page-break"></div>

<!-- ==================== REFERENCIAS APA 7 ==================== -->
<h1>11. Referencias Bibliográficas (Normas APA 7.ª Edición)</h1>

<div class="reference-item">
  Beust, C., &amp; Suleiman, H. (2020). <em>Next Generation Java Testing: TestNG and Advanced Concepts</em>. Addison-Wesley Professional.
</div>

<div class="reference-item">
  Black, R., van Veenendaal, E., &amp; Graham, D. (2012). <em>Foundations of Software Testing: ISTQB Certification</em> (3rd ed.). Cengage Learning.
</div>

<div class="reference-item">
  CMMI Institute. (2018). <em>CMMI for Development, Version 2.0: Improving performance for developing better products and services</em>. Information Science Institute.
</div>

<div class="reference-item">
  Cohn, M. (2009). <em>Succeeding with Agile: Software Development Using Scrum</em>. Addison-Wesley Professional.
</div>

<div class="reference-item">
  Copeland, L. (2004). <em>A Practitioner's Guide to Software Test Design</em>. Artech House Publishers.
</div>

<div class="reference-item">
  Fewster, M., &amp; Graham, D. (1999). <em>Software Test Automation: Effective Use of Test Execution Tools</em>. ACM Press / Addison-Wesley.
</div>

<div class="reference-item">
  Hunt, J. (2021). <em>Advanced Guide to Apache Maven and JUnit 5</em>. Springer Nature. https://doi.org/10.1007/978-3-030-74567-8
</div>

<div class="reference-item">
  IEEE Computer Society. (2008). <em>IEEE Standard for Software and System Test Documentation</em> (IEEE Std 829-2008). IEEE. https://doi.org/10.1109/IEEESTD.2008.4578383
</div>

<div class="reference-item">
  ISO/IEC. (2011). <em>Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models</em> (ISO/IEC 25010:2011). International Organization for Standardization.
</div>

<div class="reference-item">
  ISO/IEC. (2023). <em>Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model</em> (ISO/IEC 25010:2023). International Organization for Standardization.
</div>

<div class="reference-item">
  ISO/IEC/IEEE. (2021). <em>Software and systems engineering — Software testing — Part 3: Test documentation</em> (ISO/IEC/IEEE 29119-3:2021). IEEE. https://doi.org/10.1109/IEEESTD.2021.9602419
</div>

<div class="reference-item">
  ISO/IEC/IEEE. (2021). <em>Software and systems engineering — Software testing — Part 4: Test techniques</em> (ISO/IEC/IEEE 29119-4:2021). IEEE. https://doi.org/10.1109/IEEESTD.2021.9602420
</div>

<div class="reference-item">
  JUnit 5 User Guide. (2024). <em>JUnit 5: The new major version of the programmer-friendly testing framework for Java and the JVM</em>. JUnit Team. https://junit.org/junit5/docs/current/user-guide/
</div>

<div class="reference-item">
  Kniberg, H. (2015). <em>Scrum and XP from the Trenches: How we do Scrum</em> (2nd ed.). Crisp Publishing.
</div>

<div class="reference-item">
  McCabe, T. J. (1976). A complexity measure. <em>IEEE Transactions on Software Engineering</em>, SE-2(4), 308–320. https://doi.org/10.1109/TSE.1976.233837
</div>

<div class="reference-item">
  Myers, G. J., Badgett, T., &amp; Sandler, C. (2011). <em>The Art of Software Testing</em> (3rd ed.). John Wiley &amp; Sons.
</div>

<div class="reference-item">
  Pressman, R. S., &amp; Maxim, B. R. (2020). <em>Software Engineering: A Practitioner's Approach</em> (9th ed.). McGraw-Hill Education.
</div>

<div class="reference-item">
  Schwaber, K., &amp; Sutherland, J. (2020). <em>The Scrum Guide: The Definitive Guide to Scrum: The Rules of the Game</em>. Scrum.org.
</div>

<div class="reference-item">
  Sommerville, I. (2016). <em>Software Engineering</em> (10th ed.). Pearson Education.
</div>

<div class="reference-item">
  Vocke, M. (2018). <em>The Practical Test Pyramid</em>. MartinFowler.com. https://martinfowler.com/articles/practical-test-pyramid.html
</div>

<div class="page-break"></div>

<!-- ==================== ANEXO A ==================== -->
<h1>Anexo A: Guion Oficial para el Video de Sustentación (15 Minutos)</h1>
<p>
A continuación se presenta el guion técnico y la distribución cronológica segundo a segundo para la grabación del video de sustentación de <strong>Jhoan Sebastián Agudelo Mejía</strong> y <strong>Juan Pablo Bedoya Payán</strong>.
</p>

<h3>Reglas de Oro Obligatorias para la Grabación del Video</h3>
<div class="callout-warning">
  <ul>
    <li><strong>Duración estricta:</strong> Entre 7 y 15 minutos (tiempo óptimo planificado: 14 minutos).</li>
    <li><strong>Presencia en cámara:</strong> Ambos integrantes <strong>deben aparecer en cámara a medio cuerpo</strong> y hablar obligatoriamente (50% del tiempo cada uno). Si uno no aparece o no habla, no recibe nota de video.</li>
    <li><strong>Demostración técnica en vivo:</strong> Es obligatorio compartir pantalla y ejecutar en vivo la terminal con Maven (<code>./mvnw test</code>) mostrando los 92 tests verdes y una pequeña sesión interactiva de la aplicación.</li>
    <li><strong>Plataforma de entrega:</strong> Subir el video a Google Drive (compartido con permisos de lectura para el docente) o a YouTube en modo <strong>Oculto (Unlisted)</strong>. Probar el enlace en modo incógnito antes de enviarlo.</li>
  </ul>
</div>

<h3>Cronograma Minuto a Minuto del Video</h3>
<table>
  <thead>
    <tr>
      <th style="width: 15%;">Minutos</th>
      <th style="width: 25%;">Responsable en Habla</th>
      <th style="width: 30%;">Sección y Tema</th>
      <th style="width: 30%;">Apoyo Visual en Pantalla</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>0:00 – 1:30</strong></td>
      <td><strong>Jhoan Sebastián</strong></td>
      <td>Presentación del equipo, docente David Cano Baquero y contexto del proyecto SGAP.</td>
      <td>Cámara activa + Portada del documento PDF.</td>
    </tr>
    <tr>
      <td><strong>1:30 – 3:30</strong></td>
      <td><strong>Juan Pablo</strong></td>
      <td>Estructuración en Maven, refinamiento de requisitos (RF-01 a RF-10) y arquitectura Java 17.</td>
      <td>Estructura de carpetas en IDE / Terminal y archivo <code>pom.xml</code>.</td>
    </tr>
    <tr>
      <td><strong>3:30 – 5:30</strong></td>
      <td><strong>Jhoan Sebastián</strong></td>
      <td>Métodos de prueba: Valores límite en mora, mitigación R4 con BigDecimal y grafo de caja blanca (McCabe).</td>
      <td>Código de <code>CalculadoraMensualidad.java</code> y diagrama de grafo de flujo CFG.</td>
    </tr>
    <tr>
      <td><strong>5:30 – 7:30</strong></td>
      <td><strong>Juan Pablo</strong></td>
      <td>Plan de pruebas, matriz de trazabilidad (RTM) y registro real de defectos (Bug Tracking).</td>
      <td>Tabla de 16 Casos de Prueba, RTM y Bug Log en el documento.</td>
    </tr>
    <tr>
      <td><strong>7:30 – 10:30</strong></td>
      <td><strong>Ambos (Jhoan &amp; Juan Pablo)</strong></td>
      <td><strong>Demostración en vivo (Live Demo):</strong> Ejecución de Maven Surefire (92 tests) y uso de consola SGAP.</td>
      <td>Terminal en vivo: ejecución de <code>./mvnw test</code> y comandos de <code>AplicacionSGAP</code>.</td>
    </tr>
    <tr>
      <td><strong>10:30 – 12:30</strong></td>
      <td><strong>Juan Pablo</strong></td>
      <td>Calidad de software: ISO/IEC 25010, autoevaluación CMMI Nivel 2 y Definition of Done (DoD).</td>
      <td>Sección de calidad del informe: 3 características y las 7 condiciones de la DoD.</td>
    </tr>
    <tr>
      <td><strong>12:30 – 14:00</strong></td>
      <td><strong>Jhoan Sebastián &amp; Juan Pablo</strong></td>
      <td>Conclusiones, lecciones aprendidas, dictamen final de aprobación y cierre formal.</td>
      <td>Cámara activa de ambos a medio cuerpo.</td>
    </tr>
  </tbody>
</table>

</body>
</html>
"""

# Guardar el archivo HTML temporal
html_path = "/home/sebastian/Documentos/Pruebas_ingnieria/sgap-aceptacion/Documento_Entregable_Final.html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML generado exitosamente en: {html_path}")

# Compilar a PDF usando LibreOffice headless
pdf_output_dir = "/home/sebastian/Documentos/Pruebas_ingnieria/sgap-aceptacion"
pdf_target_name = "ISII_Grupo1_Entregable.pdf"
pdf_alt_name = "ISII_Grupo_Entregable.pdf"

cmd = [
    "libreoffice",
    "-env:UserInstallation=file:///tmp/libreoffice_user",
    "--headless",
    "--convert-to", "pdf",
    html_path,
    "--outdir", pdf_output_dir
]

print("Compilando PDF con LibreOffice...")
proc = subprocess.run(cmd, capture_output=True, text=True)
print("Salida:", proc.stdout)
if proc.stderr:
    print("Stderr:", proc.stderr)

# Renombrar al nombre obligatorio especificado por el docente
src_pdf = os.path.join(pdf_output_dir, "Documento_Entregable_Final.pdf")
dest_pdf1 = os.path.join(pdf_output_dir, pdf_target_name)
dest_pdf2 = os.path.join(pdf_output_dir, pdf_alt_name)

if os.path.exists(src_pdf):
    import shutil
    shutil.copyfile(src_pdf, dest_pdf1)
    shutil.copyfile(src_pdf, dest_pdf2)
    print(f"PDF generado y copiado como: {dest_pdf1} y {dest_pdf2}")
else:
    print("Error: No se encontró el archivo PDF generado.")

