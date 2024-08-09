import pandas as pd


print(pd.__version__)

#Crear un dataframe
#Puedes agregar parametros para los datos, columnas e indices
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns= ['A','B','C'], index=['x','y','z'])

print(df)

df.head()
df.tail()
df.columns
df.index
df.values
df.shape

df.info()
