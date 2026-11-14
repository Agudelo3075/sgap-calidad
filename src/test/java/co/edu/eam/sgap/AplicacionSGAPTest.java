package co.edu.eam.sgap;

import co.edu.eam.sgap.asistencia.ControlAsistencia;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Pruebas Unitarias y de Integración - AplicacionSGAP (Consola)")
class AplicacionSGAPTest {

    private ControlAsistencia asistencia;
    private CalculadoraMensualidad calculadora;

    @BeforeEach
    void setUp() {
        asistencia = new ControlAsistencia();
        calculadora = new CalculadoraMensualidad();
    }

    private String ejecutar(String linea) {
        return AplicacionSGAP.procesar(linea, asistencia, calculadora);
    }

    @Test
    @DisplayName("Comando 'ayuda' despliega la lista de comandos disponibles")
    void comandoAyuda() {
        String res = ejecutar("ayuda");
        assertTrue(res.contains("Comandos:"));
        assertTrue(res.contains("registrar"));
        assertTrue(res.contains("recargo"));
    }

    @Test
    @DisplayName("Comando 'registrar' exitoso y validaciones")
    void comandoRegistrar() {
        String res = ejecutar("registrar Ana;2026-11-01;PRESENTE");
        assertEquals("OK", res);

        // Intento duplicado
        String dup = ejecutar("registrar Ana;2026-11-01;TARDE");
        assertTrue(dup.startsWith("ERROR: Ya existe un registro"));

        // Formato inválido de fecha
        String errFecha = ejecutar("registrar Ana;2026-99-99;PRESENTE");
        assertEquals("ERROR: fecha invalida, use AAAA-MM-DD", errFecha);

        // Estado inválido
        String errEstado = ejecutar("registrar Ana;2026-11-02;VACACIONES");
        assertEquals("ERROR: estado invalido (PRESENTE, TARDE, AUSENTE o JUSTIFICADO)", errEstado);

        // Argumentos incompletos
        String errArgs = ejecutar("registrar Ana;2026-11-01");
        assertTrue(errArgs.startsWith("ERROR: use registrar"));
    }

    @Test
    @DisplayName("Comando 'corregir' actualiza asistencia correctamente")
    void comandoCorregir() {
        ejecutar("registrar Carlos;2026-11-01;AUSENTE");
        String res = ejecutar("corregir Carlos;2026-11-01;JUSTIFICADO");
        assertEquals("OK", res);

        // Corregir registro inexistente
        String err = ejecutar("corregir Carlos;2026-11-02;PRESENTE");
        assertTrue(err.startsWith("ERROR: No existe un registro"));
    }

    @Test
    @DisplayName("Comando 'porcentaje' reporta asistencia y cumplimiento")
    void comandoPorcentaje() {
        ejecutar("registrar Maria;2026-11-01;PRESENTE");
        ejecutar("registrar Maria;2026-11-02;AUSENTE");

        String res = ejecutar("porcentaje Maria");
        assertEquals("Asistencia de Maria: 50.0 % (NO cumple el minimo de 80.0 %)", res);

        ejecutar("registrar Juan;2026-11-01;PRESENTE");
        String resJuan = ejecutar("porcentaje Juan");
        assertEquals("Asistencia de Juan: 100.0 % (cumple el minimo de 80.0 %)", resJuan);
    }

    @Test
    @DisplayName("Comando 'alerta' informa si requiere contactar al acudiente")
    void comandoAlerta() {
        ejecutar("registrar Pedro;2026-11-01;AUSENTE");
        ejecutar("registrar Pedro;2026-11-02;AUSENTE");
        String resSinAlerta = ejecutar("alerta Pedro");
        assertEquals("Sin alerta para Pedro (ausencias seguidas: 2)", resSinAlerta);

        ejecutar("registrar Pedro;2026-11-03;AUSENTE");
        String resConAlerta = ejecutar("alerta Pedro");
        assertEquals("ALERTA al acudiente de Pedro: 3 ausencias seguidas", resConAlerta);
    }

    @Test
    @DisplayName("Comando 'riesgo' lista estudiantes por debajo del 80%")
    void comandoRiesgo() {
        String vacio = ejecutar("riesgo");
        assertEquals("Ningun estudiante en riesgo", vacio);

        ejecutar("registrar David;2026-11-01;AUSENTE");
        ejecutar("registrar Camilo;2026-11-01;AUSENTE");
        String res = ejecutar("riesgo");
        assertEquals("Estudiantes en riesgo: Camilo, David", res);
    }

    @Test
    @DisplayName("Comando 'asistentes' en fecha específica")
    void comandoAsistentes() {
        ejecutar("registrar Ana;2026-11-01;PRESENTE");
        ejecutar("registrar Luis;2026-11-01;TARDE");
        ejecutar("registrar Sara;2026-11-01;AUSENTE");

        String res = ejecutar("asistentes 2026-11-01");
        assertEquals("Asistentes el 2026-11-01: 2", res);
    }

    @Test
    @DisplayName("Comando 'recargo' y 'total' calculan mora correctamente")
    void comandosRecargoYTotal() {
        String recargo = ejecutar("recargo 80000;10");
        assertEquals("Recargo por mora: 4000.00", recargo);

        String total = ejecutar("total 80000;10");
        assertEquals("Total a pagar: 84000.00", total);

        // Error numérico
        String err = ejecutar("recargo abc;10");
        assertEquals("ERROR: valor numerico invalido", err);

        String errDias = ejecutar("recargo 80000;diez");
        assertEquals("ERROR: los dias de mora deben ser un numero entero", errDias);
    }

    @Test
    @DisplayName("Comando 'anual' calcula pago de 10 mensualidades")
    void comandoAnual() {
        String anual = ejecutar("anual 80000");
        assertEquals("Pago anual (10 mensualidades): 800000.00", anual);
    }

    @Test
    @DisplayName("Comando 'estadopago' determina AL_DIA, POR_VENCER o EN_MORA")
    void comandoEstadoPago() {
        assertEquals("Estado del pago: AL_DIA", ejecutar("estadopago 2026-11-15;2026-11-10"));
        assertEquals("Estado del pago: POR_VENCER", ejecutar("estadopago 2026-11-15;2026-11-13"));
        assertEquals("Estado del pago: EN_MORA", ejecutar("estadopago 2026-11-15;2026-11-16"));
    }

    @ParameterizedTest
    @ValueSource(strings = {"inventado", "saludo", "test 123", "pagar 1000"})
    @DisplayName("Comando desconocido retorna mensaje de error amigable")
    void comandoDesconocido(String cmd) {
        String res = ejecutar(cmd);
        assertEquals("ERROR: comando desconocido (escriba 'ayuda')", res);
    }
}

