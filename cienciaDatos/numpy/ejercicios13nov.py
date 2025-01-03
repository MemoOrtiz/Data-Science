import numpy as np

vector = np.array([1, 2, 3, 4, 5])
print(vector)
print()

matriz = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
print(matriz)
print()

matrizT = matriz.T
print(matrizT)
print()

# 1.2 Using arange method
print("1.2 Using arange method")
print()
# Para realizar vectores con cierto rango

vector = np.arange(1, 6)
print(vector)
print()

# Realiza un arreglo de 1 a 100
arr = np.arange(1,100)
print(arr)
print()

# Realiza un arreglo del 1-100 con saltos de 2
arr = np.arange(1,100,2)
print(arr)
print()

# 1.3 Using ones method"
print("1.3 Using ones method")
print()

# Crear un vector de 5 elementos con valor 1
vector = np.ones(5)
print(vector)
print()

# Crear una matriz de 3x4 con valor 1
matriz = np.ones((3,4))
print(matriz)
print()

# 1.4 Using zeros method
print("1.4 Using zeros method")
print()

# Crear un vector de 5 elementos con valor 0
vector = np.zeros(5)
print(vector)
print()

# Crear una matriz de 3x3 con valor 0
matriz = np.zeros((3,3))
print(matriz)
print()

# 1.5 Using eye method - matriz identidad
print("1.5 Using eye method")
print()

# Crear una matriz identidad de 3x3
matriz = np.eye(5)
print(matriz)
print()

#Ejercicio 1

A = np.array([[2, 8, -3],
              [3, -1, 0],
              [-1, 1, 2]])

B = np.array([[4, 0],
              [3, 5],
              [1, 4]])

C = np.array([[2, 5, 3],
              [1, -2, 0]])

D = np.array([[8, 3, 0],
              [7, -1, 3],
              [0, -1, 0]])

# U = (6B).C + A(t)

U = (6 * B).dot(C) + A.T
print(U)
print()
print("--------------------")

# Comprobacion de la operacion
A1 = B.dot(6)
print(A1)
print()

A2 = A1.dot(C)
print(A2)
print()

A3 = A.T
print(A3)
print()

U = A2 + A3
print(U)
print()


# Ejercicio 2

A = np.array([[1, 2, 3],
              [-2, 0 ,1],
              [1, 1, 1]])

B = np.array([[3, 5, 0],
              [0, -1, -2],
              [-3, 4, 10]])

C = np.array([[1, 0, 1],
              [0, -1, 0],
              [-1, -1, -1]])

# Determina : 
# A) A - 2B
# B) 2A -B + 2C
print("Ejercicio 2\n Inciso A")
print()

ejercicio_A = A - (2 * B)
print(ejercicio_A)
print()

# Comprobacion
A1 = 2 * B
print(A1)
print()

A2 = A - A1
print(A2)
print()

print("--------------------")
print()
print("Ejercicio 2\n Inciso B")
print()
ejercicio_B = (2 * A) - B + (2 * C)
print(ejercicio_B)
print()

# Comprobacion
A1 = 2 * A
print(A1)
print()

A2 = A1 - B
print(A2)
print()

A3 = 2 * C
print(A3)
print()

A4 = A2 + A3
print(A4)
print()
