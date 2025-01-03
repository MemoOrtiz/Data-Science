import numpy as np

a = np.array([[5, 6, 9],
             [10, 15, 20],
             [16, 21, 14]])
print(a)
print()
b = np.array([[7, 2, 6],
              [2, 5, 10],
              [1, 1, 1],
              [10, 10, 10]])
print(b)
print()

c = np.arange(2,14)
print(c)
print()

d = c.reshape(3,4)
print(d)
print()

# matriz transpuesta de D
e = d.T
print(e)
print()

#Matriz de puros 1 de orden 3,4
y = np.ones((3,4))
print(y)
print()


v = np.array([1, 2, 3])

# Obtener el valor de X,X = (B.A) + E
x = (b.dot(a)) + e
print(x)
print()

# Obtener el valor de R,R = X.Y
r = np.dot(x,y)
print(r)
print()

# Obtener el valor de S,S = R.v
try:
    s = np.dot(r, v)
    print("Vector S:")
    print(s)
except ValueError as e:
    print("Error al calcular S = R.v:", e)
print()

# Obtenga el valor max, min, la sumatoria, el promedio de la matriz r
"""
maximo = np.max(r)
minimo = np.min(r)
print(maximo)
print(minimo)
print()
"""

print(r.max())
print(r.min())
print(r.sum())
print(r.mean())
print()

# Obtenga el indice del valor maximo y minimo de la matriz r
print(r.argmax())
indice_maximo = np.argmax(r)
coordenadas_maximo = np.unravel_index(indice_maximo, r.shape)
print(coordenadas_maximo)
print(r.argmin())
print()
print()
print()

# Obtener el índice del valor máximo y mínimo de la matriz r
indice_maximo = np.argmax(r)
indice_minimo = np.argmin(r)

# Convertir los índices a coordenadas de la matriz original
coordenadas_maximo = np.unravel_index(indice_maximo, r.shape)
coordenadas_minimo = np.unravel_index(indice_minimo, r.shape)

# Formatear la salida para que aparezca como [fila][columna]
coordenadas_maximo_formateadas = f"[{coordenadas_maximo[0]}][{coordenadas_maximo[1]}]"
coordenadas_minimo_formateadas = f"[{coordenadas_minimo[0]}][{coordenadas_minimo[1]}]"

print(coordenadas_maximo_formateadas)
print(coordenadas_minimo_formateadas)
print()

# Mostrar un rango de la matriz r
print(r[3:,1:2])
print()
print(r[1:2,1:2])
print()

"""
# Generar una matriz de 4x3 con números aleatorios del 1 al 100
ej6 = np.random.randint(1, 101)
ejercicio6 = ej6.reshape(4,3)
print(ejercicio6)
"""
eje6 = np.random.randint(1,101,size=(4,3))
print(eje6)
print()
ejer6 =np.random.randint(1,101,12).reshape(4,3)
print(ejer6)

