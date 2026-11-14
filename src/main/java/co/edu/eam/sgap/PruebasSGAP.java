package co.edu.eam.sgap;

import co.edu.eam.sgap.asistencia.ControlAsistencia;
import co.edu.eam.sgap.asistencia.EstadoAsistencia;

import java.math.BigDecimal;
import java.time.LocalDate;

public class PruebasSGAP {

    private static int aprobadas = 0;
    private static int falladas = 0;

    public static void verificar(String id, Object esperado, Object obtenido) {
        boolean ok = (esperado == null && obtenido == null) || (esperado != null && esperado.equals(obtenido));
        if (ok) {
            aprobadas++;
        } else {
            falladas++;
        }
        System.out.println(id + " | esperado=" + esperado + " | obtenido=" + obtenido
                + " -> " + (ok ? "APROBO" : "FALLO"));
    }

    public static void resumen() {
        System.out.println("==================================================");
        System.out.println("TOTAL PRUEBAS SGAP: Aprobadas: " + aprobadas + " | Falladas: " + falladas);
        System.out.println("==================================================");
    }

    public static void main(String[] args) {
        System.out.println("==========================================================");
        System.out.println("  EJECUCIÓN DE PRUEBAS DE SGAP (GUÍA 1 - INGENIERÍA DE SOFTWARE)");
        System.out.println("  Sistema de Gestión de Asistencia y Pagos");
        System.out.println("  Autores: Jhoan Sebastián Agudelo Mejía & Juan Pablo Bedoya Payán");
        System.out.println("==========================================================");

        ControlAsistencia control = new ControlAsistencia();
        CalculadoraMensualidad calc = new CalculadoraMensualidad();

        // CP-01: RF-01 Registro y unicidad de asistencia diaria (Integración)
        LocalDate f1 = LocalDate.of(2026, 11, 1);
        control.registrarAsistencia("Carlos", f1, EstadoAsistencia.PRESENTE);

        boolean duplicadoRechazado = false;
        try {
            control.registrarAsistencia("Carlos", f1, EstadoAsistencia.TARDE);
        } catch (IllegalStateException e) {
            duplicadoRechazado = true;
        }
        verificar("CP-01 [Integracion] RF-01 Rechazo de asistencia duplicada el mismo dia", true, duplicadoRechazado);

        // CP-02: RF-02 Cálculo ponderado con excusas médicas (Integración)
        LocalDate d1 = LocalDate.of(2026, 11, 1);
        LocalDate d2 = LocalDate.of(2026, 11, 2);
        LocalDate d3 = LocalDate.of(2026, 11, 3);
        LocalDate d4 = LocalDate.of(2026, 11, 4);

        control.registrarAsistencia("Ana", d1, EstadoAsistencia.PRESENTE);
        control.registrarAsistencia("Ana", d2, EstadoAsistencia.TARDE);
        control.registrarAsistencia("Ana", d3, EstadoAsistencia.JUSTIFICADO);
        verificar("CP-02A [Integracion] RF-02 Porcentaje con Pres+Tarde+Justificado (100.0%)", 100.0, control.calcularPorcentajeAsistencia("Ana"));

        control.registrarAsistencia("Ana", d4, EstadoAsistencia.AUSENTE);
        verificar("CP-02B [Integracion] RF-02 Porcentaje agregando 1 ausencia (66.67%)", 66.67, control.calcularPorcentajeAsistencia("Ana"));

        // CP-03: RF-03 Alerta de ausencias consecutivas - Frontera 3 (Integración)
        control.registrarAsistencia("Pedro", LocalDate.of(2026, 11, 1), EstadoAsistencia.AUSENTE);
        control.registrarAsistencia("Pedro", LocalDate.of(2026, 11, 2), EstadoAsistencia.AUSENTE);
        verificar("CP-03A [Integracion] RF-03 Alerta con 2 ausencias seguidas (fuera de frontera)", false, control.requiereAlertaAcudiente("Pedro"));

        control.registrarAsistencia("Pedro", LocalDate.of(2026, 11, 3), EstadoAsistencia.AUSENTE);
        verificar("CP-03B [Integracion] RF-03 Alerta con 3 ausencias seguidas (frontera exacta)", true, control.requiereAlertaAcudiente("Pedro"));

        // CP-04: RF-04 Recargo por mora y valor límite de tope 15% (Unitaria)
        BigDecimal mensualidad = new BigDecimal("100000");

        BigDecimal recargo0 = calc.calcularRecargoPorMora(mensualidad, 0);
        verificar("CP-04A [Unitaria] RF-04 Recargo 0 dias de mora ($0.00)", new BigDecimal("0.00"), recargo0);

        BigDecimal recargo10 = calc.calcularRecargoPorMora(mensualidad, 10);
        verificar("CP-04B [Unitaria] RF-04 Recargo 10 dias de mora ($5000.00)", new BigDecimal("5000.00"), recargo10);

        BigDecimal recargo30 = calc.calcularRecargoPorMora(mensualidad, 30);
        verificar("CP-04C [Unitaria] RF-04 Recargo 30 dias de mora (tope frontera $15000.00)", new BigDecimal("15000.00"), recargo30);

        BigDecimal recargo40 = calc.calcularRecargoPorMora(mensualidad, 40);
        verificar("CP-04D [Unitaria] RF-04 Recargo 40 dias de mora (acotado por tope $15000.00)", new BigDecimal("15000.00"), recargo40);

        BigDecimal total10 = calc.calcularTotalAPagar(mensualidad, 10);
        verificar("CP-04E [Unitaria] RF-04 Total a pagar 10 dias mora ($105000.00)", new BigDecimal("105000.00"), total10);

        BigDecimal anual = calc.calcularPagoAnual(mensualidad);
        verificar("CP-04F [Unitaria] RF-04 Pago anual con descuento 10 meses ($1000000.00)", new BigDecimal("1000000.00"), anual);

        // CP-05: RF-05 Estados de cobro y ventana preventiva (Unitaria)
        LocalDate vencimiento = LocalDate.of(2026, 11, 10);

        verificar("CP-05A [Unitaria] RF-05 Estado a 4 dias del vencimiento (AL_DIA)", EstadoPago.AL_DIA, calc.determinarEstadoPago(vencimiento, LocalDate.of(2026, 11, 6)));
        verificar("CP-05B [Unitaria] RF-05 Estado a 3 dias del vencimiento (POR_VENCER frontera)", EstadoPago.POR_VENCER, calc.determinarEstadoPago(vencimiento, LocalDate.of(2026, 11, 7)));
        verificar("CP-05C [Unitaria] RF-05 Estado el dia del vencimiento (POR_VENCER hoy)", EstadoPago.POR_VENCER, calc.determinarEstadoPago(vencimiento, LocalDate.of(2026, 11, 10)));
        verificar("CP-05D [Unitaria] RF-05 Estado 1 dia despues del vencimiento (EN_MORA)", EstadoPago.EN_MORA, calc.determinarEstadoPago(vencimiento, LocalDate.of(2026, 11, 11)));

        resumen();
    }
}

