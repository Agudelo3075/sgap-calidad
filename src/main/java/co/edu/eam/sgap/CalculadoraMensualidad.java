package co.edu.eam.sgap;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

/**
 * Lógica de negocio de SGAP para el cálculo de mensualidades.
 * Responde al riesgo R4 de la matriz de riesgos ("errores en el cálculo de
 * mensualidades y pagos"). Se usa BigDecimal porque double no es exacto
 * para dinero.
 */
public class CalculadoraMensualidad {

    /** Recargo por cada día de mora: 0,5 %. */
    public static final BigDecimal TASA_RECARGO_DIARIA = new BigDecimal("0.005");
    /** El recargo nunca supera el 15 % de la mensualidad. */
    public static final BigDecimal TOPE_RECARGO = new BigDecimal("0.15");
    /** Pago anual: se pagan 10 meses y 2 quedan gratis. */
    public static final int MESES_PAGO_ANUAL = 10;
    /** Días de anticipación para avisar al acudiente. */
    public static final int DIAS_AVISO_PREVIO = 3;

    /** Recargo en pesos por pagar con retraso. Sin mora, el recargo es 0. */
    public BigDecimal calcularRecargoPorMora(BigDecimal mensualidad, int diasMora) {
        validarMensualidad(mensualidad);
        if (diasMora < 0) {
            throw new IllegalArgumentException("Los días de mora no pueden ser negativos");
        }
        BigDecimal tasa = TASA_RECARGO_DIARIA.multiply(BigDecimal.valueOf(diasMora));
        if (tasa.compareTo(TOPE_RECARGO) > 0) {
            tasa = TOPE_RECARGO;
        }
        return mensualidad.multiply(tasa).setScale(2, RoundingMode.HALF_UP);
    }

    /** Valor total a pagar = mensualidad + recargo por mora. */
    public BigDecimal calcularTotalAPagar(BigDecimal mensualidad, int diasMora) {
        BigDecimal recargo = calcularRecargoPorMora(mensualidad, diasMora);
        return mensualidad.setScale(2, RoundingMode.HALF_UP).add(recargo);
    }

    /** Pago anual con descuento: 10 mensualidades en lugar de 12. */
    public BigDecimal calcularPagoAnual(BigDecimal mensualidad) {
        validarMensualidad(mensualidad);
        return mensualidad.multiply(BigDecimal.valueOf(MESES_PAGO_ANUAL))
                .setScale(2, RoundingMode.HALF_UP);
    }

    /** Clasifica una mensualidad según la fecha de hoy y su vencimiento. */
    public EstadoPago determinarEstadoPago(LocalDate vencimiento, LocalDate hoy) {
        if (vencimiento == null || hoy == null) {
            throw new IllegalArgumentException("Las fechas no pueden ser nulas");
        }
        if (hoy.isAfter(vencimiento)) {
            return EstadoPago.EN_MORA;
        }
        long diasFaltantes = ChronoUnit.DAYS.between(hoy, vencimiento);
        return diasFaltantes <= DIAS_AVISO_PREVIO ? EstadoPago.POR_VENCER : EstadoPago.AL_DIA;
    }

    private void validarMensualidad(BigDecimal mensualidad) {
        if (mensualidad == null || mensualidad.signum() <= 0) {
            throw new IllegalArgumentException("La mensualidad debe ser mayor que cero");
        }
    }
}
