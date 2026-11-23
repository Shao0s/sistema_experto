"""Base de conocimiento: reglas de producción del sistema experto."""

REGLAS = [
    {
        "id": "R1",
        "nombre": "Priorización por Matriz de Eisenhower",
        "condiciones": {
            "tiene_multiples_tareas": True,
            "existen_tareas_urgentes_e_importantes": True,
        },
        "conclusiones": {"debe_priorizar_tareas": True},
        "recomendacion": (
            "Aplicar la Matriz de Eisenhower para clasificar las tareas "
            "según su importancia y urgencia."
        ),
    },
    {
        "id": "R2",
        "nombre": "Registro de actividades",
        "condiciones": {"desconoce_uso_tiempo": True},
        "conclusiones": {"requiere_registro_tiempo": True},
        "recomendacion": (
            "Llevar una bitácora diaria durante tres días para identificar "
            "patrones de uso del tiempo."
        ),
    },
    {
        "id": "R3",
        "nombre": "Control de distracciones",
        "condiciones": {"sufre_interrupciones_frecuentes": True},
        "conclusiones": {"requiere_control_distracciones": True},
        "recomendacion": (
            "Reducir las notificaciones y otras distracciones durante "
            "los bloques de trabajo."
        ),
    },
    {
        "id": "R4",
        "nombre": "Técnica Pomodoro",
        "condiciones": {
            "requiere_alta_concentracion": True,
            "fatiga_mental": True,
        },
        "conclusiones": {"se_recomienda_pomodoro": True},
        "recomendacion": (
            "Aplicar la técnica Pomodoro: 25 minutos de trabajo enfocado "
            "y 5 minutos de descanso."
        ),
    },
    {
        "id": "R5",
        "nombre": "Evaluación y ajuste diario",
        "condiciones": {"cumplio_planificacion_diaria": False},
        "conclusiones": {"requiere_ajuste_diario": True},
        "recomendacion": (
            "Analizar los obstáculos de la jornada y reorganizar las tareas "
            "del día siguiente."
        ),
    },
]
