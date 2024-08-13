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

#Se puede copiar desde el repositorio tambien
print("\n")
print("--------------------------------------------")
print("\n")
coffee = pd.read_csv('./data/coffee.csv')

print(coffee.head())
print("\n")
#Diferencias principales entre archivos .csv, .feather y .parquet

# CSV: Formato de texto plano, sin compresión, altamente compatible, pero más lento y con archivos más grandes.
# Parquet: Formato binario columnar, con compresión, rápido para operaciones en columnas, ideal para grandes volúmenes de datos y entornos de Big Data.
# Feather: Formato binario columnar, sin compresión por defecto, muy rápido, ideal para intercambio de datos entre Python y R.

results = pd.read_parquet('./data/RESULTS.parquet')

print(results.head())
print("\n")
#Cargar un archivo Excel

# Cargar un archivo Excel (primera hoja por defecto)
olympics_data = pd.read_excel('./data/olympics-data.xlsx')
print(olympics_data.head())
print("\n")
# Cargar una hoja específica del archivo Excel
olympics_data = pd.read_excel('./data/olympics-data.xlsx', sheet_name='results')
print(olympics_data.head())
print("\n")

bios = pd.read_csv('./data/bios.csv')

#La funcion .to_excel() permite guardar un DataFrame en un archivo Excel


"""
Acceder a datos con pandas
"""



#La funcion sample se utiliza para obtener una muestra aleatoria de filas o columnas de un DataFrame.
print(coffee.sample(10))
print("\n")
#Al establecer un valor para random_state, se fija la semilla del generador de números aleatorios, 
# lo que garantiza que se obtendrán los mismos resultados cada vez que se ejecute el código.
print(coffee.sample(10,random_state=1))
print("\n")
#La funcion loc[#rows,#column]

#si se tiene loc[0] se obtiene la primera fila en forma de serie
print(coffee.loc[0])
print("\n")
#Si se tiene loc[[0,1,2,3]] se obtiene un DataFrame con las filas 0,1,2 y 3
print(coffee.loc[[0,1,2,3]])
print("\n")
#Si se tiene loc[0:3] se obtiene un DataFrame con las filas 0,1,2 y 3
print(coffee.loc[0:3])
print("\n")
#Si se tiene loc[0:3,'Day'] se obtiene una serie con las filas 0,1,2 y 3 y la columna 'Day'
print(coffee.loc[5:8,'Day'])
print("\n")

print(coffee.loc[5:8,'Day':'Units Sold'])
print("\n")

print(coffee.loc[:,'Day':'Units Sold'])
print("\n")

#La funcion iloc es similar a loc pero en lugar de usar etiquetas de filas y columnas, utiliza índices enteros.

print(coffee.iloc[0])
print("\n")

print(coffee.iloc[[0,1,2,3]])
print("\n")

print(coffee.iloc[0:3])
print("\n")

print(coffee.iloc[5:8,0])
print("\n")

print(coffee.iloc[5:8,0:3])
print("\n")

print(coffee.iloc[:,[0,2]])
print("\n")

#Modificar un DataFrame