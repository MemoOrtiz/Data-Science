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

print(coffee)
print("\n")
#Supongamos que quisiera modificar un dato en la columna Units Sold de la fila 1.
#Se puede aplicar el concepto de rango con : para seleccionar por ejemplo 1:3 para seleccionar las filas 1 y 2 y 3
coffee.loc[1,'Units Sold'] = 10
print(coffee.head())
print("\n")
# Se puede utilizar la función .at[] para modificar un valor específico en un DataFrame.

coffee.at[1,'Units Sold'] = 20

print(coffee.head())
print("\n")

#Se puede utilizar la función .iat[] para modificar un valor específico en un DataFrame utilizando índices enteros.

coffee.iat[1,2] = 30

print(coffee.head())
print("\n")
#Se puede utilizar la funcion sort_values para ordenar un DataFrame por una o más columnas.
print(coffee.sort_values('Units Sold'))
print("\n")
#Por default lo ordena ascendente asi que si quisieramos que se ordenara descendente seria de la sig manera:

print(coffee.sort_values('Units Sold',ascending=False)) 
print("\n")
print(coffee.sort_values(['Coffee Type','Units Sold'],ascending=[True,False]))
print("\n")
#Se puede iterar pero se pierde mucha efiencia de memoria
for index, row in coffee.iterrows():
    print(index)
    print(row['Units Sold'])
    print("\n")

#La funcion drop() permite eliminar filas o columnas de un DataFrame.

#Eliminar una fila
coffee_fila_eliminada = coffee.drop(2,axis=0)
print(coffee_fila_eliminada)
print("\n")
#Eliminar una columna

coffee_columna_eliminada = coffee.drop('Day',axis=1)
print(coffee_columna_eliminada)
print("\n")

#El método rename() se utiliza para cambiar los nombres de las filas o columnas de un DataFrame.

# Renombrar columnas
df_renamed_columns = df.rename(columns={'Day': 'Weekday', 'Units Sold': 'Sales'})
print("\nDataFrame después de renombrar las columnas:")
print(df_renamed_columns)
print("\n")
# Renombrar filas
df_renamed_rows = df.rename(index={0: 'First', 1: 'Second'})
print("\nDataFrame después de renombrar las filas:")
print(df_renamed_rows)
print("\n")
#El método replace() se utiliza para reemplazar valores específicos en un DataFrame.

# Reemplazar valores en una columna
df_replaced_values = df.replace({'Units Sold': {20: 25, 18: 30}})
print("\nDataFrame después de reemplazar valores en la columna 'Units Sold':")
print(df_replaced_values)
print("\n")
# Reemplazar valores en todo el DataFrame
df_replaced_all = df.replace({20: 25, 'Monday': 'Mon'})
print("\nDataFrame después de reemplazar valores en todo el DataFrame:")
print(df_replaced_all)
print("\n")
"""
FILTRADO DE DATOS
"""

print(bios.info())
print("\n")

#filtrar por altura
print(bios.loc[bios['height_cm'] > 215 ])
print("\n")
#filtrar por altura mayor a 215cm  que solo se vean los nombres y altura

print(bios.loc[bios['height_cm'] > 215 , ['name','height_cm']])
print("\n")

#Filtrar por altura mayor a 215cm y que sean de USA
print(bios.loc[(bios['height_cm'] > 215) & (bios['born_country'] == 'USA')])
print("\n")
#filtrar por altura mayor a 215cm  que solo se vean los nombres y altura y que sean de USA
print(bios.loc[(bios['height_cm'] > 215) & (bios['born_country'] == 'USA'), ['name', 'born_country']])
print("\n")

#Filtrar por la columna name que contenga la palabra 'Keith'
print(bios[bios['name'].str.contains('Keith')])
print("\n")

#Utilizaremos regex para filtrar

print(bios[bios['name'].str.contains('keith|patrick', case = False)])
print("\n")


#Para filtrar por born_country que contenga USA, FRA o GBR

print(bios[bios['born_country'].isin(['USA', 'FRA', 'GBR'])])

print("\n")

print(bios[bios['born_country'].isin(['USA', 'FRA', 'GBR']) & (bios['name'].str.contains('Keith'))])
print("\n")
#La funcion query se utiliza para filtrar filas de un DataFrame utilizando una expresión de consulta basada en una cadena. Este método permite
# escribir consultas de una manera similar a SQL, lo que puede hacer que el código sea más legible y conciso.

print(bios.query('born_country == "USA" '))
print("\n")


