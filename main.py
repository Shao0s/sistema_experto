"""Punto de entrada del sistema experto de productividad personal."""

from conocimiento.hechos import obtener_hechos_iniciales
from motor_inferencia.motor_inferencia import evaluar_sistema_experto
from motor_inferencia.reglas import REGLAS



def mostrar_hechos(titulo, hechos):
    print(f"\n=== {titulo} ===")
    for nombre, valor in hechos.items():
        print(f"- {nombre}: {valor}")


def main():
    hechos_iniciales = obtener_hechos_iniciales()
    mostrar_hechos("HECHOS INICIALES", hechos_iniciales)

    hechos_finales, activadas, diagnostico = evaluar_sistema_experto(
        hechos_iniciales,
        REGLAS,
    )

    print("\n=== REGLAS ACTIVADAS ===")
    if activadas:
        for regla_id in activadas:
            print(f"- {regla_id}")
    else:
        print("No se activó ninguna regla.")

    print("\n=== RECOMENDACIONES ===")
    if diagnostico:
        for numero, resultado in enumerate(diagnostico, 1):
            print(
                f"{numero}. [{resultado['regla']}] "
                f"{resultado['nombre']}: {resultado['texto']}"
            )
    else:
        print("No hay recomendaciones para los hechos proporcionados.")

    mostrar_hechos("BASE DE HECHOS FINAL", hechos_finales)


if __name__ == "__main__":
    main()
