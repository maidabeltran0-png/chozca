#4.4.1. Creating New Columns
#vamos a crear nuevas columnas, usando info existente. Dado un dataframe df
#crear una nueva columnas con el mismo valor repetido
#usando corchetes con un string 
import numpy as np
import pandas as pd
url = "https://raw.githubusercontent.com/byuidatascience/data4python4ds/master/data-raw/flights/flights.csv"
flights = pd.read_csv(url)
df = pd.DataFrame(
    data=np.reshape(range(36), (6, 6)),
    index=["a", "b", "c", "d", "e", "f"],
    columns=["col" + str(i) for i in range(6)],
    dtype=float,
)
df["col6"] = ["apple", "orange", "pineapple", "mango", "kiwi", "lemon"]

df["new_column0"] = 5
df
#otra forma es usando .assign()
# see this with an example where we put different values in each position by assigning a list to the new column.
df["new_column0"] = [0, 1, 2, 3, 4, 5]
df
#creando mas columnas, aca uso corchetes dobles
df[["new_column1", "new_column2"]] = [5, 6]
df
#Very often, you will want to create a new column that is the result of 
# an operation on existing columns. 
# There are a couple of ways to do this. 
# One is to use the .assign() method y se utiliza cuando se desean encadenar varios pasos 
# utilizan una sintaxis especial instrucción «lambda», que (al menos en este caso)  proporciona
#  una forma de especificar a Pandas que deseamos realizar la operación en cada fila. 
# tener en cuenta que la palabra «fila» a continuación es ficticia; 
# puede reemplazarla por cualquier nombre de variable (por ejemplo, x), pero «fila» aclara un poco lo que sucede.

(
    flights.assign(
        gain=lambda row: row["dep_delay"] - row["arr_delay"],
        speed=lambda row: row["distance"] / row["air_time"] * 60,
    )
)
#4.4.2. Accessing Columns
# Hay varias formas de acceder a las columnas de un dataframe.
#syntax is the name of the data frame followed by square brackets 
# and the column name (as a string)
df["col0"]
# PARA VARIAS COLUMNAS
df[["col0", "new_column0", "col2"]]

# Si desea acceder a filas particulares al mismo tiempo, use la función de acceso .loc:
df.loc[["a", "b"], ["col0", "new_column0", "col2"]]

#Sometimes, you’ll want to select columns based on the type of data that they hold. 
# For this, pandas provides a function .select_dtypes(). Let’s use this to select 
# all columns with integers in the flights data.
flights.select_dtypes(int)

#Hay otras ocasiones en las que se desea seleccionar columnas según criterios 
# como patrones en el nombre de la columna. Esto no suele estar integrado 
# en las funciones de Pandas. El truco consiste en generar una lista de nombres de 
# columna que se deseen a partir del patrón que se desea.
#Primero, obtendremos todas las columnas de nuestro data frame df que comiencen por 
# "new_...". Generaremos una lista de valores verdaderos y falsos 
# que refleje si cada columna comienza por "new" y luego pasaremos esos valores 
# a .loc, que solo mostrará las columnas cuyo resultado sea verdadero. 
# Para ilustrar el proceso, lo dividiremos en dos pasos:

print("The list of columns:")
print(df.columns)
print("\n")
#Muestra todos los nombres de columnas.

print("The list of true and false values:")
print(df.columns.str.startswith("new"))
print("\n")
#Muestra una lista de valores True y False que 
# indican si el nombre de la columna comienza con "new".

print("The selection from the data frame:")
df.loc[:, df.columns.str.startswith("new")]
#Muestra las columnas que comienzan con "new".

#4.4.3. Renaming Columns
#Para cambiar el nombre de las columnas, use el método .rename().
df.rename(columns={"col0": "new_col0", "col1": "new_col1"})
#Para ello, simplemente configure df.columns igual al nuevo conjunto de columnas que desea tener.
df.columns = df.columns.str.capitalize()
df

# we might be interested in just replacing specific 
# parts of column names. In this case, we can use .str.replace()

df.columns.str.replace("Col", "Original_column")

#4.4.4. Re-ordering Columns
#Para reordenar las columnas, simplemente pase una lista de los nombres de las columnas
# en el orden que desee a .loc.
#you may have reasons to want the columns to appear in a particular order
df = pd.DataFrame(
    data=np.reshape(range(36), (6, 6)),
    index=["a", "b", "c", "d", "e", "f"],
    columns=["col" + str(i) for i in range(6)],
    dtype=float,
)
df

df = df[["col5", "col3", "col1", "col4", "col2", "col0"]]
df
#Existen métodos que pueden facilitarlo según el contexto. 
# ¿Quizás simplemente quieras ordenar las columnas? Esto se puede lograr combinando sorted() 
# y el comando reindex() (que funciona tanto para filas como para columnas) 
# con axis=1, que corresponde al segundo eje (es decir, columnas).

df.reindex(sorted(df.columns), axis=1)
