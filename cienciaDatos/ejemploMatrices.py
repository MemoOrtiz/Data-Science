import numpy as np

# Crear una matriz 2x4 con los valores proporcionados
matrizA = np.array([[5, 3, -4, -2], [8, -1, 0, -3]])
print(matrizA)
print()
# Crear una matriz 4x3 con los valores proporcionados
matrizB = np.array([[1, 4, 0], [-5, 3, 7], [0, -9, 5], [5, 1, 4]])
print(matrizB)
print()
# Multiplicar las matrices
matrizC = matrizA.dot(matrizB)
print(matrizC)
print()

"""
Al momento de multiplicar matrices funciona de la siguiente manera:
        2 x 4        4 x 3    =  2 x 3
        |   |         |   |         
        |   -----------   |   Signfica que si se puede
        |                 |
        -------------------   Los extremos son las dimensiones de la nueva matriz
"""
# Matriz A
matriz_ejemplo_A = np.array([[-3, 0], [2, 5], [8, -7]])
print(matriz_ejemplo_A)
print()

# Matriz B
matriz_ejemplo_B = np.array([[7, -5], [4, -2], [1, -4]])
print(matriz_ejemplo_B)
print()
"""
Deben de ser del mismo orden ambas matrices


"""

# Sumar las matrices
print("Suma de matrices")
matriz_ejemplo_C = matriz_ejemplo_A + matriz_ejemplo_B
print(matriz_ejemplo_C)
print()

