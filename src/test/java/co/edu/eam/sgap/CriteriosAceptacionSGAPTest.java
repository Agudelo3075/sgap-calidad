package co.edu.eam.sgap;

import co.edu.eam.sgap.asistencia.ControlAsistencia;
import co.edu.eam.sgap.asistencia.EstadoAsistencia;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Pruebas de Criterios de Aceptación para SGAP.
 * Valida los requerimientos y expectativas del cliente (academia deportiva / musical)
 * utilizando el patrón Dado-Cuando-Entonces (Given-When-Then).
 */
@DisplayName("Pruebas de Criterios de Aceptación (BDD) - SGAP")
class CriteriosAceptacionSGAPTest {

    private ControlAsistencia controlAsistencia;
    private CalculadoraMensualidad calculadoraMensualidad;

    @BeforeEach
    void inicializarEntorno() {
        controlAsistencia = new ControlAsistencia();
        calculadoraMensualidad = new CalculadoraMensualidad();
    }

    @Test
    @DisplayName("CA-01: Registro diario de asistencia sin duplicidad en la misma jornada")
    void criterioAceptacion01_RegistroSinDuplicidad() {
        // GIVEN (Dado): Una academia con el estudiante "Esteban" activo
        LocalDate hoy = LocalDate.of(2026, 11, 10);

        // WHEN (Cuando): El docente registra su asistencia como PRESENTE
        controlAsistencia.registrarAsistencia("Esteban", hoy, EstadoAsistencia.PRESENTE);

        // THEN (Entonces): Se almacena la asistencia y se bloquea un segundo registro el mismo día
        assertEquals(1, controlAsistencia.contarPorEstado("Esteban", EstadoAsistencia.PRESENTE));

        IllegalStateException excepcion = assertThrows(IllegalStateException.class, () ->
                controlAsistencia.registrarAsistencia("Esteban", hoy, EstadoAsistencia.TARDE));

        assertTrue(excepcion.getMessage().contains("Ya existe un registro"));
    }

    @Test
    @DisplayName("CA-02: Llegadas tarde cuentan a favor de la asistencia del estudiante")
    void criterioAceptacion02_LlegadasTardeCuentanComoAsistencia() {
        // GIVEN: El estudiante "Juliana" tiene 1 clase puntual y 1 llegada tarde
        LocalDate d1 = LocalDate.of(2026, 11, 1);
        LocalDate d2 = LocalDate.of(2026, 11, 2);

        // WHEN: Se calculan las estadísticas
        controlAsistencia.registrarAsistencia("Juliana", d1, EstadoAsistencia.PRESENTE);
        controlAsistencia.registrarAsistencia("Juliana", d2, EstadoAsistencia.TARDE);

        // THEN: Su porcentaje de asistencia es 100% y cumple con el mínimo institucional (80%)
        assertEquals(100.0, controlAsistencia.calcularPorcentajeAsistencia("Juliana"));
        assertTrue(controlAsistencia.cumpleAsistenciaMinima("Juliana", 80.0));
    }

    @Test
    @DisplayName("CA-03: Excusas justificadas no perjudican el promedio del alumno")
    void criterioAceptacion03_ExcusasNoPerjudicanPromedio() {
        // GIVEN: El estudiante "Camilo" asiste a 3 clases, falta a 1 con excusa médica y falta a 1 sin excusa
        LocalDate base = LocalDate.of(2026, 11, 1);
        controlAsistencia.registrarAsistencia("Camilo", base, EstadoAsistencia.PRESENTE);
        controlAsistencia.registrarAsistencia("Camilo", base.plusDays(1), EstadoAsistencia.PRESENTE);
        controlAsistencia.registrarAsistencia("Camilo", base.plusDays(2), EstadoAsistencia.PRESENTE);
        controlAsistencia.registrarAsistencia("Camilo", base.plusDays(3), EstadoAsistencia.JUSTIFICADO);
        controlAsistencia.registrarAsistencia("Camilo", base.plusDays(4), EstadoAsistencia.AUSENTE);

        // WHEN: Se evalúa el porcentaje
        // Total evaluable: 5 - 1 justificada = 4 clases. Asistidas = 3.
        // Porcentaje esperado: 3 / 4 = 75.0%
        double porcentaje = controlAsistencia.calcularPorcentajeAsistencia("Camilo");

        // THEN: El cálculo excluye la clase justificada de la base penalizadora
        assertEquals(75.0, porcentaje);
        assertFalse(controlAsistencia.cumpleAsistenciaMinima("Camilo", 80.0));
    }

    @Test
    @DisplayName("CA-04: Alerta temprana automática al acudiente con 3 ausencias injustificadas seguidas")
    void criterioAceptacion04_AlertaTresAusenciasConsecutivas() {
        // GIVEN: El estudiante "Mateo" acumula 2 faltas consecutivas
        LocalDate dia1 = LocalDate.of(2026, 11, 1);
        LocalDate dia2 = LocalDate.of(2026, 11, 2);
        LocalDate dia3 = LocalDate.of(2026, 11, 3);

        controlAsistencia.registrarAsistencia("Mateo", dia1, EstadoAsistencia.AUSENTE);
        controlAsistencia.registrarAsistencia("Mateo", dia2, EstadoAsistencia.AUSENTE);

        // WHEN: Tiene 2 faltas, el sistema no debe alertar aún
        assertFalse(controlAsistencia.requiereAlertaAcudiente("Mateo"));

        // WHEN: Se registra la tercera falta consecutiva
        controlAsistencia.registrarAsistencia("Mateo", dia3, EstadoAsistencia.AUSENTE);

        // THEN: El sistema emite inmediatamente la condición de alerta
        assertEquals(3, controlAsistencia.contarAusenciasConsecutivas("Mateo"));
        assertTrue(controlAsistencia.requiereAlertaAcudiente("Mateo"));
    }

    @Test
    @DisplayName("CA-05: Detección y listado alfabético de estudiantes en riesgo académico (< 80%)")
    void criterioAceptacion05_ListadoEstudiantesEnRiesgo() {
        // GIVEN: Varios estudiantes con diferentes registros de asistencia
        LocalDate hoy = LocalDate.of(2026, 11, 1);
        LocalDate manana = LocalDate.of(2026, 11, 2);

        // Zoe: 1 presente, 1 ausente = 50% (En riesgo)
        controlAsistencia.registrarAsistencia("Zoe", hoy, EstadoAsistencia.PRESENTE);
        controlAsistencia.registrarAsistencia("Zoe", manana, EstadoAsistencia.AUSENTE);

        // Andres: 0 presente, 1 ausente = 0% (En riesgo)
        controlAsistencia.registrarAsistencia("Andres", hoy, EstadoAsistencia.AUSENTE);

        // Bernardo: 2 presentes = 100% (No en riesgo)
        controlAsistencia.registrarAsistencia("Bernardo", hoy, EstadoAsistencia.PRESENTE);
        controlAsistencia.registrarAsistencia("Bernardo", manana, EstadoAsistencia.PRESENTE);

        // WHEN: El coordinador solicita el reporte de riesgo
        List<String> enRiesgo = controlAsistencia.obtenerEstudiantesEnRiesgo(80.0);

        // THEN: Aparecen únicamente Zoe y Andres, en orden alfabético
        assertEquals(List.of("Andres", "Zoe"), enRiesgo);
    }

    @Test
    @DisplayName("CA-06: Consulta de aforo diario (asistencias efectivas en una fecha)")
    void criterioAceptacion06_ConsultaAforoEfectivo() {
        // GIVEN: Una clase donde asistieron 2 a tiempo, 1 tarde, 1 faltó y 1 con excusa
        LocalDate fecha = LocalDate.of(2026, 11, 5);
        controlAsistencia.registrarAsistencia("Alumno1", fecha, EstadoAsistencia.PRESENTE);
        controlAsistencia.registrarAsistencia("Alumno2", fecha, EstadoAsistencia.PRESENTE);
        controlAsistencia.registrarAsistencia("Alumno3", fecha, EstadoAsistencia.TARDE);
        controlAsistencia.registrarAsistencia("Alumno4", fecha, EstadoAsistencia.AUSENTE);
        controlAsistencia.registrarAsistencia("Alumno5", fecha, EstadoAsistencia.JUSTIFICADO);

        // WHEN: El docente consulta la cantidad de asistentes del día
        int asistentes = controlAsistencia.contarAsistentesEnFecha(fecha);

        // THEN: El aforo reportado es de 3 estudiantes presentes físicamente
        assertEquals(3, asistentes);
    }

    @Test
    @DisplayName("CA-07: Recargo por mora del 0.5% diario con tope máximo del 15%")
    void criterioAceptacion07_RecargoConTopeMaximo() {
        BigDecimal mensualidad = new BigDecimal("80000");

        // GIVEN / WHEN: 10 días de retraso (0.5% * 10 = 5% = 4000)
        BigDecimal recargo10Dias = calculadoraMensualidad.calcularRecargoPorMora(mensualidad, 10);
        BigDecimal total10Dias = calculadoraMensualidad.calcularTotalAPagar(mensualidad, 10);
        assertEquals(new BigDecimal("4000.00"), recargo10Dias);
        assertEquals(new BigDecimal("84000.00"), total10Dias);

        // GIVEN / WHEN: 40 días de retraso (0.5% * 40 = 20% > tope 15% = 12000)
        BigDecimal recargoTope = calculadoraMensualidad.calcularRecargoPorMora(mensualidad, 40);
        BigDecimal totalTope = calculadoraMensualidad.calcularTotalAPagar(mensualidad, 40);

        // THEN: Se aplica estrictamente el tope de 12.000 (15%)
        assertEquals(new BigDecimal("12000.00"), recargoTope);
        assertEquals(new BigDecimal("92000.00"), totalTope);
    }

    @Test
    @DisplayName("CA-08: Descuento por pronto pago anual (paga 10 mensualidades en lugar de 12)")
    void criterioAceptacion08_PagoAnualConDescuento() {
        // GIVEN: Una mensualidad de $100.000
        BigDecimal mensualidad = new BigDecimal("100000");

        // WHEN: El cliente paga el año completo por adelantado
        BigDecimal pagoAnual = calculadoraMensualidad.calcularPagoAnual(mensualidad);

        // THEN: El costo total es $1.000.000 (ahorro equivalente a 2 mensualidades = $200.000)
        assertEquals(new BigDecimal("1000000.00"), pagoAnual);
    }

    @Test
    @DisplayName("CA-09: Clasificación del estado de pago y ventana preventiva de cobro de 3 días")
    void criterioAceptacion09_ClasificacionEstadoPago() {
        LocalDate vencimiento = LocalDate.of(2026, 11, 20);

        // Caso 1: Faltan 5 días -> AL_DIA
        LocalDate fechaLejana = LocalDate.of(2026, 11, 15);
        assertEquals(EstadoPago.AL_DIA, calculadoraMensualidad.determinarEstadoPago(vencimiento, fechaLejana));

        // Caso 2: Faltan 2 días (dentro de ventana de aviso de 3 días) -> POR_VENCER
        LocalDate fechaAlerta = LocalDate.of(2026, 11, 18);
        assertEquals(EstadoPago.POR_VENCER, calculadoraMensualidad.determinarEstadoPago(vencimiento, fechaAlerta));

        // Caso 3: Mismo día de vencimiento -> POR_VENCER
        assertEquals(EstadoPago.POR_VENCER, calculadoraMensualidad.determinarEstadoPago(vencimiento, vencimiento));

        // Caso 4: 1 día después de la fecha de corte -> EN_MORA
        LocalDate fechaMora = LocalDate.of(2026, 11, 21);
        assertEquals(EstadoPago.EN_MORA, calculadoraMensualidad.determinarEstadoPago(vencimiento, fechaMora));
    }
}

