#1. Find all flights that 
# a. Had an arrival delay of two or more hours
# b. Flew to Houston ("IAH" or "HOU")
# c. Were operated by United, American, or Delta
# d. Departed in summer (July, August, and September)
# e. Arrived more than two hours late, but didn’t leave late
# f. Were delayed by at least an hour, but made up over 30 minutes in flight
# 2. Sort flights to find the flights with longest departure delays.
# 3. Sort flights to find the fastest flights
# 4. Which flights traveled the farthest?
# 5. Does it matter what order you used query() and sort_values() 
# in if you’re using both? Why/why not? Think about the results 
# and how much work the functions would have to do.

import numpy as np
import pandas as pd
url = "https://raw.githubusercontent.com/byuidatascience/data4python4ds/master/data-raw/flights/flights.csv"
flights = pd.read_csv(url)

# 1.a. vuelos que hayan tenido retraso de dos o mas horas
(
    flights.query("dep_delay >=120")
)
#“Dame todos los vuelos que salieron con 120 minutos (2 horas) o más de retraso”.

# b. Voló a Houston ("IAH" o "HOU")
flights.query("dest == 'IAH' or dest == 'HOU'")

#1. c. Were operated by United, American, or Delta
#carrier UA o DL
flights.query("carrier == 'UA' or carrier == 'DL'")

#1.d. salida in summer (July, August, and September)
flights.query("month==7 or month == 8 or month ==9"
)
#1.e. Arrived more than two hours late, but didn’t leave late
#llego mas de dos horas tardes, pero despego maso putual 

(flights.query ("dep_time==1 and arr_delay>=120"))

#1.f. Were delayed by at least an hour, but made up over 30 minutes in flight
#Tuvimos un retraso de al menos una hora, pero recuperamos más de 30 minutos en vuelo.
(flights.query("dep_delay>=60 and dep_delay - arr_delay > 30"))

#2. Ordene los vuelos para encontrar los vuelos con 
# mayores retrasos en la salida.
#pandas te lo hace muy facil con la función 
# .sort_values() puedo reodenar filas
flights.sort_values("dep_delay", ascending=False)

#3. Sort flights to find the fastest flights
flights.sort_values("air_time")

#4. ¿Qué vuelos recorrieron más distancia?
flights.sort_values("distance", ascending=False)

#¿Importa el orden en que se usaron query() y 
# sort_values() si se usan ambas? 
# ¿Por qué sí o por qué no? 
# Piensa en los resultados y en cuánto trabajo 
# tendrían que realizar las funciones.
