import numpy as np

"""PRIMERO SE INSTALA UN ENTORNO VIRTUAL DE PYTHON
PARA PODER INSTALAR NUMPY, SE PUEDE HACER DE LA SIGUIENTE MANERA:

1. Instalar pip
sudo apt-get install python3-pip

2. Instalar numpy
pip install numpy

3. Crear un entorno virtual de python
python3 -m venv .venv

4. Activar el entorno virtual
source .venv/bin/activate


"""

# Crear un array de 15 elementos y luego cambiar su forma a una matriz de 3x5
a = np.arange(15).reshape(3, 5)

print(a)  # Imprimir la matriz 'a'

# Imprimir la forma de la matriz 'a' (3 filas, 5 columnas)

#Shape es un atributo de la matriz que nos dice cuantas filas y columnas tiene
#En caso de los arreglos nos dice cuantos elementos tiene
print(a.shape)

# Imprimir el número de dimensiones de la matriz 'a' (2 dimensiones)
print(a.ndim)

# Imprimir el nombre del tipo de datos de los elementos en la matriz 'a' (int64)
print(a.dtype.name)

# Imprimir el tamaño en bytes de cada elemento en la matriz 'a' (8 bytes)
print(a.itemsize)

# Imprimir el número total de elementos en la matriz 'a' (15 elementos)
print(a.size)

# Imprimir el tipo de objeto de 'a' (<class 'numpy.ndarray'>)
print(type(a))

# Crear un array con los elementos [6, 7, 8]
b = np.array([6, 7, 8])
print(b)  # Imprimir el array 'b'

# Imprimir el tipo de objeto de 'b' 
print(type(b))

print(a[2,3])  # Imprimir el elemento en la posición (0, 0) de la matriz 'a'


c = np.array([[1, 2, 3, 4], [5, 6, 7 ,8 ], [9, 10, 11, 12]], dtype='int32')
print(c)  # Imprimir la matriz 'c'
print(c[1,3]) # Imprimir el elemento en la posición (1, 3) de la matriz 'c'



"""ARREGLOS DE NUMPY"""
print("-----------------")
# Crear un array de 10 ceros
d = np.zeros(10)
print(d)  

# Crear un array de 10 unos
e = np.ones(10)
print(e)  


# Crear un array vacío de 3 elementos. Los valores iniciales 
# en el array son indefinidos y dependen del estado de la memoria.
f = np.empty(3)
print(f) 

#Rango de elementos en un array
g = np.arange(4)
print(g)  

# Crear un array de 5 elementos que vayan desde 0 a 10
h = np.linspace(0,10,num = 5)
print(h)  

#Crear un arreglo con numeros decimales aleatorios
i = np.random.rand(5,2)
print(i)  

#Crear un arreglo con numeros enteros aleatorios
j = np.random.randint(4,7, size=(3,3))
print(j)

"""SE PUEDE ESPECIFICAR EL TIPO DE DATO CON EL DTYPE = AL TIPO DE DATO, 
AL PASARLO COMO PARAMETRO  """

print("-----------------")
#Devuelve el tamaño en bytes de un solo elemento del array
print(c.itemsize)


cd = np.array([1, 2, 3], dtype=np.int32)

# Imprimir el tamaño en bytes de un solo elemento del array 'cd'
print(cd.itemsize)
# Imprimir el tamaño total en bytes del array 'cd'
print(cd.nbytes)

arr = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(arr)

#Obtener una casilla en especifico
print(arr[1, 5])

#Obtener una fila en especifico
print(arr[0, :])

#Obtener una columna en especifico
print(arr[:, 1])
# Obtener los elementos de la fila 0, desde la columna 1 hasta la 6, de 2 en 2
print(arr[0, 1:6:2])    

"""Es mutable, por lo que se permiten cambios """

#cambiar el valor de una casilla
arr[1,5] = 20
print(arr)
print("\n")
arr[:, 2] = 5
print(arr)


"""3D example"""

array = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(array)

print(array[0,1,1])

#replace a element
array[0,1,1] = 20
print(array)

#repeat an array
arre = np.array([[1,2,3]])
r1 = np.repeat(arre, 3, axis=0)
print(r1)

#Ejercicio con numpy

# Crear un array de unos de tamaño 5x5
ej1 = np.ones((5,5))
print(ej1)

# Crear un array de ceros de tamaño 3x3
z = np.zeros((3,3))
print(z)

# Asignar el valor 9 al elemento central del array 'z'
z[1,1] = 9
print(z)

# Reemplazar el subarray central de 'ej1' con el array 'z'
ej1[1:4,1:4] = z
print(ej1)


"""SEGUIMOS CON MAS FUNCIONES DE NUMPY"""
print("-----------------")
ba = np.ones((2,3))
ab = np.full((3,2), 2)
print(ba)
print(ab)

#Podemos multiplicar el contenido de diferentes arreglos, de diferentes
#dimensiones por medio de la funcion matmul

print(np.matmul(ba, ab))

ejemplos = np.array([[1,2,3],[4,5,6]])
#Existen las funciones min, max, sum, mean, median, std, etc
print(ejemplos)

#La diferencia es que cuando se pasa el parametro axis, se puede especificar
#si se quiere calcular el minimo, maximo, etc, por fila o por columna
#si se pasa de parametro axis = 0, se calcula por columna
#si se pasa de parametro axis = 1, se calcula por fila
print(np.min(ejemplos))
print(np.min(ejemplos,axis=0))
print(np.min(ejemplos,axis=1))

#Suma de todos los elementos
print(np.sum(ejemplos))

"""REORGANIZAR ARREGLOS"""
print("-----------------")
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((4,2))
print(after)


#Stacking arrays

#tiene que coincidir el tamaño para poderlos stackear

print("-----------------")
v1 = np.array([1,2,3,4])
print(v1)
v2 = np.array([5,6,7,8])
print(v2)
#Apilar verticalmente
print(np.vstack([v1,v2]))
#Apilar horizontalmente
print(np.hstack([v1,v2]))

#Indexacion de un array
abc = np.array([1,2,3,4,5,6,7,8,9])
print(abc[[1,2,8]])


"""IMPORTAR INFORMACION DESDE UN ARCHIVO UTILIZANDO NUMPY"""


#Cargar un archivo de texto
print("-----------------")

filedatanumerictxt = np.genfromtxt('datanumeric.txt', delimiter=',')
print(filedatanumerictxt)
print("-----------------")

print(filedatanumerictxt.astype('int32'))
print("-----------------")
#Obtiene los valores que cumplan las condiciones
#Los imprime con True y False
print(filedatanumerictxt>70)

#Imprime los valores en un array que cumplan las condiciones
print(filedatanumerictxt[filedatanumerictxt>70])


#Copiar un array de manera profunda
print("-----------------")
copyfiledata = filedatanumerictxt[filedatanumerictxt.copy()>75]
print(copyfiledata)



#Si intentamos cargar un archivo de texto con datos con caracteres especiales
#Nos dara un error, ya que no puede convertirlos a numeros y lo que sucede es que 
#El error que presenta es que existen mas columnas en una fila que en otra

#filedata = np.genfromtxt('data.txt', delimiter=',')
#print(filedata)

#Para evitar este tipo de errores se recomienda mejor utilizar pandas