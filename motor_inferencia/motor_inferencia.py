"""Motor de inferencia mediante encadenamiento hacia adelante."""


def evaluar_sistema_experto(hechos_iniciales, base_reglas):
    """
    Ejecuta las reglas aplicables hasta alcanzar un punto fijo.

    Retorna la base de hechos resultante, las reglas activadas y
    las recomendaciones generadas.
    """
    hechos = hechos_iniciales.copy()
    reglas_activadas = []
    recomendaciones = []
    reglas_ejecutadas = set()

    hubo_inferencia = True

    while hubo_inferencia:
        hubo_inferencia = False

        for regla in base_reglas:
            regla_id = regla["id"]

            if regla_id in reglas_ejecutadas:
                continue

            condiciones_cumplidas = all(
                nombre_hecho in hechos
                and hechos[nombre_hecho] == valor_esperado
                for nombre_hecho, valor_esperado
                in regla["condiciones"].items()
            )

            if not condiciones_cumplidas:
                continue

            reglas_ejecutadas.add(regla_id)
            reglas_activadas.append(regla_id)
            recomendaciones.append({
                "regla": regla_id,
                "nombre": regla["nombre"],
                "texto": regla["recomendacion"],
            })

            for nombre_hecho, valor in regla["conclusiones"].items():
                if nombre_hecho not in hechos:
                    hechos[nombre_hecho] = valor
                    hubo_inferencia = True

    return hechos, reglas_activadas, recomendaciones
