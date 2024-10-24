# SUBRUTINA PRINCIPAL
def main():  # void
    # Declaramos el arreglo bidimensional
    m = 4  # número de filas
    n = 4  # número de columnas
    arrBi = [[1, 22, 40, 55], 
             [2, 23, 41, 56], 
             [3, 24, 42, 57], 
             [4, 25, 43, 58]]  # arr bi int

    # Mostrar el arreglo original
    print("Arreglo Original:")
    mostrarArreglo(arrBi, m, n)

    # Solicitar las filas a intercambiar
    fila1 = int(input("Ingrese el índice de la primera fila a intercambiar (0 a 3): "))  # int
    fila2 = int(input("Ingrese el índice de la segunda fila a intercambiar (0 a 3): "))  # int

    # Validamos si los índices de las filas son correctos
    if not validarFilas(fila1, fila2, m):
        print("Índices de fila incorrectos. Fin del programa.")
        return

    # Intercambiar las filas
    intercambiarFilas(arrBi, fila1, fila2)

    # Mostrar el arreglo modificado
    print("\nArreglo Modificado:")
    mostrarArreglo(arrBi, m, n)

    return

# SUBRUTINA: Validar si los índices de las filas son correctos
def validarFilas(f1, f2, m):  # bool
    if f1 < 0 or f1 >= m or f2 < 0 or f2 >= m:
        return False
    return True

# SUBRUTINA: Intercambiar las filas del arreglo bidimensional
def intercambiarFilas(arr, f1, f2):  # void modificador
    arr[f1], arr[f2] = arr[f2], arr[f1]  # Intercambiar las filas

# SUBRUTINA: Mostrar el arreglo bidimensional
def mostrarArreglo(arr, m, n):  # void
    for i in range(m):
        for j in range(n):
            print("{:4}".format(arr[i][j]), end=" ")
        print() 

main()
