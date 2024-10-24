# SUBRUTINA PRINCIPAL
def main():  # void
    # Declaramos el arreglo bidimensional para los votos
    votos = [
        [194, 48, 206, 45],  # Distrito 1
        [180, 20, 320, 16],  # Distrito 2
        [221, 90, 140, 20],  # Distrito 3
        [432, 50, 821, 14],  # Distrito 4
        [820, 61, 946, 18]   # Distrito 5
    ]  # arr bi int

    candidatos = ["Candidato A", "Candidato B", "Candidato C", "Candidato D"]  # arr uni str
    n_distritos = 5  # int
    n_candidatos = 4  # int

    # Mostrar la tabla original con las cabeceras
    imprimirTabla(votos, candidatos, n_distritos, n_candidatos)

    # Calcular el total de votos por candidato
    totalVotos, totalGeneral = calcularTotales(votos, n_distritos, n_candidatos)

    # Mostrar el total de votos y porcentajes
    imprimirResultados(totalVotos, totalGeneral, candidatos)

    # Determinar si hay un ganador o si se pasa a la segunda ronda
    determinarGanador(totalVotos, totalGeneral, candidatos)

    return

# SUBRUTINA: Imprimir la tabla de votos con cabeceras
def imprimirTabla(votos, candidatos, n_distritos, n_candidatos):  # void
    print("Distrito", end=" ")
    for candidato in candidatos:
        print(f"{candidato}", end="    ")
    print()  # Nueva línea

    for i in range(n_distritos):
        print(f"{i+1:7}", end=" ")  # Imprimir número de distrito
        for j in range(n_candidatos):
            print(f"{votos[i][j]:10}", end=" ")  # Imprimir votos
        print()  # Nueva línea

# SUBRUTINA: Calcular el total de votos por candidato
def calcularTotales(votos, n_distritos, n_candidatos):  # arr uni int, int
    totalVotos = [0] * n_candidatos  # Inicializamos el arreglo unidimensional

    totalGeneral = 0  # int, total de votos emitidos
    for j in range(n_candidatos):
        for i in range(n_distritos):
            totalVotos[j] += votos[i][j]  # Sumamos los votos por candidato
        totalGeneral += totalVotos[j]  # Sumar al total general

    return totalVotos, totalGeneral

# SUBRUTINA: Imprimir el total de votos y el porcentaje de cada candidato
def imprimirResultados(totalVotos, totalGeneral, candidatos):  # void
    print("\nResultados totales:")
    for i in range(len(candidatos)):
        porcentaje = (totalVotos[i] / totalGeneral) * 100  # Calculamos el porcentaje
        print(f"{candidatos[i]}: {totalVotos[i]} votos ({porcentaje:.2f}%)")

# SUBRUTINA: Determinar si hay un ganador o se pasa a la segunda ronda
def determinarGanador(totalVotos, totalGeneral, candidatos):  # void
    maxVotos = max(totalVotos)  # Obtener el máximo número de votos
    ganador = totalVotos.index(maxVotos)  # Índice del candidato más votado

    # Verificamos si el ganador tiene más del 50%
    if (totalVotos[ganador] / totalGeneral) * 100 > 50:
        print(f"\n{candidatos[ganador]} ha ganado con más del 50% de los votos.")
    else:
        # Encontrar los dos candidatos más votados para la segunda ronda
        sorted_indices = sorted(range(len(totalVotos)), key=lambda k: totalVotos[k], reverse=True)
        print(f"\nNingún candidato ha obtenido más del 50% de los votos.")
        print(f"Los candidatos que pasan a la segunda ronda son {candidatos[sorted_indices[0]]} y {candidatos[sorted_indices[1]]}.")

main()
