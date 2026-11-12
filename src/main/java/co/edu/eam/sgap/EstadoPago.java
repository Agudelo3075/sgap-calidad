package co.edu.eam.sgap;

/** Estado de una mensualidad respecto a su fecha de vencimiento. */
public enum EstadoPago {
    AL_DIA,      // Aún falta tiempo para el vencimiento
    POR_VENCER,  // Faltan pocos días (o vence hoy): se debe avisar al acudiente
    EN_MORA      // La fecha de vencimiento ya pasó
}
