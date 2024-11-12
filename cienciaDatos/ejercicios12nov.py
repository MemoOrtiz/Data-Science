import numpy as np 
# Clase 12 nov 2025

# Matriz transpuesta, las filas se convierten en columnas y las columnas en filas

# Ejercicio 1
A_matriz = np.array([[1, 2, 3], 
                     [4, 5, 6], 
                     [7, 8, 9]])

B_matriz = np.array([[-8, 3, 4],
                     [-9, 7, -5],
                     [15, -3, 0]])

print("\nEjercicio 1: \n")
# B * A(transpuesta)
A_matriz_transpuesta = A_matriz.T
print(A_matriz_transpuesta)
print()

C_matriz1 = B_matriz.dot(A_matriz_transpuesta)
print(C_matriz1)
print()

# Clase
lista = [2, 4, 6, 8, 10]
lista * 2
print(lista)
print()

