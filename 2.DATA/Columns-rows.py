##With all of these different ways to access values in data frames, it can get confusing. 
# These are the different ways to get the first column of a data frame 
# (when that first column is called column and the data frame is df):

#df.column
#df["column"]
#df.loc[:, "column"]
#df.iloc[:, 0]

#Note that : means ‘give me everything’! The ways to access rows are similar 
# (here assuming the first row is called row):
#df.loc["row", :]
#df.iloc[0, :]

#And to access the first value (ie the value in first row, first column):
#df.column[0]
#df["column"][0]
#df.iloc[0, 0]
#df.loc["row", "column"]

#En los ejemplos anteriores, los corchetes indican dónde extraer bits de la trama de datos. 
# Son como un sistema de direcciones para los valores dentro de una trama de datos. 
# Sin embargo, los corchetes también indican listas. Por lo tanto, si desea seleccionar
#  varias columnas o filas, podría encontrar una sintaxis como esta.

#df.loc[["row0", "row1"], ["column0", "column2"]]

#which picks out two rows and two columns via the lists ["row0", "row1"] 
# and ["column0", "column2"]. Because there are lists alongside the usual system of selecting values, there are two sets of square brackets.
#Dado que junto al sistema habitual de selección de valores hay listas, hay dos conjuntos de corchetes.
#Si solo desea recordar una sintaxis para acceder a filas y columnas por nombre, 
# utilice el patrón df.loc[["fila0", "fila1", ...], ["col0", "col1", ...]]. 
# Esto también funciona con una sola fila o una sola columna (o ambas).
