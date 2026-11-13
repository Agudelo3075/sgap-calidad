package co.edu.eam.sgap.asistencia;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.EnumSource;
import org.junit.jupiter.params.provider.NullAndEmptySource;
import org.junit.jupiter.params.provider.ValueSource;

import java.time.LocalDate;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Pruebas Unitarias - ControlAsistencia")
class ControlAsistenciaTest {

    private ControlAsistencia control;

    @BeforeEach
    void setUp() {
        control = new ControlAsistencia();
    }

    @Nested
    @DisplayName("Registro de Asistencia")
    class RegistroAsistenciaTests {

        @ParameterizedTest
        @EnumSource(EstadoAsistencia.class)
        @DisplayName("Registrar asistencia válida en todos los estados posibles")
        void registrarAsistenciaValida(EstadoAsistencia estado) {
            LocalDate fecha = LocalDate.of(2026, 11, 1);
            control.registrarAsistencia("Carlos", fecha, estado);

            assertEquals(1, control.contarPorEstado("Carlos", estado));
        }

        @Test
        @DisplayName("El nombre del estudiante se normaliza eliminando espacios en blanco circundantes")
        void normalizarNombreEstudiante() {
            LocalDate fecha = LocalDate.of(2026, 11, 1);
            control.registrarAsistencia("   Sofia Lopez   ", fecha, EstadoAsistencia.PRESENTE);

            assertEquals(1, control.contarPorEstado("Sofia Lopez", EstadoAsistencia.PRESENTE));
            assertEquals(100.0, control.calcularPorcentajeAsistencia("Sofia Lopez"));
        }

        @ParameterizedTest
        @NullAndEmptySource
        @ValueSource(strings = {"   ", "\t", "\n"})
        @DisplayName("Nombre nulo, vacío o en blanco debe lanzar IllegalArgumentException")
        void nombreInvalidoLanzaExcepcion(String nombreInvalido) {
            LocalDate fecha = LocalDate.of(2026, 11, 1);
            IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () ->
                    control.registrarAsistencia(nombreInvalido, fecha, EstadoAsistencia.PRESENTE));
            assertEquals("El nombre del estudiante es obligatorio", ex.getMessage());
        }

        @Test
        @DisplayName("Fecha o estado nulos debe lanzar IllegalArgumentException")
        void fechaOEstadoNulosLanzanExcepcion() {
            assertThrows(IllegalArgumentException.class, () ->
                    control.registrarAsistencia("Ana", null, EstadoAsistencia.PRESENTE));
            assertThrows(IllegalArgumentException.class, () ->
                    control.registrarAsistencia("Ana", LocalDate.of(2026, 11, 1), null));
        }

        @Test
        @DisplayName("Registrar duplicado para un mismo estudiante en la misma fecha lanza IllegalStateException")
        void registroDuplicadoMismoDiaLanzaExcepcion() {
            LocalDate fecha = LocalDate.of(2026, 11, 1);
            control.registrarAsistencia("Ana", fecha, EstadoAsistencia.PRESENTE);

            IllegalStateException ex = assertThrows(IllegalStateException.class, () ->
                    control.registrarAsistencia("Ana", fecha, EstadoAsistencia.TARDE));

            assertTrue(ex.getMessage().contains("Ya existe un registro de Ana"));
        }

        @Test
        @DisplayName("Permite registrar diferentes estudiantes en la misma fecha")
        void registrarMultiplesEstudiantesMismaFecha() {
            LocalDate fecha = LocalDate.of(2026, 11, 1);
            control.registrarAsistencia("Ana", fecha, EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Juan", fecha, EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Pedro", fecha, EstadoAsistencia.TARDE);

            assertEquals(3, control.contarAsistentesEnFecha(fecha));
        }
    }

    @Nested
    @DisplayName("Corrección de Asistencia")
    class CorreccionAsistenciaTests {

        @Test
        @DisplayName("Corregir un registro existente actualiza el estado correctamente")
        void corregirRegistroExistente() {
            LocalDate fecha = LocalDate.of(2026, 11, 1);
            control.registrarAsistencia("Mateo", fecha, EstadoAsistencia.AUSENTE);
            assertEquals(1, control.contarPorEstado("Mateo", EstadoAsistencia.AUSENTE));

            control.corregirAsistencia("Mateo", fecha, EstadoAsistencia.JUSTIFICADO);

            assertEquals(0, control.contarPorEstado("Mateo", EstadoAsistencia.AUSENTE));
            assertEquals(1, control.contarPorEstado("Mateo", EstadoAsistencia.JUSTIFICADO));
        }

        @Test
        @DisplayName("Corregir un registro inexistente lanza IllegalStateException")
        void corregirRegistroInexistenteLanzaExcepcion() {
            LocalDate fecha = LocalDate.of(2026, 11, 1);
            IllegalStateException ex = assertThrows(IllegalStateException.class, () ->
                    control.corregirAsistencia("NoExiste", fecha, EstadoAsistencia.PRESENTE));

            assertTrue(ex.getMessage().contains("No existe un registro"));
        }

        @Test
        @DisplayName("Corregir con parámetros nulos lanza IllegalArgumentException")
        void corregirParametrosNulosLanzaExcepcion() {
            LocalDate fecha = LocalDate.of(2026, 11, 1);
            assertThrows(IllegalArgumentException.class, () ->
                    control.corregirAsistencia(null, fecha, EstadoAsistencia.PRESENTE));
            assertThrows(IllegalArgumentException.class, () ->
                    control.corregirAsistencia("Mateo", null, EstadoAsistencia.PRESENTE));
            assertThrows(IllegalArgumentException.class, () ->
                    control.corregirAsistencia("Mateo", fecha, null));
        }
    }

    @Nested
    @DisplayName("Cálculo de Porcentajes de Asistencia")
    class PorcentajeAsistenciaTests {

        @Test
        @DisplayName("Estudiante sin registros retorna 0.0%")
        void sinRegistrosRetornaCero() {
            assertEquals(0.0, control.calcularPorcentajeAsistencia("EstudianteNuevo"));
        }

        @Test
        @DisplayName("Estudiante con solo ausencias justificadas retorna 0.0% (evita división por cero)")
        void soloJustificadasRetornaCero() {
            control.registrarAsistencia("Lucas", LocalDate.of(2026, 11, 1), EstadoAsistencia.JUSTIFICADO);
            control.registrarAsistencia("Lucas", LocalDate.of(2026, 11, 2), EstadoAsistencia.JUSTIFICADO);

            assertEquals(0.0, control.calcularPorcentajeAsistencia("Lucas"));
        }

        @Test
        @DisplayName("PRESENTE y TARDE cuentan como asistencias completas (100%)")
        void presenteYTardeSumanComoAsistencia() {
            control.registrarAsistencia("Sara", LocalDate.of(2026, 11, 1), EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Sara", LocalDate.of(2026, 11, 2), EstadoAsistencia.TARDE);

            assertEquals(100.0, control.calcularPorcentajeAsistencia("Sara"));
        }

        @Test
        @DisplayName("Cálculo estándar con ausencias: 3 asistencias de 4 clases = 75.0%")
        void calculoConAusencia() {
            control.registrarAsistencia("David", LocalDate.of(2026, 11, 1), EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("David", LocalDate.of(2026, 11, 2), EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("David", LocalDate.of(2026, 11, 3), EstadoAsistencia.TARDE);
            control.registrarAsistencia("David", LocalDate.of(2026, 11, 4), EstadoAsistencia.AUSENTE);

            assertEquals(75.0, control.calcularPorcentajeAsistencia("David"));
        }

        @Test
        @DisplayName("Las ausencias justificadas NO se cuentan en la base del cálculo")
        void justificadasNoAfectanBaseNegativamente() {
            // Total registros: 4 (2 PRESENTE, 1 JUSTIFICADO, 1 AUSENTE)
            // Base = 4 - 1 = 3 clases exigibles. Asistidas = 2.
            // 2 / 3 = 66.6666...% -> redondeado a 66.67%
            control.registrarAsistencia("Elena", LocalDate.of(2026, 11, 1), EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Elena", LocalDate.of(2026, 11, 2), EstadoAsistencia.JUSTIFICADO);
            control.registrarAsistencia("Elena", LocalDate.of(2026, 11, 3), EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Elena", LocalDate.of(2026, 11, 4), EstadoAsistencia.AUSENTE);

            assertEquals(66.67, control.calcularPorcentajeAsistencia("Elena"));
        }

        @Test
        @DisplayName("1 Asistencia y 1 Justificada debe ser 100% de asistencia exigible")
        void unaAsistenciaYUnaJustificadaEsCienPorCiento() {
            control.registrarAsistencia("Camila", LocalDate.of(2026, 11, 1), EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Camila", LocalDate.of(2026, 11, 2), EstadoAsistencia.JUSTIFICADO);

            assertEquals(100.0, control.calcularPorcentajeAsistencia("Camila"));
        }
    }

    @Nested
    @DisplayName("Cumplimiento de Asistencia Mínima")
    class CumpleAsistenciaMinimaTests {

        @Test
        @DisplayName("Cumple si el porcentaje es mayor o exactamente igual al mínimo requerido (80.0%)")
        void cumpleAsistenciaMinimaLimiteExacto() {
            // 4 presentes de 5 = 80.0%
            LocalDate base = LocalDate.of(2026, 11, 1);
            control.registrarAsistencia("Daniel", base, EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Daniel", base.plusDays(1), EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Daniel", base.plusDays(2), EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Daniel", base.plusDays(3), EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Daniel", base.plusDays(4), EstadoAsistencia.AUSENTE);

            assertEquals(80.0, control.calcularPorcentajeAsistencia("Daniel"));
            assertTrue(control.cumpleAsistenciaMinima("Daniel", 80.0));
        }

        @Test
        @DisplayName("No cumple si el porcentaje está por debajo del mínimo requerido")
        void noCumpleAsistenciaMinima() {
            // 3 presentes de 4 = 75.0%
            LocalDate base = LocalDate.of(2026, 11, 1);
            control.registrarAsistencia("Laura", base, EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Laura", base.plusDays(1), EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Laura", base.plusDays(2), EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Laura", base.plusDays(3), EstadoAsistencia.AUSENTE);

            assertFalse(control.cumpleAsistenciaMinima("Laura", 80.0));
        }

        @ParameterizedTest
        @ValueSource(doubles = {-0.1, -10.0, 100.1, 150.0})
        @DisplayName("Porcentaje mínimo menor a 0 o mayor a 100 debe lanzar IllegalArgumentException")
        void porcentajeMinimoInvalidoLanzaExcepcion(double minimoInvalido) {
            assertThrows(IllegalArgumentException.class, () ->
                    control.cumpleAsistenciaMinima("Daniel", minimoInvalido));
        }
    }

    @Nested
    @DisplayName("Ausencias Consecutivas y Alertas")
    class AusenciasConsecutivasYAlertasTests {

        @Test
        @DisplayName("Sin ausencias o con ausencias aisladas la racha es menor a 3")
        void ausenciasAisladasNoSuperanRacha() {
            LocalDate d = LocalDate.of(2026, 11, 1);
            control.registrarAsistencia("Samuel", d, EstadoAsistencia.AUSENTE);
            control.registrarAsistencia("Samuel", d.plusDays(1), EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Samuel", d.plusDays(2), EstadoAsistencia.AUSENTE);
            control.registrarAsistencia("Samuel", d.plusDays(3), EstadoAsistencia.TARDE);
            control.registrarAsistencia("Samuel", d.plusDays(4), EstadoAsistencia.AUSENTE);

            assertEquals(1, control.contarAusenciasConsecutivas("Samuel"));
            assertFalse(control.requiereAlertaAcudiente("Samuel"));
        }

        @Test
        @DisplayName("Llegar al límite de 3 ausencias consecutivas activa la alerta al acudiente")
        void tresAusenciasConsecutivasActivaAlerta() {
            LocalDate d = LocalDate.of(2026, 11, 1);
            control.registrarAsistencia("Valeria", d, EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Valeria", d.plusDays(1), EstadoAsistencia.AUSENTE);
            control.registrarAsistencia("Valeria", d.plusDays(2), EstadoAsistencia.AUSENTE);
            control.registrarAsistencia("Valeria", d.plusDays(3), EstadoAsistencia.AUSENTE);

            assertEquals(3, control.contarAusenciasConsecutivas("Valeria"));
            assertTrue(control.requiereAlertaAcudiente("Valeria"));
        }

        @Test
        @DisplayName("Una ausencia justificada rompe la racha de ausencias consecutivas injustificadas")
        void justificadaRompeRachaDeAusencias() {
            LocalDate d = LocalDate.of(2026, 11, 1);
            control.registrarAsistencia("Felipe", d, EstadoAsistencia.AUSENTE);
            control.registrarAsistencia("Felipe", d.plusDays(1), EstadoAsistencia.AUSENTE);
            control.registrarAsistencia("Felipe", d.plusDays(2), EstadoAsistencia.JUSTIFICADO); // Rompe racha
            control.registrarAsistencia("Felipe", d.plusDays(3), EstadoAsistencia.AUSENTE);

            assertEquals(2, control.contarAusenciasConsecutivas("Felipe"));
            assertFalse(control.requiereAlertaAcudiente("Felipe"));
        }

        @Test
        @DisplayName("Los registros se evalúan cronológicamente incluso si se ingresan desordenados")
        void ordenCronologicoIndependienteDelOrdenDeInsercion() {
            // Se ingresan en desorden: día 4, día 1, día 3, día 2
            LocalDate d = LocalDate.of(2026, 11, 1);
            control.registrarAsistencia("Tomas", d.plusDays(3), EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Tomas", d, EstadoAsistencia.AUSENTE);
            control.registrarAsistencia("Tomas", d.plusDays(2), EstadoAsistencia.AUSENTE);
            control.registrarAsistencia("Tomas", d.plusDays(1), EstadoAsistencia.AUSENTE);

            // Cronológico: d(AUS), d+1(AUS), d+2(AUS), d+3(PRES) -> racha de 3
            assertEquals(3, control.contarAusenciasConsecutivas("Tomas"));
            assertTrue(control.requiereAlertaAcudiente("Tomas"));
        }
    }

    @Nested
    @DisplayName("Estudiantes en Riesgo y Asistentes por Fecha")
    class RiesgoYAsistentesPorFechaTests {

        @Test
        @DisplayName("Obtener estudiantes en riesgo devuelve la lista ordenada alfabéticamente")
        void estudiantesEnRiesgoOrdenAlfabetico() {
            LocalDate d = LocalDate.of(2026, 11, 1);
            // Carlos: 50%
            control.registrarAsistencia("Carlos", d, EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Carlos", d.plusDays(1), EstadoAsistencia.AUSENTE);

            // Ana: 0%
            control.registrarAsistencia("Ana", d, EstadoAsistencia.AUSENTE);

            // Beatriz: 50%
            control.registrarAsistencia("Beatriz", d, EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Beatriz", d.plusDays(1), EstadoAsistencia.AUSENTE);

            // David: 100%
            control.registrarAsistencia("David", d, EstadoAsistencia.PRESENTE);

            List<String> enRiesgo = control.obtenerEstudiantesEnRiesgo(80.0);

            // Solo Ana, Beatriz y Carlos están por debajo de 80.0% y deben estar en orden alfabético
            assertEquals(List.of("Ana", "Beatriz", "Carlos"), enRiesgo);
        }

        @Test
        @DisplayName("Si ningún estudiante está en riesgo retorna lista vacía")
        void ningunEstudianteEnRiesgoRetornaVacio() {
            control.registrarAsistencia("Ana", LocalDate.of(2026, 11, 1), EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Bernardo", LocalDate.of(2026, 11, 1), EstadoAsistencia.TARDE);

            assertTrue(control.obtenerEstudiantesEnRiesgo(80.0).isEmpty());
        }

        @Test
        @DisplayName("Contar asistentes en fecha suma PRESENTES y TARDES pero ignora AUSENTES y JUSTIFICADOS")
        void contarAsistentesEnFechaEspecifica() {
            LocalDate fecha = LocalDate.of(2026, 11, 5);
            control.registrarAsistencia("Estudiante1", fecha, EstadoAsistencia.PRESENTE);
            control.registrarAsistencia("Estudiante2", fecha, EstadoAsistencia.TARDE);
            control.registrarAsistencia("Estudiante3", fecha, EstadoAsistencia.AUSENTE);
            control.registrarAsistencia("Estudiante4", fecha, EstadoAsistencia.JUSTIFICADO);

            // En otra fecha:
            control.registrarAsistencia("Estudiante5", fecha.plusDays(1), EstadoAsistencia.PRESENTE);

            assertEquals(2, control.contarAsistentesEnFecha(fecha));
            assertEquals(0, control.contarAsistentesEnFecha(LocalDate.of(2026, 11, 20)));
        }

        @Test
        @DisplayName("Contar asistentes con fecha nula lanza IllegalArgumentException")
        void contarAsistentesFechaNulaLanzaExcepcion() {
            assertThrows(IllegalArgumentException.class, () ->
                    control.contarAsistentesEnFecha(null));
        }
    }
}

