# UNIVERSIDAD AUTÓNOMA DE CAMPECHE
# Práctica 6 – Modelado de Problemas Aplicados a la Ingeniería Civil
# Tema: Movimiento de Tierras (Corte y Relleno)
# Alumno: Jonathan J. González Cuj
# Matrícula: al069319

def calcular_volumenes(terreno, h_diseno, area_celda):
    """Calcula los volúmenes totales de corte y relleno"""
    corte_total = 0
    relleno_total = 0

    for fila in terreno:
        for h_actual in fila:
            delta_h = h_actual - h_diseno
            volumen = delta_h * area_celda
            if volumen > 0:
                corte_total += volumen
            elif volumen < 0:
                relleno_total += abs(volumen)
    return corte_total, relleno_total


def leer_matriz():
    """Lee la matriz de elevaciones desde texto ingresado por el usuario"""
    print("Introduce las elevaciones del terreno (una fila por línea).")
    print("Ejemplo: 12.5 12.8 13.0")
    print("Cuando termines, escribe 'fin' y presiona Enter.\n")

    terreno = []
    while True:
        linea = input("Fila: ")
        if linea.lower() == "fin":
            break
        try:
            fila = [float(x) for x in linea.split()]
            terreno.append(fila)
        except ValueError:
            print("⚠️ Ingresa solo números separados por espacios.")
    return terreno


def main():
    print("=============================================")
    print(" CÁLCULO DE CORTE Y RELLENO DE UN TERRENO ")
    print("=============================================\n")

    # Leer datos del usuario
    terreno = leer_matriz()
    h_diseno = float(input("\nIntroduce la altura de diseño (m): "))
    area_celda = float(input("Introduce el área de cada celda (m²): "))

    # Calcular volúmenes
    corte, relleno = calcular_volumenes(terreno, h_diseno, area_celda)

    # Mostrar resultados
    print("\n===== RESULTADOS =====")
    print(f"Volumen total de corte: {corte:.2f} m³")
    print(f"Volumen total de relleno: {relleno:.2f} m³")
    print("=======================")
    print("Cálculo completado con éxito.")


# Ejecutar programa
if __name__ == "__main__":
    main()
