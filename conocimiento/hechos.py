"""Definición y creación de la base de hechos iniciales."""


def obtener_hechos_iniciales():
    """Devuelve una copia nueva de los hechos iniciales del usuario."""
    return {
        "desconoce_uso_tiempo": True,
        "tiene_multiples_tareas": True,
        "existen_tareas_urgentes_e_importantes": True,
        "sufre_interrupciones_frecuentes": True,
        "requiere_alta_concentracion": True,
        "fatiga_mental": True,
        "cumplio_planificacion_diaria": False,
    }
