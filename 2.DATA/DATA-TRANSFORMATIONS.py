#It’s very rare that data arrive in exactly 
#the right form you need. Often, you’ll need 
#to create some new variables or summaries, 
#or maybe you just want to rename the variables 
#or reorder the observations to make the data a 
#little easier to work with.
#Will introduce you to data transformation using the pandas package 
#and a new dataset on flights that departed New York City in 2013.


#Paso 1) Let’s download the data:
import pandas as pd
url = "https://raw.githubusercontent.com/byuidatascience/data4python4ds/master/data-raw/flights/flights.csv"
flights = pd.read_csv(url)
flights.head(25)
#To get more general information on the columns, 
# the data types (dtypes) of the columns, a
# nd the size of the dataset, use .info().
flights.info()

#The different column data types are important because the 
# operations you can perform on a column depend so much on its “type”; 
# for example, you can remove all punctuation from strings while you can multiply ints and floats.

#Vamos a trabajar con variable "time_hour", pandas makes it easy 
# to perform that conversion on that specific column
flights["time_hour"]

flights["time_hour"] = pd.to_datetime(flights["time_hour"], format="%Y-%m-%dT%H:%M:%SZ")

# mas importante del data frames de pandas, es que estan construidos
# alrededor de un indice que esta en el lado izquierdo del data frame
# Every time you perform an operation on a data frame, you need to think about 
# how it might or might not affect the index; or, put another way, whether you want to modify the index.
# Let’simple example of this with a made-up data frame:

df = pd.DataFrame(
    data={
        "col0": [0, 0, 0, 0],
        "col1": [0, 0, 0, 0],
        "col2": [0, 0, 0, 0],
        "col3": ["a", "b", "b", "a"],
        "col4": ["alpha", "gamma", "gamma", "gamma"],
    },
    index=["row" + str(i) for i in range(4)],
)
df.head()

#You can see there are 5 columns (named "col0" to "col4") 
# and that the index consists of four entries named "row0" to "row3".
# CLAVE, las operationes en el data frame de pandas puede funcionanr en cadena
# We need not perform one assignment per line of code; we can actually do multiple assignments in a single command.
# We’re going to string together four operations:

#USAMOS query() to find only the filas where la columna destino "dest" tiene el valor "IAH". 
# This doesn’t change the index, it only removes irrelevant rows. 
# In effect, this step removes rows we’re not interested in.
#query () NO MODIFICA EL INDICE/SOLO REMUEVE FILAS NO RELEVANTES

# groupby() AGREUPA LAS FILAS POR AÑO, MES, Y DIA
# las pasamos a una lista de columnas agrupadas por filas de años, mes y dia.
# ESTO MODIFICA EL INDICE. The new index will have three columns in that track the year, month, and day. 
# Elegiremos las columnas que deseamos conservar después de la operación groupby() 
# pasando una lista de ellas entre corchetes (los corchetes porque se trata de una lista dentro de un data frame).
#  Aquí solo queremos una columna, "arr_delay". Esto no afecta al índice. 
# De hecho, este paso elimina las columnas que no nos interesan.
# Finalmente, debemos especificar qué operación groupby() deseamos aplicar; al agregar la 
# información de varias filas a una sola, debemos indicar cómo se debe agregar esa información. 
# En este caso, usaremos la media(). Este paso aplica un estadístico a la(s) variable(s) seleccionada(s) previamente, 
# en los grupos creados previamente.

(flights.query("dest == 'IAH'").groupby(["year", "month", "day"])[["arr_delay"]].mean())

#We’ve created a new data frame with a new index. 
# To do it, we used four key operations:
# 1. manipulating rows
# 2. manipulating the index
# 3. manipulating columns
# 4. applying statistics