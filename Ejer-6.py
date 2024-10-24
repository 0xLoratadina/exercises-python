# SUBRUTINA PRINCIPAL
def main():  # void
    # Solicitamos el tamaño del arreglo
    N = int(input("Ingrese el número de filas (y columnas) para la matriz N×N: "))  # int

    # Inicializamos el arreglo bidimensional NxN
    matriz = []  # arr bi int
    inicializarMatriz(matriz, N)

    # Solicitamos los datos por consola para llenar la matriz
    leerMatriz(matriz, N)

    # Mostramos la matriz
    print("\nMatriz ingresada:")
    mostrarMatriz(matriz, N)

    # Calculamos la suma de la diagonal principal
    sumaDiagonal = sumarDiagonalPrincipal(matriz, N)

    # Calculamos la suma de la triangular superior
    sumaTriangularSuperior = sumarTriangularSuperior(matriz, N)

    # Calculamos la suma de la triangular inferior
    sumaTriangularInferior = sumarTriangularInferior(matriz, N)

    # Calculamos el resultado final
    resultado = sumaDiagonal + sumaTriangularSuperior - sumaTriangularInferior

    # Mostramos el resultado final
    print(f"\nResultado de la operación: {sumaDiagonal} (Diagonal Principal) + {sumaTriangularSuperior} (Triangular Superior) - {sumaTriangularInferior} (Triangular Inferior) = {resultado}")

    return

# SUBRUTINA: Inicializar la matriz con ceros
def inicializarMatriz(matriz, N):  # void modificador
    for i in range(N):
        matriz.append([0] * N)  # Inicializamos con ceros

# SUBRUTINA: Leer la matriz desde consola
def leerMatriz(matriz, N):  # void modificador
    for i in range(N):
        for j in range(N):
            matriz[i][j] = int(input(f"Ingrese el valor para la posición [{i+1},{j+1}]: "))

# SUBRUTINA: Mostrar la matriz
def mostrarMatriz(matriz, N):  # void
    for i in range(N):
        for j in range(N):
            print(f"{matriz[i][j]:4}", end=" ")
        print()  # Salto de línea

# SUBRUTINA: Sumar los elementos de la diagonal principal
def sumarDiagonalPrincipal(matriz, N):  # int
    suma = 0  # int
    for i in range(N):
        suma += matriz[i][i]  # Sumamos los elementos de la diagonal principal
    return suma

# SUBRUTINA: Sumar los elementos de la triangular superior
def sumarTriangularSuperior(matriz, N):  # int
    suma = 0  # int
    for i in range(N):
        for j in range(i+1, N):  # Solo los elementos por encima de la diagonal principal
            suma += matriz[i][j]
    return suma

# SUBRUTINA: Sumar los elementos de la triangular inferior
def sumarTriangularInferior(matriz, N):  # int
    suma = 0  # int
    for i in range(1, N):  # Comenzamos desde la fila 1 (debajo de la diagonal)
        for j in range(i):
            suma += matriz[i][j]
    return suma

main()
