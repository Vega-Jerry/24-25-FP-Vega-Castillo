def buscar_en_matriz(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición (fila, columna) del valor encontrado
    return None  # Retorna None si el valor no se encuentra en la matriz

# Ejemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
valor_a_buscar = 2
resultado = buscar_en_matriz(matriz, valor_a_buscar)
print(f"El valor {valor_a_buscar} se encuentra en la posición: {resultado}")
