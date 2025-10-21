#4.6. Grouping, changing the index, and applying summary statistics
#La creación de grupos suele implicar también un cambio de índice. 
# Y dado que los grupos suelen implicar una agregación o agrupación de datos, 
# suelen ir de la mano con la aplicación de una estadística de resumen.

#4.6.1. Grouping and Aggregating
#Veamos cómo crear un grupo con la función .groupby(), seleccionar una 
# columna y aplicar una estadística de resumen mediante una agregación. 
# Tenga en cuenta que la agregación, mediante .agg(), siempre genera un 
# nuevo índice porque hemos reducido la información al nivel de grupo 
#(y el nuevo índice se compone de esos niveles).

#The key point to remember is: use .agg() 
# with .groupby() when you want your groups to become the new index.
import pandas as pd
import numpy as np  
url = "https://raw.githubusercontent.com/byuidatascience/data4python4ds/master/data-raw/flights/flights.csv"
flights = pd.read_csv(url)

(flights.groupby("month")[["dep_delay"]].mean())
#Es un DataFrame donde cada fila es un mes y la columna es el promedio de dep_delay para ese mes.

#Para realizar múltiples agregaciones en múltiples columnas con nuevos 
# nombres para las variables de salida, la sintaxis se convierte en
(
    flights.groupby(["month"]).agg(
        mean_delay=("dep_delay", "mean"),
        count_flights=("dep_delay", "count"),
    )
)
#groupby agrupa los datos del DataFrame según los valores de la columna "month
#agg significa aggregate (agregar). Permite aplicar una o varias funciones estadísticas a las columnas del DataFrame para cada grupo.
#"count" → función que cuenta cuántos valores existen en la columna dep_delay dentro de cada grupo.
# count_flights → nombre de la columna en el resultado final.

#"Agrupo los vuelos por mes y calculo, para cada mes, el retraso promedio y la cantidad total de vuelos."


#4.6.2. Grouping by multiple variables
month_year_delay = flights.groupby(["month", "year"]).agg(
    mean_delay=("dep_delay", "mean"),
    count_flights=("dep_delay", "count"),
)
month_year_delay
#enemos un índice múltiple (es decir, un índice con más de una columna). 
# Esto se debe a que solicitamos un índice con varios grupos, y el índice rastrea 
# lo que sucede dentro de cada grupo; por lo tanto, necesitamos más de una dimensión 
# del índice para hacerlo eficientemente.

month_year_delay.reset_index() #Si alguna vez desea volver a un índice que es solo la posición


#Quizás solo quieras eliminar una capa del índice. Esto se puede lograr indicando 
# la posición del índice que quieres eliminar: por ejemplo, }
# para cambiar solo el índice del año a una columna, usaríamos:
month_year_delay.reset_index(1) #el 1 indica que queremos eliminar la segunda capa del índice (0 es la primera capa).