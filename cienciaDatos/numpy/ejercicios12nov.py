import numpy as np 
# Clase 12 nov 2025

# Matriz transpuesta, las filas se convierten en columnas y las columnas en filas

# Ejercicio 1
A_matriz12nov = np.array([[1, 2, 3], 
                     [4, 5, 6], 
                     [7, 8, 9]])

B_matriz12nov = np.array([[-8, 3, 4],
                     [-9, 7, -5],
                     [15, -3, 0]])

print("\nEjercicio 1: \n")
# B * A(transpuesta)
A_matriz_transpuesta = A_matriz12nov.T
print(A_matriz_transpuesta)
print()

C_matriz1 = B_matriz12nov.dot(A_matriz_transpuesta)
print(C_matriz1)
print()

print("--------------------------")
# Clase
lista = [2, 4, 6, 8, 10]
#Se puede realizar lo siguiente
#lista * 2
print(lista)
print()


vector = np.array(lista)
print(vector)
print() 
vector * 2
print(vector)
print()

lista1 = [2, 4, 6]
lista2 = [10, 12, 14]
lista3 = [2, 5, 8]

matrizA = np.array([lista1, lista2, lista3])
print(matrizA)
print()

# Tipo de dato
print(type(matrizA))
print()

# Dimensiones
print(matrizA.shape)
print()

# Matriz A : 3x2
A_matriz = np.array([[-2, 3], 
                     [-5, 1], 
                     [0, -6]])
print(A_matriz)
print()
# Matriz B : 2x3
B_matriz = np.array([[1, -5, 0], 
                     [-8, 9, 2]])
print(B_matriz)
print()

print(matrizA.shape)
print()

print(B_matriz.shape)
print()

# Para la multiplicacion se utiliza el metodo dot o el operador @
C_matriz1 = A_matriz.dot(B_matriz)
print(C_matriz1)
print()
