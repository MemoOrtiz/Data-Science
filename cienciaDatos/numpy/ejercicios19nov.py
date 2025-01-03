import numpy as np

matrizA = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
matrizB = np.array([[10,11,12],
                    [13,14,15],
                    [16,17,18]])

arr = np.dot(matrizA,matrizB)#Multiplicar
print(arr)
print()

#Producto elemento por elemento 
arr2 = np.multiply(matrizA,matrizB)
print(arr2)
print()

# Es lo mismo que el anterior pero con el operador *
arr3 = matrizA * matrizB
print(arr3)
print()

#Matriz inversa
arr = np.linalg.inv(matrizA)
print(arr)
print()

#determinante 
arr = np.linalg.det(matrizA)
print(arr)
print()

#Traza de una matriz(Es la suma de los elementos en diagonal)
matrizA
arr = np.trace(matrizA)
print(arr)
print()

#Suma
arr = np.array([1,2,3,4,5])
suma = np.sum(arr)
print(suma)
print()

#Minimo de todos los elementos de un arreglo
minimo = np.min(arr)
print(minimo)
print()

#Promedio
promedio = np.mean(arr)
print(promedio)
print()

#Desviacion estandar
desv_est = np.std(arr)
print(desv_est)
print()

#Varianza
varianza = np.var(arr)
print(varianza)
print()

#Mediana
media = np.median(arr)
print(media)
print()

#sumar las filas de la matriz A
suma = np.sum(matrizA,axis = 0)
print(suma)
print()

#sumar las columnas de la matriz A
suma = np.sum(matrizA,axis = 1)
print(suma)
print()

#sumar Todos los elementos de la matriz A
suma = np.sum(matrizA)
print(suma)
print()


