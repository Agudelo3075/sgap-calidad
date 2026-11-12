package co.edu.eam.sgap.asistencia;

/** Estado con el que se registra la asistencia de un estudiante a una clase. */
public enum EstadoAsistencia {
    PRESENTE,     // Asistió a tiempo
    TARDE,        // Asistió, pero llegó tarde (cuenta como asistencia)
    AUSENTE,      // No asistió y no presentó excusa
    JUSTIFICADO   // No asistió, pero presentó excusa (no cuenta en su contra)
}
