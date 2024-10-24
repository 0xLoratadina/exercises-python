# SUBRUTINA PRINCIPAL
def main():  # void
    # Declaramos el arreglo con valores preinicializados
    arrNumeros = [1, 22, 40, 55, 22, 40, 1, 99, 55, 78]  # arr uni int
    n = len(arrNumeros)  # Número de elementos en el arreglo

    # Mostrar el arreglo original
    print("Arreglo Original: ", arrNumeros)

    # Llamamos a la subrutina que realiza la modificación
    entradasModificadas = sustituirDuplicados(arrNumeros, n)

    # Mostrar el arreglo modificado y el número de entradas modificadas
    print("\nArreglo Modificado: ", arrNumeros)
    print("Número de entradas modificadas: ", entradasModificadas)

    return

# SUBRUTINA: Sustituir los valores duplicados por -5
def sustituirDuplicados(arr, n):  # int
    entradasModificadas = 0  # int
    vistos = []  # arr uni int, para almacenar los números ya vistos

    for i in range(n):
        if arr[i] in vistos:
            arr[i] = -5  # Sustituimos el valor duplicado por -5
            entradasModificadas += 1  # Contamos la modificación
        else:
            vistos.append(arr[i])  # Añadimos el valor al arreglo de vistos

    return entradasModificadas

main()
