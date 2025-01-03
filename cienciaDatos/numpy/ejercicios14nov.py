import numpy as np


#Chapter 1.6 Using a random method
#Numeros aleatorios entre el (0,1) Distribucion uniforme se le conoce cuando se generan numeros aleatorios     
arr = np.random.rand(5)
print(arr)
print()

# Generar una matriz de 3x4 con números aleatorios entre 0 y 1
arr = np.random.rand(3,4)
print(arr)
print()

#Esta genera nueros aleatorios con una distribución normal pegados al cero 
arr = np.random.randn(6)
print(arr)
print()

#Genera numeros aleatrios del 0 al 10 generara 5 numeros aleatorios
arr = np.random.randint(0,11,(3,4))
print(arr)
print()

arr = np.array([[2,8,-3],
                [3,-1,0],
                [2,5,2],
               [1,3,4]])

# Cambiar la forma de la matriz a 3x4
r = arr.reshape(3,4)
print(r)
print()

#Crear un arreglo de numpy de los numeros 5,10,15,20
arreglo = np.array([5,10,15,20])
print(arreglo)
print()

#Genera un arreglo con valores  desde 0 hasta 9
arreglo = np.arange(10)
print(arreglo)
print()
#crea un arreglo de tamaño 5 lleno de 1s
arreglo = np.ones(5)
print(arreglo)
print()

#Genera una matriz de ceros de tamaño 3 * 3
arreglo = np.zeros((3,3))
print(arreglo)
print()

#Crea una matriz identidad de 4 * 4
arreglo = np.eye(4)
print(arreglo)
print()

#Crea una matriz de 2 * 2 convalores aleatorios de una distribucion de desviacion estandar  1
arreglo = np.random.randn(2,2)
print(arreglo)
print()

#crea un arreglo con 3 enteros aleatorios entre 1 y 10
arreglo = np.random.randint(1,10,3)
print(arreglo)
print()

#Array indexing and slicing
arr = np.arange(1,11)
print(arr)
print()

# Obtener el valor en la posición 3
print(arr[3])
print()
#Buscar en un arreglo mediante el index entre cierto rango de números
print(arr[2:7])
print()
#Seleccionar del 0 al 5 
print(arr[:5])
print()

#Seleccionar hasta el ultimo valor en un arreglo
print(arr[5:])
print()

#Convertir arreglos en una sola matriz
row1 = [1,2,3]
row2 = [4,5,6]
row3 = [7,8,9]

arr = np.array([row1,row2,row3])
print(arr)
print()

#Filas-Columnas
print(arr[:2,:3])
print()

#Mostrar solo ciertas columnas
print(arr[:2,:2])
print()

#Que aparezcan las ultimas dos filas 
print(arr[1:3])
print()

#Que aparezcan solo 5,6,8,9
print(arr[1:3,1:3])
print()



lista = [10,20,30,40,50]
# Calcular la raíz cuadrada
arr = np.sqrt(lista)
print(arr)
print()

# Calcular el cuadrado de cada elemento
arr = np.square(lista)
print(arr)
print()

# Calcular el logaritmo base 10 de cada elemento
arr = np.log10(lista)
print(arr)
print()

# Calcular el logaritmo natural (base e) de cada elemento
arr = np.log(lista)
print(arr)
print()

# Calcular la exponencial (e^x) de cada elemento
arr = np.exp(lista)
print(arr)
print()

# Calcular el seno de cada elemento
arr = np.sin(lista)
print(arr)
print()

# Calcular el coseno de cada elemento
arr = np.cos(lista)
print(arr)
print()


#1
A = np.eye(3)
print(A)
print()

#2
V = np.random.randn(3)
print(V)
print()

mult = A * V
print(mult)
print()

#3
C = np.ones([3,4])
print(C)
print()

D = np.random.randint(1,51,[4,3])
print(D)
print()

