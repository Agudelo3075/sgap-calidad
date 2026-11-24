#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de la Presentación de Diapositivas para la Sustentación de SGAP
Institución Universitaria EAM - Ingeniería de Software II (ISII)
Autores: Jhoan Sebastián Agudelo Mejía (240420242064) & Juan Pablo Bedoya Payán (240420242060)
Docente: Mg. David Cano Baquero
"""

import os
import subprocess

html_presentation = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sustentación SGAP — Aseguramiento de Calidad y Pruebas</title>
<style>
  @page {
    size: 297mm 210mm; /* A4 Horizontal 16:9 ratio */
    margin: 10mm;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Liberation Sans', 'DejaVu Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    background-color: #0f172a;
    color: #1e293b;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
  }

  /* Contenedor del Slide */
  .slide-container {
    width: 100vw;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    padding: 20px;
  }

  .slide {
    width: 95vw;
    max-width: 1300px;
    height: 90vh;
    max-height: 750px;
    background: #ffffff;
    border-radius: 12px;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    display: none;
    flex-direction: column;
    padding: 40px 55px;
    position: relative;
    overflow: hidden;
  }

  .slide.active {
    display: flex;
  }

  /* Encabezado del Slide */
  .slide-header {
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 12px;
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }

  .slide-badge {
    font-size: 11pt;
    font-weight: 700;
    color: #2563eb;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 4px;
  }

  .slide-title {
    font-size: 24pt;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.15;
  }

  .slide-speaker {
    background-color: #eff6ff;
    color: #1e40af;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 10pt;
    font-weight: 600;
    border: 1px solid #bfdbfe;
  }

  /* Contenido del Slide */
  .slide-content {
    flex: 1;
    display: flex;
    gap: 30px;
    align-items: stretch;
    justify-content: center;
  }

  .col-1 { flex: 1; }
  .col-2 { flex: 1; display: flex; flex-direction: column; gap: 15px; }

  /* Tarjetas y bloques */
  .card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 16px 20px;
    border-left: 4px solid #1e3a8a;
  }

  .card-title {
    font-size: 12pt;
    font-weight: 700;
    color: #1e3a8a;
    margin-bottom: 6px;
  }

  .card-text {
    font-size: 10pt;
    color: #475569;
    line-height: 1.45;
  }

  .card-alert {
    border-left-color: #e11d48;
    background: #fff1f2;
  }
  .card-alert .card-title { color: #9f1239; }

  .card-success {
    border-left-color: #16a34a;
    background: #f0fdf4;
  }
  .card-success .card-title { color: #166534; }

  /* Tablas y listas */
  ul {
    padding-left: 20px;
    font-size: 10.5pt;
    color: #334155;
    line-height: 1.5;
  }

  li {
    margin-bottom: 6px;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 9.5pt;
    margin-top: 5px;
  }

  th, td {
    border: 1px solid #cbd5e1;
    padding: 6px 10px;
    text-align: left;
  }

  th {
    background-color: #1e3a8a;
    color: #ffffff;
    font-weight: 600;
    font-size: 9pt;
  }

  tr:nth-child(even) { background-color: #f1f5f9; }

  code {
    background: #f1f5f9;
    color: #b91c1c;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'DejaVu Sans Mono', monospace;
    font-size: 9.5pt;
  }

  /* Pie de slide */
  .slide-footer {
    border-top: 1px solid #e2e8f0;
    padding-top: 10px;
    margin-top: 15px;
    display: flex;
    justify-content: space-between;
    font-size: 9pt;
    color: #94a3b8;
  }

  /* Navegación */
  .nav-controls {
    position: fixed;
    bottom: 20px;
    display: flex;
    gap: 15px;
    align-items: center;
    background: rgba(15, 23, 42, 0.85);
    padding: 8px 18px;
    border-radius: 30px;
    backdrop-filter: blur(8px);
    z-index: 100;
  }

  .nav-btn {
    background: #2563eb;
    color: white;
    border: none;
    padding: 6px 14px;
    border-radius: 20px;
    cursor: pointer;
    font-weight: bold;
    font-size: 10pt;
    transition: 0.2s;
  }

  .nav-btn:hover { background: #1d4ed8; }

  .slide-counter {
    color: white;
    font-size: 10pt;
    font-weight: 600;
    min-width: 60px;
    text-align: center;
  }

  /* Portada Especial */
  .cover-slide {
    text-align: center;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
    color: #ffffff;
  }

  .cover-slide h1 {
    font-size: 30pt;
    font-weight: 800;
    margin-bottom: 12px;
    color: #ffffff;
    line-height: 1.15;
    text-transform: uppercase;
  }

  .cover-slide h2 {
    font-size: 16pt;
    color: #93c5fd;
    font-weight: 600;
    margin-bottom: 30px;
  }

  .cover-box {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 20px 35px;
    border-radius: 12px;
    display: inline-block;
    text-align: left;
    backdrop-filter: blur(5px);
  }

  .cover-box p {
    font-size: 11pt;
    line-height: 1.6;
    color: #e2e8f0;
  }

  .cover-box strong {
    color: #ffffff;
  }

  /* Modo impresión / PDF */
  @media print {
    body {
      background: none;
      display: block;
    }
    .slide-container {
      display: block;
      width: 100%;
      height: auto;
      padding: 0;
    }
    .slide {
      display: flex !important;
      width: 100%;
      height: 195mm;
      max-height: 195mm;
      page-break-after: always;
      box-shadow: none;
      border: 1px solid #cbd5e1;
      margin-bottom: 20mm;
    }
    .nav-controls { display: none; }
  }
</style>
</head>
<body>

<div class="slide-container">

  <!-- ==================== SLIDE 1: PORTADA ==================== -->
  <div class="slide cover-slide active" id="slide-1">
    <div style="font-size: 13pt; letter-spacing: 2px; color: #60a5fa; text-transform: uppercase; font-weight: 700; margin-bottom: 15px;">
      Institución Universitaria EAM — Facultad de Ingeniería
    </div>
    <h1>Plan de Aseguramiento de Calidad de Software (SQA)</h1>
    <h2>Proyecto SGAP — Sistema de Gestión de Asistencia y Pagos</h2>

    <div class="cover-box">
      <p><strong>Asignatura:</strong> Ingeniería de Software II (ISII) — Pruebas y Calidad de Software</p>
      <p><strong>Docente Evaluador:</strong> Mg. David Cano Baquero</p>
      <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.2); margin: 10px 0;">
      <p><strong>Expositores / Desarrolladores:</strong></p>
      <p>• <strong>Jhoan Sebastián Agudelo Mejía</strong> — Cód. Estudiantil: <code>240420242064</code></p>
      <p>• <strong>Juan Pablo Bedoya Payán</strong> — Cód. Estudiantil: <code>240420242060</code></p>
      <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.2); margin: 10px 0;">
      <p><strong>Entorno Técnico:</strong> Java 17 LTS | JUnit 5.10.2 | Apache Maven 3.10 | Surefire 3.1.2</p>
    </div>
  </div>

  <!-- ==================== SLIDE 2: CONTEXTO Y PROBLEMÁTICA ==================== -->
  <div class="slide" id="slide-2">
    <div class="slide-header">
      <div>
        <div class="slide-badge">Contexto Operativo del Software</div>
        <div class="slide-title">1. Problemática en Academias Formativas</div>
      </div>
      <div class="slide-speaker">Voz: Jhoan Sebastián</div>
    </div>
    <div class="slide-content">
      <div class="col-1">
        <div class="card card-alert" style="margin-bottom: 15px;">
          <div class="card-title">⚠️ La Crisis de la Gestión en Papel y Excel</div>
          <div class="card-text">
            Las escuelas deportivas (fútbol, natación, artes marciales) y conservatorios musicales operan artesanalmente, provocando pérdidas financieras y deserciones masivas no atendidas a tiempo.
          </div>
        </div>
        <div class="card" style="margin-bottom: 15px;">
          <div class="card-title">📉 Deserción Silenciosa (Riesgo R1)</div>
          <div class="card-text">
            Los estudiantes acumulan inasistencias consecutivas y la administración solo se entera semanas después cuando el acudiente formaliza el retiro. Ya es tarde para intervenir.
          </div>
        </div>
        <div class="card">
          <div class="card-title">💸 Cobros Conflictivos y Arbitrarios (Riesgo R4)</div>
          <div class="card-text">
            Liquidaciones de mora sin soporte legal ni topes máximos que generan disputas constantes con acudientes por recargos desmedidos.
          </div>
        </div>
      </div>
      <div class="col-2">
        <div class="card card-success">
          <div class="card-title">🎯 Misión y Solución Aportada por SGAP</div>
          <div class="card-text">
            Unificar en un motor desacoplado de alta fiabilidad:
            <ul style="margin-top: 8px;">
              <li><strong>Control de Asistencia:</strong> 4 estados (<code>PRESENTE</code>, <code>TARDE</code>, <code>AUSENTE</code>, <code>JUSTIFICADO</code>).</li>
              <li><strong>Alerta Temprana:</strong> Disparo automático ante $\ge 3$ ausencias seguidas.</li>
              <li><strong>Justicia en Excusas:</strong> Deducción de justificaciones de la base evaluable.</li>
              <li><strong>Blindaje Financiero:</strong> Mora diaria al 0.5% con tope estricto del 15% mediante <code>BigDecimal</code>.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <span>Plan de Calidad SGAP — ISII EAM</span>
      <span>Diapositiva 2 / 10</span>
    </div>
  </div>

  <!-- ==================== SLIDE 3: ARQUITECTURA Y REQUISITOS ==================== -->
  <div class="slide" id="slide-3">
    <div class="slide-header">
      <div>
        <div class="slide-badge">Estandarización y Alcance</div>
        <div class="slide-title">2. Arquitectura Maven y 10 Requisitos Refinados</div>
      </div>
      <div class="slide-speaker">Voz: Juan Pablo</div>
    </div>
    <div class="slide-content">
      <div class="col-1">
        <div class="card" style="margin-bottom: 12px;">
          <div class="card-title">🏗️ Decisiones de Arquitectura Técnica</div>
          <div class="card-text">
            • <strong>Estandarización Apache Maven:</strong> Convención <code>src/main/java</code> y <code>src/test/java</code> con JUnit 5 Jupiter y Surefire 3.1.2.<br>
            • <strong>Inmutabilidad con Java Records:</strong> <code>RegistroAsistencia</code> previene efectos colaterales y mutación accidental en memoria.<br>
            • <strong>Desacoplamiento:</strong> Lógica de negocio (<code>ControlAsistencia</code> y <code>CalculadoraMensualidad</code>) independiente de la consola.
          </div>
        </div>
        <div class="card card-success">
          <div class="card-title">📋 Eliminación de Ambigüedades en Requisitos</div>
          <div class="card-text">
            Se ampliaron los 5 requisitos iniciales a <strong>10 Requisitos Funcionales (RF-01 al RF-10)</strong> rigurosamente verificables.
          </div>
        </div>
      </div>
      <div class="col-2">
        <table>
          <thead>
            <tr><th>Req</th><th>Nombre</th><th>Regla de Negocio Crítica</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>RF-01</strong></td><td>Unicidad Asistencia</td><td>Rechazo de duplicados en la misma fecha con <code>IllegalStateException</code>.</td></tr>
            <tr><td><strong>RF-02</strong></td><td>Porcentaje Ponderado</td><td>Llegadas TARDE suman a favor; JUSTIFICADO se excluye del divisor base.</td></tr>
            <tr><td><strong>RF-03</strong></td><td>Alerta Ausencias</td><td>Disparo al acudiente si acumula $\ge 3$ ausencias seguidas en orden cronológico.</td></tr>
            <tr><td><strong>RF-04</strong></td><td>Mora y Tope 15%</td><td>0.5% diario congelado estrictamente al alcanzar el 15.0% (<code>BigDecimal</code>).</td></tr>
            <tr><td><strong>RF-05</strong></td><td>Semáforo Cartera</td><td>Ventana 3 días: <code>AL_DIA</code> (&gt;3d), <code>POR_VENCER</code> (0-3d), <code>EN_MORA</code>.</td></tr>
            <tr><td><strong>RF-06..10</strong></td><td>Complementarios</td><td>Corrección de asistencia, alumnos en riesgo (&lt;80%), pago anual y CLI robusta.</td></tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="slide-footer">
      <span>Plan de Calidad SGAP — ISII EAM</span>
      <span>Diapositiva 3 / 10</span>
    </div>
  </div>

  <!-- ==================== SLIDE 4: RESULTADOS GUÍA ANTERIOR ==================== -->
  <div class="slide" id="slide-4">
    <div class="slide-header">
      <div>
        <div class="slide-badge">Punto de Partida Obligatorio</div>
        <div class="slide-title">3. Resultados Completos de la Guía Anterior</div>
      </div>
      <div class="slide-speaker">Voz: Juan Pablo</div>
    </div>
    <div class="slide-content">
      <div class="col-1">
        <div class="card" style="margin-bottom: 12px;">
          <div class="card-title">🔬 Experimento de Límites de Edad (18 a 120 años)</div>
          <div class="card-text">
            • <code>CP-01 (edad 25):</code> Esperado=true | Obtenido=true &rarr; <strong style="color:green">APROBÓ</strong><br>
            • <code>CP-02 (edad 18):</code> Esperado=true | Obtenido=false &rarr; <strong style="color:red">FALLÓ</strong><br>
            • <code>CP-03 (edad 17):</code> Esperado=false | Obtenido=false &rarr; <strong style="color:green">APROBÓ</strong><br>
            <em>Lección:</em> El código tenía <code>edad > 18</code> en vez de <code>>= 18</code>. Los valores intermedios ocultan los defectos; los valores límite los revelan.
          </div>
        </div>
        <div class="card card-alert">
          <div class="card-title">⚖️ Verificación vs. Validación</div>
          <div class="card-text">
            Si el software cumple toda la especificación pero no resuelve la necesidad del cliente, <strong>falló la VALIDACIÓN</strong> (construir el producto correcto).
          </div>
        </div>
      </div>
      <div class="col-2">
        <div class="card">
          <div class="card-title">🧩 Matriz de Error, Defecto y Fallo en SGAP</div>
          <div class="card-text">
            • <strong>Error (Mental):</strong> Creer que la mora crece indefinidamente o que la alerta es con más de 3 faltas.<br>
            • <strong>Defecto (Código):</strong> Omitir el tope del 15% o escribir <code>racha > 3</code>.<br>
            • <strong>Fallo (Ejecución):</strong> Cobrar $20.000 en vez de $15.000, o no avisar al acudiente perdiendo al alumno.
          </div>
        </div>
        <div class="card card-success">
          <div class="card-title">🤝 Simulación de Aceptación con el Cliente</div>
          <div class="card-text">
            Aprobación formal de CA-01 (justificaciones médicas neutrales), CA-02 (alerta preventiva en 3 ausencias) y CA-03 (tope de mora respetado).
          </div>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <span>Plan de Calidad SGAP — ISII EAM</span>
      <span>Diapositiva 4 / 10</span>
    </div>
  </div>

  <!-- ==================== SLIDE 5: CAJA NEGRA Y RIESGO R4 ==================== -->
  <div class="slide" id="slide-5">
    <div class="slide-header">
      <div>
        <div class="slide-badge">Etapa 1: Métodos de Prueba</div>
        <div class="slide-title">4. Caja Negra: BVA, Mitigación R4 y Tablas de Decisión</div>
      </div>
      <div class="slide-speaker">Voz: Jhoan Sebastián</div>
    </div>
    <div class="slide-content">
      <div class="col-1">
        <div class="card card-alert" style="margin-bottom: 15px;">
          <div class="card-title">💣 La Trampa del IEEE 754 y la Mitigación del Riesgo R4</div>
          <div class="card-text">
            En Java, <code>double</code> y <code>float</code> son binarios: no representan exactamente fracciones como <code>0.005</code>, produciendo residuos como <code>1500.0000000000002</code>.<br>
            <strong>Solución SGAP:</strong> Se blindó el cálculo usando <code>java.math.BigDecimal</code> con escala 2 y redondeo bancario formal <code>RoundingMode.HALF_UP</code>.
          </div>
        </div>
        <div class="card card-success">
          <div class="card-title">📊 Tabla de Decisión de Cartera</div>
          <div class="card-text">
            Mapeo formal de 5 condiciones booleanas (pago anual, vencimiento, ventana 3 días, tope mora) generando 8 acciones libres de contradicción.
          </div>
        </div>
      </div>
      <div class="col-2">
        <div class="card">
          <div class="card-title">🎯 Análisis de Valores Límite Riguroso (BVA en Mora)</div>
          <div class="card-text">Evaluando mensualidad base de $100.000:</div>
          <table>
            <thead>
              <tr><th>Días Mora</th><th>Tasa Aplicada</th><th>Monto Liquidado</th><th>Frontera Evaluada</th></tr>
            </thead>
            <tbody>
              <tr><td>0 días</td><td>0.0%</td><td>$0.00</td><td>Límite inferior sin mora</td></tr>
              <tr><td>1 día</td><td>0.5%</td><td>$500.00</td><td>Primer día de mora lineal</td></tr>
              <tr><td><strong>29 días</strong></td><td>14.5%</td><td>$14.500.00</td><td>Pre-frontera de tope</td></tr>
              <tr><td><strong>30 días</strong></td><td>15.0%</td><td>$15.000.00</td><td><strong>Frontera exacta de tope</strong></td></tr>
              <tr><td><strong>31 días</strong></td><td>15.0% (tope)</td><td>$15.000.00</td><td><strong>Post-frontera congelada</strong></td></tr>
              <tr><td>40 días</td><td>15.0% (tope)</td><td>$15.000.00</td><td>Comportamiento asintótico</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <span>Plan de Calidad SGAP — ISII EAM</span>
      <span>Diapositiva 5 / 10</span>
    </div>
  </div>

  <!-- ==================== SLIDE 6: CAJA BLANCA Y MCCABE ==================== -->
  <div class="slide" id="slide-6">
    <div class="slide-header">
      <div>
        <div class="slide-badge">Etapa 1: Métodos de Prueba</div>
        <div class="slide-title">5. Caja Blanca: Grafo de Flujo (CFG) y McCabe V(G)=4</div>
      </div>
      <div class="slide-speaker">Voz: Jhoan Sebastián</div>
    </div>
    <div class="slide-content">
      <div class="col-1">
        <div class="card" style="margin-bottom: 15px;">
          <div class="card-title">📐 Deducción Matemática de la Complejidad Ciclomática</div>
          <div class="card-text">
            Método real analizado: <code>calcularRecargoPorMora(mensualidad, diasMora)</code>.<br>
            Corroborado por tres métodos matemáticos independientes:
            <ul style="margin-top: 6px;">
              <li><strong>1. Aristas y Nodos:</strong> $V(G) = E - N + 2P = 12 - 10 + 2(1) = \mathbf{4}$</li>
              <li><strong>2. Nodos Predicado:</strong> $V(G) = P + 1 = 3 + 1 = \mathbf{4}$</li>
              <li><strong>3. Regiones Planas:</strong> 3 regiones cerradas + 1 abierta = $\mathbf{4}$</li>
            </ul>
          </div>
        </div>
        <div class="card card-success">
          <div class="card-title">✅ Cobertura Total Alcanzada</div>
          <div class="card-text">
            <strong>100% Cobertura de Sentencias</strong> y <strong>100% Cobertura de Ramas</strong> garantizado científicamente mediante los 4 caminos base.
          </div>
        </div>
      </div>
      <div class="col-2">
        <div class="card">
          <div class="card-title">🛣️ Conjunto Base de Caminos Independientes</div>
          <table>
            <thead>
              <tr><th>Camino</th><th>Ruta en el Grafo CFG</th><th>Dato de Prueba</th><th>Resultado</th></tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Camino 1</strong></td>
                <td>1 &rarr; 2 &rarr; 3 (Excepción)</td>
                <td><code>mensualidad = -50000</code></td>
                <td><code>IllegalArgumentException</code></td>
              </tr>
              <tr>
                <td><strong>Camino 2</strong></td>
                <td>1 &rarr; 2 &rarr; 4 &rarr; 5 (Excepción)</td>
                <td><code>diasMora = -1</code></td>
                <td><code>IllegalArgumentException</code></td>
              </tr>
              <tr>
                <td><strong>Camino 3</strong></td>
                <td>1 &rarr; 2 &rarr; 4 &rarr; 6 &rarr; 7 &rarr; 9</td>
                <td><code>diasMora = 10</code> (tasa 5%)</td>
                <td>Retorna $5000.00 (Proporcional)</td>
              </tr>
              <tr>
                <td><strong>Camino 4</strong></td>
                <td>1 &rarr; 2 &rarr; 4 &rarr; 6 &rarr; 7 &rarr; 8 &rarr; 9</td>
                <td><code>diasMora = 40</code> (tasa 20%)</td>
                <td>Retorna $15000.00 (Tope congelado)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <span>Plan de Calidad SGAP — ISII EAM</span>
      <span>Diapositiva 6 / 10</span>
    </div>
  </div>

  <!-- ==================== SLIDE 7: PLAN DE PRUEBAS Y DEFECTOS ==================== -->
  <div class="slide" id="slide-7">
    <div class="slide-header">
      <div>
        <div class="slide-badge">Etapa 2: Plan de Pruebas</div>
        <div class="slide-title">6. Plan ISO 29119-3, Matriz RTM y Bitácora de Bugs</div>
      </div>
      <div class="slide-speaker">Voz: Juan Pablo</div>
    </div>
    <div class="slide-content">
      <div class="col-1">
        <div class="card" style="margin-bottom: 12px;">
          <div class="card-title">📑 Plan de Pruebas Formal (ISO/IEC/IEEE 29119-3)</div>
          <div class="card-text">
            • <strong>Identificador:</strong> <code>PLN-QA-SGAP-2026-V1</code> (3 páginas en PDF).<br>
            • <strong>Exclusiones Justificadas:</strong> Se excluyen bases de datos relacionales externas (persistencia en memoria para no falsear pruebas unitarias).<br>
            • <strong>Criterio de Salida:</strong> 100% tests verdes sin fallos y cobertura de ramas $\ge 90\%$.
          </div>
        </div>
        <div class="card card-success">
          <div class="card-title">🔗 Matriz de Trazabilidad Bidireccional (RTM)</div>
          <div class="card-text">
            16 Casos de prueba documentados (CP-01 a CP-16) asociados a los 10 requisitos. Se evitaron tanto "requisitos huérfanos" como "pruebas huérfanas".
          </div>
        </div>
      </div>
      <div class="col-2">
        <div class="card">
          <div class="card-title">🐛 Bitácora de Defectos Reales Resueltos (Bug Tracker)</div>
          <table>
            <thead>
              <tr><th>ID</th><th>Severidad</th><th>Defecto Encontrado</th><th>Solución Aplicada</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>BUG-01</strong></td><td><span style="color:red">CRÍTICA</span></td><td>Imprecisión flotante IEEE 754 en cuotas.</td><td>Migración estricta a <code>BigDecimal</code>.</td></tr>
              <tr><td><strong>BUG-02</strong></td><td><span style="color:orange">ALTA</span></td><td>Operador de tope de mora permitía cobro &gt;15%.</td><td>Blindaje con <code>tasa.compareTo > 0</code>.</td></tr>
              <tr><td><strong>BUG-03</strong></td><td><span style="color:blue">MEDIA</span></td><td>Crash por espacios o nombres en blanco en CLI.</td><td>Validación defensiva <code>isBlank()</code> y <code>trim()</code>.</td></tr>
              <tr><td><strong>BUG-04</strong></td><td><span style="color:orange">ALTA</span></td><td>Fallo en rachas si las fechas entraban desordenadas.</td><td>Ordenamiento forzado en Stream por fecha.</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <span>Plan de Calidad SGAP — ISII EAM</span>
      <span>Diapositiva 7 / 10</span>
    </div>
  </div>

  <!-- ==================== SLIDE 8: AUTOMATIZACIÓN Y LIVE DEMO ==================== -->
  <div class="slide" id="slide-8">
    <div class="slide-header">
      <div>
        <div class="slide-badge">Etapa 3: Automatización</div>
        <div class="slide-title">7. Suite JUnit 5 (92 Tests) y Demostración en Vivo</div>
      </div>
      <div class="slide-speaker">Voz: Jhoan Sebastián & Juan Pablo</div>
    </div>
    <div class="slide-content">
      <div class="col-1">
        <div class="card card-success" style="margin-bottom: 15px;">
          <div class="card-title">⚡ Métricas de Ejecución Oficial Maven Surefire</div>
          <div class="card-text">
            • <code>CriteriosAceptacionSGAPTest:</code> 9 pruebas BDD.<br>
            • <code>CalculadoraMensualidadTest:</code> 33 pruebas unitarias y parametrizadas.<br>
            • <code>ControlAsistenciaTest:</code> 36 pruebas de lógica de asistencia.<br>
            • <code>AplicacionSGAPTest:</code> 14 pruebas de integración en consola.<br>
            <strong>TOTAL: 92 tests ejecutados en 3.8 segundos. 0 Fallos, 0 Errores.</strong>
          </div>
        </div>
        <div class="card">
          <div class="card-title">👁️ ¿Qué Pruebas se Mantuvieron Manuales?</div>
          <div class="card-text">
            Ergonomía visual de la consola CLI, pruebas exploratorias de interacción humana (Ad-hoc) y validación de aceptación subjetiva con directivos.
          </div>
        </div>
      </div>
      <div class="col-2">
        <div class="card card-alert" style="height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
          <div style="font-size: 38pt; margin-bottom: 10px;">💻</div>
          <div class="card-title" style="font-size: 16pt;">PASO A DEMOSTRACIÓN EN VIVO</div>
          <div class="card-text" style="font-size: 11pt; margin-top: 10px;">
            1. Ejecución de la suite con Maven: <code>./mvnw test</code><br>
            2. Interacción con la consola SGAP (Unicidad, Topes y Errores defensivos).
          </div>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <span>Plan de Calidad SGAP — ISII EAM</span>
      <span>Diapositiva 8 / 10</span>
    </div>
  </div>

  <!-- ==================== SLIDE 9: CALIDAD ISO 25010 Y CMMI ==================== -->
  <div class="slide" id="slide-9">
    <div class="slide-header">
      <div>
        <div class="slide-badge">Etapa 4: Calidad de Software</div>
        <div class="slide-title">8. Estándares ISO/IEC 25010 y Madurez CMMI v2.0</div>
      </div>
      <div class="slide-speaker">Voz: Juan Pablo</div>
    </div>
    <div class="slide-content">
      <div class="col-1">
        <div class="card" style="margin-bottom: 12px;">
          <div class="card-title">🏆 3 Características de Calidad ISO/IEC 25010</div>
          <div class="card-text">
            • <strong>Adecuación Funcional:</strong> Corrección matemática bancaria con <code>BigDecimal</code> sin pérdida de centavos.<br>
            • <strong>Fiabilidad:</strong> Tolerancia a fallos ante entradas corruptas comprobada en 92 tests continuos.<br>
            • <strong>Mantenibilidad:</strong> Modularidad desacoplada y alta testabilidad con 100% de ramas cubiertas.
          </div>
        </div>
      </div>
      <div class="col-2">
        <div class="card card-success" style="margin-bottom: 12px;">
          <div class="card-title">🎖️ Autoevaluación Honesta en CMMI: Nivel 2 (Gestionado)</div>
          <div class="card-text">
            • <strong>Sustento:</strong> Gestión de requisitos, trazabilidad RTM, control de versiones Git y monitoreo Surefire.<br>
            • <em>¿Por qué no Nivel 3 aún?</em> Porque estas prácticas fueron gestionadas por el equipo para este proyecto; no están institucionalizadas como política en toda la facultad.
          </div>
        </div>
        <div class="card">
          <div class="card-title">🚀 Plan de Acción para Escalar a Nivel 3 (Definido)</div>
          <div class="card-text">
            1. Estandarización de plantillas de prueba como activos organizacionales.<br>
            2. Tubería CI/CD automatizada con GitHub Actions.<br>
            3. Umbrales obligatorios de cobertura de ramas (&ge;90%).
          </div>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <span>Plan de Calidad SGAP — ISII EAM</span>
      <span>Diapositiva 9 / 10</span>
    </div>
  </div>

  <!-- ==================== SLIDE 10: DOD Y CONCLUSIONES ==================== -->
  <div class="slide" id="slide-10">
    <div class="slide-header">
      <div>
        <div class="slide-badge">Cierre del Proyecto</div>
        <div class="slide-title">9. Definition of Done (DoD) y Conclusiones</div>
      </div>
      <div class="slide-speaker">Voz: Jhoan Sebastián & Juan Pablo</div>
    </div>
    <div class="slide-content">
      <div class="col-1">
        <div class="card" style="margin-bottom: 12px;">
          <div class="card-title">🛡️ Definition of Done (DoD) — 7 Condiciones</div>
          <div class="card-text">
            1. Código limpio sin advertencias de compilador.<br>
            2. Compilación reproducible con Maven (<code>clean compile</code>).<br>
            3. 100% pruebas verdes en Surefire (0 fallos, 0 errores).<br>
            4. Cobertura de ramas condicionales $\ge 90\%$.<br>
            5. Criterios de Aceptación BDD aprobados.<br>
            6. Revisión cruzada de código por pares (Peer Review).<br>
            7. Matriz RTM y manuales actualizados.
          </div>
        </div>
      </div>
      <div class="col-2">
        <div class="card card-success" style="margin-bottom: 12px;">
          <div class="card-title">🎓 Principales Lecciones de Ingeniería Aprendidas</div>
          <div class="card-text">
            • <strong>La falacia de los valores intermedios:</strong> Las pruebas tradicionales dan falsa seguridad; son los valores límite los que exponen los bugs reales.<br>
            • <strong>La calidad como cultura de proceso:</strong> Calidad no es probar al final, sino modelar con inmutabilidad, rigor matemático y automatización continua.
          </div>
        </div>
        <div class="card" style="text-align: center; background: #1e3a8a; color: white;">
          <div class="card-title" style="color: #93c5fd; font-size: 13pt;">✅ DICTAMEN FINAL: APROBADO Y ACEPTADO</div>
          <div class="card-text" style="color: #e2e8f0;">92 pruebas automatizadas exitosas — 0 Fallos — 100% de Éxito.</div>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <span>Plan de Calidad SGAP — ISII EAM</span>
      <span>Diapositiva 10 / 10</span>
    </div>
  </div>

</div>

<!-- Barra de navegación en pantalla -->
<div class="nav-controls">
  <button class="nav-btn" onclick="prevSlide()">◀ Anterior</button>
  <span class="slide-counter" id="slide-num">1 / 10</span>
  <button class="nav-btn" onclick="nextSlide()">Siguiente ▶</button>
  <button class="nav-btn" style="background: #475569;" onclick="toggleFullScreen()">⛶ Pantalla Completa</button>
</div>

<script>
  let currentSlide = 1;
  const totalSlides = 10;

  function showSlide(n) {
    document.querySelectorAll('.slide').forEach(s => s.classList.remove('active'));
    currentSlide = n;
    if (currentSlide > totalSlides) currentSlide = 1;
    if (currentSlide < 1) currentSlide = totalSlides;
    document.getElementById('slide-' + currentSlide).classList.add('active');
    document.getElementById('slide-num').innerText = currentSlide + ' / ' + totalSlides;
  }

  function nextSlide() { showSlide(currentSlide + 1); }
  function prevSlide() { showSlide(currentSlide - 1); }

  document.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
      nextSlide();
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
      prevSlide();
    }
  });

  function toggleFullScreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen();
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      }
    }
  }
</script>

</body>
</html>
"""

# Guardar el archivo HTML de la presentación
html_path = "/home/sebastian/Documentos/Pruebas_ingnieria/sgap-aceptacion/presentacion_sustentacion.html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_presentation)

print(f"Presentación interactiva HTML creada en: {html_path}")

# Compilar la presentación a PDF horizontal apaisado con LibreOffice
output_dir = "/home/sebastian/Documentos/Pruebas_ingnieria/sgap-aceptacion"
cmd = [
    "libreoffice",
    "-env:UserInstallation=file:///tmp/libreoffice_user",
    "--headless",
    "--convert-to", "pdf",
    html_path,
    "--outdir", output_dir
]

print("Compilando PDF de diapositivas...")
proc = subprocess.run(cmd, capture_output=True, text=True)
print("Salida:", proc.stdout)

# Renombrar a Presentacion_SGAP_Sustentacion.pdf
src_pdf = os.path.join(output_dir, "presentacion_sustentacion.pdf")
dest_pdf = os.path.join(output_dir, "Presentacion_SGAP_Sustentacion.pdf")
if os.path.exists(src_pdf):
    import shutil
    shutil.copyfile(src_pdf, dest_pdf)
    print(f"PDF de diapositivas generado exitosamente como: {dest_pdf}")
