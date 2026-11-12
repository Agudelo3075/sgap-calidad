package co.edu.eam.sgap.asistencia;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.TreeSet;

/**
 * Funcionalidad de control de asistencia de SGAP.
 * Guarda los registros en memoria y ofrece 9 operaciones: registrar, corregir,
 * contar, calcular porcentajes, detectar ausencias seguidas y generar alertas.
 */
public class ControlAsistencia {

    /** Porcentaje mínimo de asistencia que debe tener un estudiante. */
    public static final double ASISTENCIA_MINIMA = 80.0;
    /** Con 3 ausencias seguidas se debe avisar al acudiente. */
    public static final int LIMITE_AUSENCIAS_CONSECUTIVAS = 3;

    private final List<RegistroAsistencia> registros = new ArrayList<>();

    // 1. Registrar una asistencia nueva
    public void registrarAsistencia(String estudiante, LocalDate fecha, EstadoAsistencia estado) {
        String nombre = validarNombre(estudiante);
        if (fecha == null || estado == null) {
            throw new IllegalArgumentException("La fecha y el estado son obligatorios");
        }
        if (buscarIndice(nombre, fecha) >= 0) {
            throw new IllegalStateException("Ya existe un registro de " + nombre + " para " + fecha);
        }
        registros.add(new RegistroAsistencia(nombre, fecha, estado));
    }

    // 2. Corregir un registro que ya existe
    public void corregirAsistencia(String estudiante, LocalDate fecha, EstadoAsistencia nuevoEstado) {
        String nombre = validarNombre(estudiante);
        if (fecha == null || nuevoEstado == null) {
            throw new IllegalArgumentException("La fecha y el estado son obligatorios");
        }
        int indice = buscarIndice(nombre, fecha);
        if (indice < 0) {
            throw new IllegalStateException("No existe un registro de " + nombre + " para " + fecha);
        }
        registros.set(indice, new RegistroAsistencia(nombre, fecha, nuevoEstado));
    }

    // 3. Contar cuántas veces tiene un estudiante un estado
    public int contarPorEstado(String estudiante, EstadoAsistencia estado) {
        if (estado == null) {
            throw new IllegalArgumentException("El estado es obligatorio");
        }
        return (int) registrosDe(estudiante).stream()
                .filter(r -> r.estado() == estado)
                .count();
    }

    // 4. Porcentaje de asistencia (PRESENTE y TARDE suman; JUSTIFICADO no cuenta en su contra)
    public double calcularPorcentajeAsistencia(String estudiante) {
        List<RegistroAsistencia> lista = registrosDe(estudiante);
        long justificadas = lista.stream().filter(r -> r.estado() == EstadoAsistencia.JUSTIFICADO).count();
        long base = lista.size() - justificadas;
        if (base == 0) {
            return 0.0;
        }
        long asistidas = lista.stream().filter(r -> asistio(r.estado())).count();
        return Math.round(asistidas * 10000.0 / base) / 100.0;
    }

    // 5. ¿Cumple el porcentaje mínimo que se le pide?
    public boolean cumpleAsistenciaMinima(String estudiante, double minimo) {
        validarPorcentaje(minimo);
        return calcularPorcentajeAsistencia(estudiante) >= minimo;
    }

    // 6. Mayor número de ausencias seguidas (ordenadas por fecha)
    public int contarAusenciasConsecutivas(String estudiante) {
        int maxima = 0;
        int actual = 0;
        for (RegistroAsistencia r : registrosDe(estudiante)) {
            if (r.estado() == EstadoAsistencia.AUSENTE) {
                actual++;
                maxima = Math.max(maxima, actual);
            } else {
                actual = 0;
            }
        }
        return maxima;
    }

    // 7. ¿Hay que avisar al acudiente por ausencias seguidas?
    public boolean requiereAlertaAcudiente(String estudiante) {
        return contarAusenciasConsecutivas(estudiante) >= LIMITE_AUSENCIAS_CONSECUTIVAS;
    }

    // 8. Estudiantes cuyo porcentaje está por debajo del mínimo (en orden alfabético)
    public List<String> obtenerEstudiantesEnRiesgo(double minimo) {
        validarPorcentaje(minimo);
        TreeSet<String> nombres = new TreeSet<>();
        registros.forEach(r -> nombres.add(r.estudiante()));
        List<String> enRiesgo = new ArrayList<>();
        for (String nombre : nombres) {
            if (calcularPorcentajeAsistencia(nombre) < minimo) {
                enRiesgo.add(nombre);
            }
        }
        return enRiesgo;
    }

    // 9. Cuántos estudiantes asistieron (PRESENTE o TARDE) en una fecha
    public int contarAsistentesEnFecha(LocalDate fecha) {
        if (fecha == null) {
            throw new IllegalArgumentException("La fecha es obligatoria");
        }
        return (int) registros.stream()
                .filter(r -> r.fecha().equals(fecha) && asistio(r.estado()))
                .count();
    }

    // ----- métodos auxiliares privados -----

    private boolean asistio(EstadoAsistencia estado) {
        return estado == EstadoAsistencia.PRESENTE || estado == EstadoAsistencia.TARDE;
    }

    private String validarNombre(String estudiante) {
        if (estudiante == null || estudiante.isBlank()) {
            throw new IllegalArgumentException("El nombre del estudiante es obligatorio");
        }
        return estudiante.trim();
    }

    private void validarPorcentaje(double porcentaje) {
        if (porcentaje < 0 || porcentaje > 100) {
            throw new IllegalArgumentException("El porcentaje debe estar entre 0 y 100");
        }
    }

    private List<RegistroAsistencia> registrosDe(String estudiante) {
        String nombre = validarNombre(estudiante);
        return registros.stream()
                .filter(r -> r.estudiante().equals(nombre))
                .sorted(Comparator.comparing(RegistroAsistencia::fecha))
                .toList();
    }

    private int buscarIndice(String nombre, LocalDate fecha) {
        for (int i = 0; i < registros.size(); i++) {
            RegistroAsistencia r = registros.get(i);
            if (r.estudiante().equals(nombre) && r.fecha().equals(fecha)) {
                return i;
            }
        }
        return -1;
    }
}
