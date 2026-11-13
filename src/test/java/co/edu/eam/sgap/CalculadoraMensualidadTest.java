package co.edu.eam.sgap;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

import java.math.BigDecimal;
import java.time.LocalDate;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Pruebas Unitarias - CalculadoraMensualidad")
class CalculadoraMensualidadTest {

    private CalculadoraMensualidad calculadora;

    @BeforeEach
    void setUp() {
        calculadora = new CalculadoraMensualidad();
    }

    @Nested
    @DisplayName("Cálculo de Recargo por Mora")
    class RecargoPorMoraTests {

        @Test
        @DisplayName("Sin días de mora el recargo debe ser 0.00")
        void sinMoraRecargoCero() {
            BigDecimal mensualidad = new BigDecimal("80000");
            BigDecimal recargo = calculadora.calcularRecargoPorMora(mensualidad, 0);
            assertEquals(new BigDecimal("0.00"), recargo);
        }

        @ParameterizedTest(name = "Mensualidad: 100000, Días mora: {0} -> Recargo esperado: {1}")
        @CsvSource({
                "1, 500.00",    // 0.5%
                "2, 1000.00",   // 1.0%
                "10, 5000.00",  // 5.0%
                "20, 10000.00", // 10.0%
                "29, 14500.00", // 14.5%
                "30, 15000.00"  // 15.0% (Límite exacto del tope)
        })
        @DisplayName("Cálculo proporcional de mora hasta alcanzar el tope del 15%")
        void recargoProporcionalHastaTope(int diasMora, String esperado) {
            BigDecimal mensualidad = new BigDecimal("100000");
            BigDecimal recargo = calculadora.calcularRecargoPorMora(mensualidad, diasMora);
            assertEquals(new BigDecimal(esperado), recargo);
        }

        @ParameterizedTest(name = "Días de mora que superan el tope: {0} días")
        @ValueSource(ints = {31, 40, 60, 100, 365})
        @DisplayName("El recargo nunca debe superar el 15% de la mensualidad (Tope máximo)")
        void recargoNoSuperaTopeDel15Porciento(int diasMora) {
            BigDecimal mensualidad = new BigDecimal("80000");
            BigDecimal recargoEsperado = new BigDecimal("12000.00"); // 80.000 * 0.15 = 12.000
            BigDecimal recargo = calculadora.calcularRecargoPorMora(mensualidad, diasMora);
            assertEquals(recargoEsperado, recargo);
        }

        @Test
        @DisplayName("Redondeo HALF_UP en valores con fracciones de centavo")
        void redondeoHalfUpExacto() {
            // 75.33 * 0.005 * 1 = 0.37665 -> debe redondear a 0.38
            BigDecimal mensualidad = new BigDecimal("75.33");
            BigDecimal recargo = calculadora.calcularRecargoPorMora(mensualidad, 1);
            assertEquals(new BigDecimal("0.38"), recargo);
        }

        @Test
        @DisplayName("Días de mora negativos debe lanzar IllegalArgumentException")
        void diasMoraNegativosLanzaExcepcion() {
            BigDecimal mensualidad = new BigDecimal("80000");
            IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () ->
                    calculadora.calcularRecargoPorMora(mensualidad, -1));
            assertEquals("Los días de mora no pueden ser negativos", ex.getMessage());
        }

        @Test
        @DisplayName("Mensualidad nula debe lanzar IllegalArgumentException")
        void mensualidadNulaLanzaExcepcion() {
            IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () ->
                    calculadora.calcularRecargoPorMora(null, 5));
            assertEquals("La mensualidad debe ser mayor que cero", ex.getMessage());
        }

        @ParameterizedTest
        @ValueSource(strings = {"0", "-1", "-50000"})
        @DisplayName("Mensualidad cero o negativa debe lanzar IllegalArgumentException")
        void mensualidadCeroONegativaLanzaExcepcion(String valor) {
            BigDecimal mensualidad = new BigDecimal(valor);
            IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () ->
                    calculadora.calcularRecargoPorMora(mensualidad, 5));
            assertEquals("La mensualidad debe ser mayor que cero", ex.getMessage());
        }
    }

    @Nested
    @DisplayName("Cálculo de Total a Pagar")
    class TotalAPagarTests {

        @Test
        @DisplayName("Total a pagar sin mora es igual a la mensualidad con 2 decimales")
        void totalSinMora() {
            BigDecimal mensualidad = new BigDecimal("80000");
            BigDecimal total = calculadora.calcularTotalAPagar(mensualidad, 0);
            assertEquals(new BigDecimal("80000.00"), total);
        }

        @Test
        @DisplayName("Total a pagar con mora incluye mensualidad más recargo")
        void totalConMora() {
            BigDecimal mensualidad = new BigDecimal("80000");
            // 10 días mora = 5% = 4000.00 -> Total = 84000.00
            BigDecimal total = calculadora.calcularTotalAPagar(mensualidad, 10);
            assertEquals(new BigDecimal("84000.00"), total);
        }

        @Test
        @DisplayName("Total a pagar con tope de mora aplicado")
        void totalConMoraTope() {
            BigDecimal mensualidad = new BigDecimal("100000");
            // 35 días mora -> recargo tope 15000.00 -> Total = 115000.00
            BigDecimal total = calculadora.calcularTotalAPagar(mensualidad, 35);
            assertEquals(new BigDecimal("115000.00"), total);
        }
    }

    @Nested
    @DisplayName("Cálculo de Pago Anual")
    class PagoAnualTests {

        @Test
        @DisplayName("Pago anual cobra 10 meses y otorga 2 meses de descuento")
        void pagoAnualEquivaleADiezMeses() {
            BigDecimal mensualidad = new BigDecimal("80000");
            BigDecimal anual = calculadora.calcularPagoAnual(mensualidad);
            assertEquals(new BigDecimal("800000.00"), anual);
        }

        @Test
        @DisplayName("Pago anual con decimales respeta escala de 2")
        void pagoAnualConDecimales() {
            BigDecimal mensualidad = new BigDecimal("120000.50");
            BigDecimal anual = calculadora.calcularPagoAnual(mensualidad);
            assertEquals(new BigDecimal("1200005.00"), anual);
        }

        @Test
        @DisplayName("Pago anual con mensualidad cero o nula lanza excepción")
        void pagoAnualMensualidadInvalida() {
            assertThrows(IllegalArgumentException.class, () -> calculadora.calcularPagoAnual(null));
            assertThrows(IllegalArgumentException.class, () -> calculadora.calcularPagoAnual(BigDecimal.ZERO));
        }
    }

    @Nested
    @DisplayName("Determinación del Estado de Pago")
    class EstadoPagoTests {

        private final LocalDate vencimiento = LocalDate.of(2026, 11, 15);

        @Test
        @DisplayName("Pago AL_DIA cuando faltan más de 3 días para el vencimiento")
        void estadoAlDiaMasDeTresDias() {
            LocalDate hoy4DiasAntes = vencimiento.minusDays(4);
            LocalDate hoy10DiasAntes = vencimiento.minusDays(10);

            assertEquals(EstadoPago.AL_DIA, calculadora.determinarEstadoPago(vencimiento, hoy4DiasAntes));
            assertEquals(EstadoPago.AL_DIA, calculadora.determinarEstadoPago(vencimiento, hoy10DiasAntes));
        }

        @ParameterizedTest(name = "Faltan {0} días para el vencimiento -> POR_VENCER")
        @ValueSource(ints = {3, 2, 1, 0})
        @DisplayName("Pago POR_VENCER en el rango de anticipación de 3 días y el mismo día de vencimiento")
        void estadoPorVencerEnVentanaDeAviso(int diasFaltantes) {
            LocalDate hoy = vencimiento.minusDays(diasFaltantes);
            assertEquals(EstadoPago.POR_VENCER, calculadora.determinarEstadoPago(vencimiento, hoy));
        }

        @ParameterizedTest(name = "{0} días después de la fecha de vencimiento -> EN_MORA")
        @ValueSource(ints = {1, 5, 30})
        @DisplayName("Pago EN_MORA cuando hoy es posterior al vencimiento")
        void estadoEnMoraDespuesDeVencimiento(int diasDespues) {
            LocalDate hoy = vencimiento.plusDays(diasDespues);
            assertEquals(EstadoPago.EN_MORA, calculadora.determinarEstadoPago(vencimiento, hoy));
        }

        @Test
        @DisplayName("Fechas nulas deben lanzar IllegalArgumentException")
        void fechasNulasLanzanExcepcion() {
            assertThrows(IllegalArgumentException.class, () ->
                    calculadora.determinarEstadoPago(null, LocalDate.now()));
            assertThrows(IllegalArgumentException.class, () ->
                    calculadora.determinarEstadoPago(LocalDate.now(), null));
        }
    }
}

