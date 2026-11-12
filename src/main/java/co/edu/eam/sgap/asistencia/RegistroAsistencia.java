package co.edu.eam.sgap.asistencia;

import java.time.LocalDate;

/** Un registro de asistencia: qué estudiante, en qué fecha y con qué estado. */
public record RegistroAsistencia(String estudiante, LocalDate fecha, EstadoAsistencia estado) {
}
