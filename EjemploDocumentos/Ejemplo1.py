import math

def longitudVector(lista):
    longitud = 0
    for i in lista:
        longitud = longitud + (i ** 2)
    return math.sqrt(longitud)

print(longitudVector([3, 4]))

def verificarListaMatriz(lista):
    if len(lista) % 2 != 0:
        raise Exception("Error, no es una matriz")
    else:
        print("Si es una matriz")

verificarListaMatriz([1, 2, 3, 4, 5])

def verificarMatriz2(matriz1, matriz2):
    if (len(matriz1) != len(matriz2)):
        raise Exception("Error, matrices no tiene el mismo tamano")
    suma = 0
    m3 = []

    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz1[i])):
            suma = matriz1[i][j] + matriz2[i][j]
            fila_resultado.append(suma)
        m3.append(fila_resultado)

    return m3

m1 = [[0, 1, 2], [3, 4, 5]]
m2 = [[6, 7, 8], [9, 10, 11]]

verificarMatriz2(m1, m2)