#4.3. Manipulating Rows in Data Frames
#Creamos data falsa y la usamos

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
df
#creo un dataframe, de rango 6x6, tengo 6 filas y columnas
#indice los pepes/el nombre el ID
# A columnas asigno  "col" por i a todo rango (6)
#tipo de data flotante

#4.3.1. ACCEDIENDO A FILAS
#To access a particular row directly, 
# you can use df.loc['rowname'] or 
# df.loc[['rowname1', 'rowname2']] for two different rows.

df.loc["a"] # roles se inverten, a es columna, 
#y las columnas del dataframe pasan a ser filas
df.loc[["a", "b"]] 

#But you can also access particular rows based on their location in the data frame
# using .iloc. Remember that Python indices begin from zero, 
# so to retrieve the first row you would use .iloc[0]:
df.iloc[0]
#This works for multiple rows too. 
# Let’s grab the first and third rows 
# (in positions 0 and 2) by passing a list of positions
df.iloc[[0,2]]

#4.3.2. Filtrado de filas con consulta
df.query("col6 == 'kiwi' or col6 == 'pineapple'")
#Seleccioná las filas donde la columna col6 sea igual a 'kiwi'
# o donde la columna col6 sea igual a 'pineapple'.
#Para los números, también se puede utilizar los signos mayor que y menor que:
df.query("col0 > 6")

#hay muchas opciones que funcionan con query(): como > (greater than), 
# you can use >= (greater than or equal to), 
# < (less than), <= (less than or equal to), 
# == (equal to), and != (not equal to). 
# ademas podes usar los comandos: and como tambien or para combinar multiples condicones

#ejemplo con vuelos

# Flights that departed on January 1
flights.query("month == 1 and day == 1")
#Tenga en cuenta que la igualdad se prueba con == y no con =, 
# porque este último se utiliza para la asignación.

#4.3.3. Re-arranging Rows/Reorganización de filas
#pandas te lo hace muy facil con la función .sort_values()
#Toma un data frame y un conjunto de nombres de columnas para ordenar.
#Si proporciona más de un nombre de columna, cada columna adicional se usará para 
# deshacer relaciones en los valores de las columnas anteriores. 
# Por ejemplo, el siguiente código ordena por la hora de salida, 
# que se distribuye en cuatro columnas.
flights.sort_values(["year", "month", "day", "dep_time"])
#Obtendrás un DataFrame donde las filas estarán ordenadas
# cronológicamente por año, mes, día y hora de salida.
#Por defecto, el orden es ascendente en todas las columnas (de menor a mayor), para 
# Cambiarlo you can use the argument 
# ascending=False to re-order by a column or columns in descending order. 
# For example, this code shows the most delayed flights:
flights.sort_values("dep_delay", ascending=False)

#Se pueden combinar todas las manipulaciones de filas anteriores 
# para resolver problemas más complejos. Por ejemplo, podríamos buscar 
# los tres destinos principales de los vuelos 
# con mayor retraso en la llegada y 
# que salieron aproximadamente a tiempo:
(
    flights.query("dep_delay <= 10 and dep_delay >= -10")
    .sort_values("arr_delay", ascending=False)
    .iloc[[0, 1, 2]]
)
#La condición dep_delay <= 10 and dep_delay >= -10 significa:
# Tomar solo los vuelos cuya demora de salida (dep_delay) esté entre -10 y +10 minutos.
# vuelos que salieron puntuales o con un retraso/adelanto de hasta 10 minutos.
# .sort_values("arr_delay", ascending=False)
# Ordena ese DataFrame filtrado según la columna arr_delay (demora en llegada).
# ascending=False significa de mayor a menor (los vuelos más retrasados en llegada primero).
# 1. Filtra los vuelos con retraso de salida entre -10 y +10 minutos.
# 2. Ordena esos vuelos por mayor retraso en llegada (arr_delay).
# 3. Devuelve solo las 3 filas más extremas (las 3 con mayor arr_delay).
