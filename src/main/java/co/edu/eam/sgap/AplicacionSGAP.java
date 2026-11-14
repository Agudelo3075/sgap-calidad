package co.edu.eam.sgap;

import co.edu.eam.sgap.asistencia.ControlAsistencia;
import co.edu.eam.sgap.asistencia.EstadoAsistencia;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.format.DateTimeParseException;
import java.util.List;

/** Consola de SGAP: asistencia y mensualidades de una academia. */
public class AplicacionSGAP {

    static final String AYUDA =
            "Comandos:\n"
            + "  registrar nombre;AAAA-MM-DD;ESTADO   (ESTADO: PRESENTE, TARDE, AUSENTE o JUSTIFICADO)\n"
            + "  corregir nombre;AAAA-MM-DD;ESTADO\n"
            + "  porcentaje nombre\n"
            + "  alerta nombre\n"
            + "  riesgo\n"
            + "  asistentes AAAA-MM-DD\n"
            + "  recargo mensualidad;diasDeMora\n"
            + "  total mensualidad;diasDeMora\n"
            + "  anual mensualidad\n"
            + "  estadopago vencimiento;hoy         (fechas AAAA-MM-DD)\n"
            + "  ayuda | salir";

    public static void main(String[] args) throws IOException {
        ControlAsistencia asistencia = new ControlAsistencia();
        CalculadoraMensualidad calculadora = new CalculadoraMensualidad();
        BufferedReader entrada = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("SGAP - Gestion de Asistencia y Pagos. Escriba 'ayuda' para ver los comandos.");
        String linea;
        while ((linea = entrada.readLine()) != null && !linea.trim().equals("salir")) {
            System.out.println(procesar(linea.trim(), asistencia, calculadora));
        }
    }

    static String procesar(String linea, ControlAsistencia asistencia, CalculadoraMensualidad calc) {
        String comando = linea.contains(" ") ? linea.substring(0, linea.indexOf(' ')) : linea;
        String resto = linea.contains(" ") ? linea.substring(linea.indexOf(' ') + 1).trim() : "";
        String[] p = resto.split(";");
        try {
            switch (comando) {
                case "ayuda":
                    return AYUDA;
                case "registrar":
                    pedir(p, 3, "registrar nombre;AAAA-MM-DD;ESTADO");
                    asistencia.registrarAsistencia(p[0], fecha(p[1]), estado(p[2]));
                    return "OK";
                case "corregir":
                    pedir(p, 3, "corregir nombre;AAAA-MM-DD;ESTADO");
                    asistencia.corregirAsistencia(p[0], fecha(p[1]), estado(p[2]));
                    return "OK";
                case "porcentaje":
                    pedir(p, 1, "porcentaje nombre");
                    double pct = asistencia.calcularPorcentajeAsistencia(p[0]);
                    boolean cumple = asistencia.cumpleAsistenciaMinima(p[0], ControlAsistencia.ASISTENCIA_MINIMA);
                    return "Asistencia de " + p[0].trim() + ": " + pct + " % ("
                            + (cumple ? "cumple" : "NO cumple") + " el minimo de "
                            + ControlAsistencia.ASISTENCIA_MINIMA + " %)";
                case "alerta":
                    pedir(p, 1, "alerta nombre");
                    int racha = asistencia.contarAusenciasConsecutivas(p[0]);
                    return asistencia.requiereAlertaAcudiente(p[0])
                            ? "ALERTA al acudiente de " + p[0].trim() + ": " + racha + " ausencias seguidas"
                            : "Sin alerta para " + p[0].trim() + " (ausencias seguidas: " + racha + ")";
                case "riesgo":
                    List<String> riesgo = asistencia.obtenerEstudiantesEnRiesgo(ControlAsistencia.ASISTENCIA_MINIMA);
                    return riesgo.isEmpty() ? "Ningun estudiante en riesgo"
                            : "Estudiantes en riesgo: " + String.join(", ", riesgo);
                case "asistentes":
                    pedir(p, 1, "asistentes AAAA-MM-DD");
                    return "Asistentes el " + fecha(p[0]) + ": " + asistencia.contarAsistentesEnFecha(fecha(p[0]));
                case "recargo":
                    pedir(p, 2, "recargo mensualidad;diasDeMora");
                    return "Recargo por mora: " + calc.calcularRecargoPorMora(dinero(p[0]), entero(p[1]));
                case "total":
                    pedir(p, 2, "total mensualidad;diasDeMora");
                    return "Total a pagar: " + calc.calcularTotalAPagar(dinero(p[0]), entero(p[1]));
                case "anual":
                    pedir(p, 1, "anual mensualidad");
                    return "Pago anual (10 mensualidades): " + calc.calcularPagoAnual(dinero(p[0]));
                case "estadopago":
                    pedir(p, 2, "estadopago vencimiento;hoy");
                    EstadoPago ep = calc.determinarEstadoPago(fecha(p[0]), fecha(p[1]));
                    return "Estado del pago: " + ep;
                default:
                    return "ERROR: comando desconocido (escriba 'ayuda')";
            }
        } catch (IllegalArgumentException | IllegalStateException e) {
            return "ERROR: " + e.getMessage();
        }
    }

    static void pedir(String[] partes, int cantidad, String uso) {
        if (partes.length != cantidad || partes[0].isBlank()) {
            throw new IllegalArgumentException("use " + uso);
        }
    }

    static LocalDate fecha(String texto) {
        try {
            return LocalDate.parse(texto.trim());
        } catch (DateTimeParseException e) {
            throw new IllegalArgumentException("fecha invalida, use AAAA-MM-DD");
        }
    }

    static EstadoAsistencia estado(String texto) {
        try {
            return EstadoAsistencia.valueOf(texto.trim().toUpperCase());
        } catch (IllegalArgumentException e) {
            throw new IllegalArgumentException("estado invalido (PRESENTE, TARDE, AUSENTE o JUSTIFICADO)");
        }
    }

    static BigDecimal dinero(String texto) {
        try {
            return new BigDecimal(texto.trim());
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("valor numerico invalido");
        }
    }

    static int entero(String texto) {
        try {
            return Integer.parseInt(texto.trim());
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("los dias de mora deben ser un numero entero");
        }
    }
}
