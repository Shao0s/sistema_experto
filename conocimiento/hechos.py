
"""Gestión de los hechos iniciales del sistema experto."""


def obtener_hechos_iniciales(respuestas_usuario=None):
    """
    Construye la base de hechos iniciales a partir de las respuestas.

    Los hechos sin respuesta no se agregan a la base de conocimiento.
    """
    if respuestas_usuario is None:
        return {}

    hechos = {}

    for identificador, valor in respuestas_usuario.items():
        if valor is not None:
            hechos[identificador] = valor

    return hechos
