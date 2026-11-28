"""Pruebas del motor de inferencia mediante Forward Chaining."""

from motor_inferencia.motor_inferencia import evaluar_sistema_experto
from motor_inferencia.reglas import REGLAS


def probar_encadenamiento():
    """Comprueba que R1 genere el hecho necesario para activar R2."""

    hechos = {
        "tiene_multiples_tareas": True,
        "existen_tareas_urgentes_e_importantes": True,
        "tiene_dificultades_priorizacion": True,
    }

    hechos_finales, activadas, recomendaciones = evaluar_sistema_experto(
        hechos,
        REGLAS,
    )

    assert "R1" in activadas
    assert "R2" in activadas
    assert hechos_finales["requiere_priorizacion"] is True
    assert hechos_finales["requiere_matriz_eisenhower"] is True

    print("PRUEBA 1: Encadenamiento R1 -> R2: CORRECTA")


def probar_hechos_desconocidos():
    """Comprueba que los hechos ausentes no se interpreten como False."""

    hechos = {
        "tiene_multiples_tareas": True,
        "existen_tareas_urgentes_e_importantes": True,
    }

    hechos_finales, activadas, recomendaciones = evaluar_sistema_experto(
        hechos,
        REGLAS,
    )

    assert "R1" not in activadas
    assert "requiere_priorizacion" not in hechos_finales

    print("PRUEBA 2: Manejo de hechos desconocidos: CORRECTA")


def probar_ausencia_de_reglas():
    """Comprueba el comportamiento cuando no existen hechos iniciales."""

    hechos_finales, activadas, recomendaciones = evaluar_sistema_experto(
        {},
        REGLAS,
    )

    assert hechos_finales == {}
    assert activadas == []
    assert recomendaciones == []

    print("PRUEBA 3: Ausencia de hechos iniciales: CORRECTA")


def probar_las_18_reglas():
    """Comprueba la activación de las 18 reglas en un escenario completo."""

    hechos = {
        # A1. Priorización
        "tiene_multiples_tareas": True,
        "existen_tareas_urgentes_e_importantes": True,
        "tiene_dificultades_priorizacion": True,

        # A2. Organización
        "planifica_actividades_diarias": False,
        "divide_tareas_grandes": False,
        "tiene_objetivos_definidos": False,

        # A3. Gestión del tiempo
        "desconoce_uso_tiempo": True,
        "estima_incorrectamente_duracion": True,
        "posponer_actividades_afecta_cumplimiento": True,

        # A4. Concentración
        "sufre_interrupciones_frecuentes": True,
        "se_distrae_facilmente": True,
        "tiene_dificultades_concentracion": True,

        # A5. Fatiga
        "experimenta_fatiga_mental": True,
        "trabaja_sin_pausas_suficientes": True,
        "disminuye_rendimiento_jornada": True,

        # A6. Seguimiento
        "revisa_cumplimiento_actividades": False,
        "incumple_planificacion_frecuentemente": True,
        "ajusta_planificacion_ante_imprevistos": False,
    }

    hechos_finales, activadas, recomendaciones = evaluar_sistema_experto(
        hechos,
        REGLAS,
    )

    identificadores_esperados = {
        f"R{i}" for i in range(1, 19)
    }

    assert set(activadas) == identificadores_esperados
    assert len(activadas) == 18
    assert len(recomendaciones) == 18

    print("PRUEBA 4: Activación de las 18 reglas: CORRECTA")
    print("Reglas activadas:", len(activadas))

def probar_reglas_individualmente():
    """Comprueba que cada regla se active al cumplir sus condiciones."""

    for regla in REGLAS:
        hechos = regla["condiciones"].copy()

        hechos_finales, activadas, recomendaciones = evaluar_sistema_experto(
            hechos,
            [regla],
        )

        assert regla["id"] in activadas, (
            f"La regla {regla['id']} no se activó."
        )

        for nombre_hecho, valor in regla["conclusiones"].items():
            assert hechos_finales[nombre_hecho] == valor, (
                f"La conclusión de {regla['id']} es incorrecta."
            )

    print("PRUEBA 5: Activación individual de las 18 reglas: CORRECTA")

def probar_condiciones_no_cumplidas():
    """Comprueba que una regla no se active si sus condiciones son falsas."""

    for regla in REGLAS:
        hechos = {
            nombre_hecho: not valor_esperado
            for nombre_hecho, valor_esperado
            in regla["condiciones"].items()
        }

        hechos_finales, activadas, recomendaciones = evaluar_sistema_experto(
            hechos,
            [regla],
        )

        assert regla["id"] not in activadas, (
            f"La regla {regla['id']} se activó incorrectamente."
        )

        for nombre_hecho in regla["conclusiones"]:
            assert nombre_hecho not in hechos_finales, (
                f"La regla {regla['id']} generó una conclusión incorrectamente."
            )

    print("PRUEBA 6: Condiciones no cumplidas: CORRECTA")

def probar_integridad_hechos_iniciales():
    """Comprueba que el motor conserve intactos los hechos originales."""

    hechos = {
        "tiene_multiples_tareas": True,
        "existen_tareas_urgentes_e_importantes": True,
        "tiene_dificultades_priorizacion": True,
    }

    hechos_originales = hechos.copy()

    hechos_finales, activadas, recomendaciones = evaluar_sistema_experto(
        hechos,
        REGLAS,
    )

    assert hechos == hechos_originales, (
        "El motor modificó los hechos iniciales."
    )

    assert "requiere_priorizacion" in hechos_finales
    assert "requiere_matriz_eisenhower" in hechos_finales

    print("PRUEBA 7: Integridad de los hechos iniciales: CORRECTA")

def main():
    probar_encadenamiento()
    probar_hechos_desconocidos()
    probar_ausencia_de_reglas()
    probar_las_18_reglas()
    probar_reglas_individualmente()
    probar_condiciones_no_cumplidas()
    probar_integridad_hechos_iniciales()

    print("\nTodas las pruebas finalizaron correctamente.")

if __name__ == "__main__":
    main()

