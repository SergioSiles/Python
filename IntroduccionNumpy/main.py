import numpy as np
import pandas as pd





#-------------------Pandas-------------------#
#-------------------Series-------------------#
serie1 = pd.Series([1,2,3])
serie1.name = "Primeros"
print(serie1)

#-------------------Dataframes-------------------#
df1 = pd.DataFrame({"columna1": [3,2,5,4,1], "columna2": ["a", "b", "c", "d", "e"], "columna3": ["?", "!", "#", "@", "&"]})
print(df1)

#-------------------Dataframes Fichero CSV-------------------#
df2 = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")

#-------------------Dataframes Numero Elementos------------------#
print(f"\nCabecera de mi DataFrame(5 primeros elementos):\n {df2.head()}")
print(f"\nMi DataFrame tiene {df2.size} celdas")
print(f"\nMi DataFrame tiene {df2.shape} filas y columnas")
print(f"\nPie de mi DataFrame(5 ultimos elementos):\n {df2.tail()}")
print(f"\nEstas son las columnas de mi DataFrame:\n {df2.columns}")

df2.columns=["LargoSepalo", "AnchoSepalo", "LargoPetalo", "AnchoPetalo", "Especie"]
print(f"\nEstas son las columnas renombradas de mi DataFrame:\n {df2.head()}")
print(f"\nDescripcion de mi DataFrame: \n{df2.describe()}")
print(f"\nFiltramos por columa especie: {df2['Especie'].value_counts()}")
print(f"\nMostramos los tipos de datos:\n {df2.dtypes}")
print(f"\nMostramos el tamaño de nuestro DataFrame: {df2.memory_usage().sum()}Kb")
print(f"\nTransponemos las filas y las columnas del DataFrame: {df2.T}")
print(f"\nPonemos nuestro DataFramo en orden descentente: \n{df1.sort_values('columna1', ascending=False)}")
# print(f"\nMostramos una columna completa: \n {df2.index(2)}")
print(df2.notnull())