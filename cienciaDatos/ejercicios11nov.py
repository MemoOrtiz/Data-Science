import numpy as np

# Ejercicio 1

# Matriz A : 3x2
A_matriz = np.array([[-2, 3], [-5, 1], [0, -6]])
# Matriz B : 2x3
B_matriz = np.array([[1, -5, 0], [-8, 9, 2]])
C_matriz1 = A_matriz.dot(B_matriz)
print("\nEjercicio 1: \n")
print(C_matriz1)
print()


# Ejercicio 2
# Matriz A : 2x2
A_matriz = np.array([[-5, 3], [4, 7]])
# Matriz B : 2x2
B_matriz = np.array([[9, 0], [2, -5]])
C_matriz2 = A_matriz.dot(B_matriz)
print("Ejercicio 2: \n")
print(C_matriz2)
print()


# Ejercicio 3
# Matriz M : 1x4
M_matriz = np.array([-1,-5,0, -3])
# Matriz N : 4x2
N_matriz = np.array([[1, -3], [1,2], [2, 0], [-1, 1]])
L_matriz3 = M_matriz.dot(N_matriz)
print("Ejercicio 3: \n")
print(L_matriz3)
print()


# Ejercicio 4

A_matriz = np.array([[-5, 10, 0], 
                     [2, 14, 9], 
                     [-6, 3, 8]])

B_matriz = np.array([[-8, 3, 4],
                     [-9, 7, -5],
                     [15, -3, 0]])

C_matriz = np.array([[5, 0 , 2],
                     [-4, 6, 10],
                     [0, -5, 1]])
# inciso A
matriz_inciso_A = A_matriz + B_matriz
print("Ejercicio 4 inciso A: \n")
print(matriz_inciso_A)
print()
# inciso B
matriz_inciso_B = B_matriz + C_matriz
print("Ejercicio 4 inciso B: \n")
print(matriz_inciso_B)
print()
# inciso C
matriz_inciso_C = A_matriz + B_matriz + C_matriz
print("Ejercicio 4 inciso C: \n")
print(matriz_inciso_C)
print()



