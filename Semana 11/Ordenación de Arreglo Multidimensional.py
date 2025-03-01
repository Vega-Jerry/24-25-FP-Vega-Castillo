def ordenar_fila(matriz, fila):
    # Verificamos si la fila es válida
    if fila < 0 or fila >= len(matriz):
        return "Fila no válida"

    # Usamos Bubble Sort para ordenar la fila específica
    for i in range(len(matriz[fila])):
        for j in range(0, len(matriz[fila]) - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                # Intercambiamos los elementos
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

    return matriz


# Ejemplo de uso
matriz = [[5, 2, 9], [1, 4, 3], [8, 7, 6]]
fila_a_ordenar = 1
resultado = ordenar_fila(matriz, fila_a_ordenar)
print(resultado)