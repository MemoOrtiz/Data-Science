import pandas as pd


print(pd.__version__)

"""
CREAR UN DATAFRAME
"""
#Puedes agregar parametros para los datos, columnas e indices
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns= ['A','B','C'], index=['x','y','z'])

print(df)

# Muestra las primeras 5 filas del DataFrame por defecto.
# Puedes pasar un parámetro opcional para mostrar un número diferente de filas, por ejemplo, df.head(10) para mostrar las primeras 10 filas.
print(df.head())

# Muestra las últimas 5 filas del DataFrame por defecto.
# Similar a .head(), puedes pasar un parámetro opcional para mostrar un número diferente de filas, por ejemplo, df.tail(10) para mostrar las últimas 10 filas.
print(df.tail())

# Muestra las etiquetas de las columnas del DataFrame.
# Esto es útil para ver rápidamente los nombres de las columnas.
print(df.columns)

# Muestra las etiquetas de los índices del DataFrame.
# Esto es útil para ver rápidamente los índices de las filas.
print(df.index)

# Muestra los valores del DataFrame como un array de NumPy.
# Esto puede ser útil para realizar operaciones de bajo nivel en los datos.
print(df.values)

# Muestra la forma del DataFrame (número de filas y columnas).
# Esto es útil para entender rápidamente el tamaño del DataFrame.
print(df.shape)

# Muestra un resumen conciso del DataFrame, incluyendo el tipo de datos de cada columna y el uso de memoria.
# Esto es útil para obtener una visión general rápida de la estructura y el contenido del DataFrame.
print(df.info())

"""
CARGAR UN DATAFRAME DESDE ARCHIVOS
"""