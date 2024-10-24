import random

# SUBRUTINA PRINCIPAL
def main():  # void
    # Declaramos las variables y arreglos
    n = 20  # int
    arrNumeros = []  # arr uni int
    arrModificado = []  # arr uni int

    # Inicialización de los arreglos
    inicializarArreglo(arrNumeros, n)
    inicializarArreglo(arrModificado, n)

    # Generamos números aleatorios
    generarNumeros(arrNumeros, n)
    
    # Mostramos el arreglo original
    print("\nArray Original: ", arrNumeros)
    
    # Validamos y modificamos el arreglo para que cumpla la condición
    while not validarSuma(arrNumeros, n):
        generarNumeros(arrNumeros, n)
    
    # Copiamos los valores modificados
    copiarArreglo(arrNumeros, arrModificado, n)

    # Mostramos el resultado
    print("\nArray Modificado: ", arrModificado)

    return

# SUBRUTINA: Inicializar un arreglo con ceros
def inicializarArreglo(arr, n):  # void modificador
    for i in range(n):
        arr.append(0)

# SUBRUTINA: Generar números aleatorios en el arreglo
def generarNumeros(arr, n):  # void modificador
    for i in range(n):
        arr[i] = random.randint(1, 100)  # Generamos números entre 1 y 100

# SUBRUTINA: Validar que la suma de los primeros 10 sea mayor que la de los últimos 10
def validarSuma(arr, n):  # bool
    sumaPrimeraMitad = sum(arr[:10])  # Sumamos los primeros 10 elementos
    sumaSegundaMitad = sum(arr[10:])  # Sumamos los últimos 10 elementos

    return sumaPrimeraMitad > sumaSegundaMitad

# SUBRUTINA: Copiar los elementos de un arreglo a otro
def copiarArreglo(arrOrigen, arrDestino, n):  # void modificador
    for i in range(n):
        arrDestino[i] = arrOrigen[i]

main()
