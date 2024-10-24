# SUBRUTINA PRINCIPAL
def main():  # void
    # Declaramos el arreglo para almacenar hasta 80 líneas de texto
    maxLineas = 80  # int
    arrTexto = []  # arr uni str
    n = 0  # int, número de líneas a leer

    # Inicializamos el arreglo con espacios vacíos
    inicializarArreglo(arrTexto, maxLineas)

    # Solicitamos la cantidad de líneas a leer
    n = int(input("Ingrese el número de líneas de texto (máximo 80): "))

    # Validamos que el número de líneas sea válido
    if not validarLineas(n, maxLineas):
        print("Número de líneas inválido. Fin del programa.")
        return

    # Leemos el texto y lo almacenamos en el arreglo
    leerTexto(arrTexto, n)

    # Mostramos el texto leído
    print("\nTexto ingresado:")
    mostrarTexto(arrTexto, n)

    return

# SUBRUTINA: Inicializar el arreglo de texto con cadenas vacías
def inicializarArreglo(arr, maxLineas):  # void modificador
    for i in range(maxLineas):
        arr.append("")

# SUBRUTINA: Validar si el número de líneas es correcto
def validarLineas(n, maxLineas):  # bool
    if n < 1 or n > maxLineas:
        return False
    return True

# SUBRUTINA: Leer las líneas de texto y almacenarlas en el arreglo
def leerTexto(arr, n):  # void modificador
    for i in range(n):
        arr[i] = input("Ingrese la línea de texto " + str(i+1) + ": ")

# SUBRUTINA: Mostrar el texto almacenado en el arreglo
def mostrarTexto(arr, n):  # void
    for i in range(n):
        print(arr[i])

main()
