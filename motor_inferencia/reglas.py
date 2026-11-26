
"""Base de conocimiento: reglas de producción del sistema experto."""

REGLAS = [
    # A1. PRIORIZACIÓN
    {
        "id": "R1",
        "nombre": "Detección de necesidad de priorización",
        "condiciones": {
            "tiene_multiples_tareas": True,
            "existen_tareas_urgentes_e_importantes": True,
            "tiene_dificultades_priorizacion": True,
        },
        "conclusiones": {"requiere_priorizacion": True},
        "recomendacion": (
            "Organiza tus tareas según su urgencia e importancia "
            "para identificar cuáles requieren atención primero."
        ),
    },
    {
        "id": "R2",
        "nombre": "Aplicación de la matriz de Eisenhower",
        "condiciones": {"requiere_priorizacion": True},
        "conclusiones": {"requiere_matriz_eisenhower": True},
        "recomendacion": (
            "Utiliza la matriz de Eisenhower para clasificar tus actividades "
            "en cuatro categorías: hacer, programar, delegar y eliminar."
        ),
    },

    # A2. ORGANIZACIÓN
    {
        "id": "R3",
        "nombre": "Planificación de actividades",
        "condiciones": {"planifica_actividades_diarias": False},
        "conclusiones": {"requiere_planificacion": True},
        "recomendacion": (
            "Establece una planificación diaria con las actividades "
            "que necesitas completar."
        ),
    },
    {
        "id": "R4",
        "nombre": "División de tareas",
        "condiciones": {"divide_tareas_grandes": False},
        "conclusiones": {"requiere_division_tareas": True},
        "recomendacion": (
            "Divide las tareas grandes en actividades pequeñas y manejables "
            "para facilitar su ejecución."
        ),
    },
    {
        "id": "R5",
        "nombre": "Definición de objetivos",
        "condiciones": {"tiene_objetivos_definidos": False},
        "conclusiones": {"requiere_definicion_objetivos": True},
        "recomendacion": (
            "Define objetivos claros y específicos para orientar "
            "tus actividades."
        ),
    },

    # A3. GESTIÓN DEL TIEMPO
    {
        "id": "R6",
        "nombre": "Registro del tiempo",
        "condiciones": {"desconoce_uso_tiempo": True},
        "conclusiones": {"requiere_registro_tiempo": True},
        "recomendacion": (
            "Registra el tiempo que dedicas a cada actividad durante "
            "varios días para identificar cómo utilizas tu jornada."
        ),
    },
    {
        "id": "R7",
        "nombre": "Mejora de estimación de duración",
        "condiciones": {"estima_incorrectamente_duracion": True},
        "conclusiones": {"requiere_mejor_estimacion": True},
        "recomendacion": (
            "Estima la duración de tus tareas considerando su complejidad "
            "y agrega un margen para imprevistos."
        ),
    },
    {
        "id": "R8",
        "nombre": "Control de procrastinación",
        "condiciones": {"posponer_actividades_afecta_cumplimiento": True},
        "conclusiones": {"requiere_control_procrastinacion": True},
        "recomendacion": (
            "Divide las actividades que pospones en acciones pequeñas "
            "y establece horarios específicos para realizarlas."
        ),
    },

    # A4. CONCENTRACIÓN
    {
        "id": "R9",
        "nombre": "Control de interrupciones",
        "condiciones": {"sufre_interrupciones_frecuentes": True},
        "conclusiones": {"requiere_control_distracciones": True},
        "recomendacion": (
            "Reduce las interrupciones desactivando notificaciones "
            "y estableciendo periodos de trabajo sin interrupciones."
        ),
    },
    {
        "id": "R10",
        "nombre": "Técnicas de concentración",
        "condiciones": {"se_distrae_facilmente": True},
        "conclusiones": {"requiere_tecnicas_concentracion": True},
        "recomendacion": (
            "Utiliza técnicas de concentración y trabaja en una sola "
            "actividad a la vez."
        ),
    },
    {
        "id": "R11",
        "nombre": "Mejora del enfoque",
        "condiciones": {"tiene_dificultades_concentracion": True},
        "conclusiones": {"requiere_tecnicas_concentracion": True},
        "recomendacion": (
            "Establece periodos de trabajo enfocado y evita cambiar "
            "constantemente entre actividades."
        ),
    },

    # A5. FATIGA Y DESCANSO
    {
        "id": "R12",
        "nombre": "Detección de fatiga mental",
        "condiciones": {"experimenta_fatiga_mental": True},
        "conclusiones": {"requiere_descansos": True},
        "recomendacion": (
            "Incorpora descansos durante tu jornada para permitir "
            "la recuperación mental."
        ),
    },
    {
        "id": "R13",
        "nombre": "Pausas durante la jornada",
        "condiciones": {"trabaja_sin_pausas_suficientes": True},
        "conclusiones": {"requiere_descansos": True},
        "recomendacion": (
            "Programa pausas periódicas entre tus actividades "
            "para evitar jornadas continuas de trabajo."
        ),
    },
    {
        "id": "R14",
        "nombre": "Aplicación de la técnica Pomodoro",
        "condiciones": {
            "experimenta_fatiga_mental": True,
            "trabaja_sin_pausas_suficientes": True,
        },
        "conclusiones": {"requiere_tecnica_pomodoro": True},
        "recomendacion": (
            "Prueba la técnica Pomodoro: trabaja durante 25 minutos "
            "y descansa durante 5 minutos."
        ),
    },
    {
        "id": "R15",
        "nombre": "Distribución de actividades",
        "condiciones": {"disminuye_rendimiento_jornada": True},
        "conclusiones": {"requiere_descansos": True},
        "recomendacion": (
            "Revisa la distribución de tus actividades y alterna "
            "tareas exigentes con otras de menor demanda."
        ),
    },

    # A6. SEGUIMIENTO
    {
        "id": "R16",
        "nombre": "Evaluación diaria",
        "condiciones": {"revisa_cumplimiento_actividades": False},
        "conclusiones": {"requiere_evaluacion_diaria": True},
        "recomendacion": (
            "Al finalizar el día, revisa las actividades completadas "
            "y las que quedaron pendientes."
        ),
    },
    {
        "id": "R17",
        "nombre": "Ajuste por incumplimiento",
        "condiciones": {"incumple_planificacion_frecuentemente": True},
        "conclusiones": {"requiere_ajuste_planificacion": True},
        "recomendacion": (
            "Identifica las causas por las que no cumpliste tu planificación "
            "y reorganiza las actividades pendientes."
        ),
    },
    {
        "id": "R18",
        "nombre": "Adaptación ante imprevistos",
        "condiciones": {"ajusta_planificacion_ante_imprevistos": False},
        "conclusiones": {"requiere_ajuste_planificacion": True},
        "recomendacion": (
            "Reserva tiempo para ajustar tu planificación cuando "
            "surjan imprevistos."
        ),
    },
]
