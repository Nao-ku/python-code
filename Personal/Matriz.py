#Declarar una matriz
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#sintaxis 2
matriz2 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
#Recorrer la matriz
for fila in matriz1:
    for elementos in fila:
        print(f"elementos matriz:{elementos},{fila}") #Imprimir los elementos en la misma linea

#Tamaño matriz
f = len(matriz1)
print(f"tamaño filas: {f}")
c = len(matriz1[2])
print(f"tamaño columnas: {c}")

#Recorrer matriz con rango
for i in range(f):
    for j in range(c):
        print(f"Posicion{i},{j}: {matriz1 [i][j]}")

print(matriz1[2][1])

