#Podemos utilizar gráficos de barras apiladas 
# para visualizar la relación entre dos variables categóricas.

#Los dos siguientes gráficos de barras 
# muestran la relación entre isla y especie,
# específicamente, visualizan la distribución de especies dentro de cada isla.

from lets_plot import * #importo libreria
from palmerpenguins import load_penguins # de libreria extraigo la data
LetsPlot.setup_html()# autorizo a que me muestre la data
penguins = load_penguins()#creo variable pinguinos
penguins #muestro a los pinguienos
#PRIMER GRAFICO:
(ggplot(penguins, aes(x="island", fill="species")) + geom_bar())
#Se muestra las frecuencias de cada especie de pingüinos 
# en cada isla. 
# El gráfico de frecuencias muestra 
# que hay el mismo número de pingüinos Adelia en cada isla.

#SEGUNDO GRAFICO:
#El segundo gráfico es un gráfico de frecuencia 
# relativa, creado al establecer 
# la posición = "fill" en el geom. 
# Es más útil para comparar la distribución de especies 
# entre islas, ya que no se ve afectado por la 
# desigualdad en el número de pingüinos.
# Con este gráfico, podemos ver que los pingüinos papúa 
# viven en la isla Biscoe y representan 
# aproximadamente el 75 % de los pingüinos de esa isla; 
# los pingüinos barbijo viven en la isla Dream y 
# representan aproximadamente el 50 % de los pingüinos de esa isla; 
# y los pingüinos Adelia viven en las tres islas 
# y constituyen todos los pingüinos de Torgersen.

(ggplot(penguins, aes(x="island", fill="species")) + geom_bar(position="fill"))
#Al crear estos gráficos de barras, 
# asignamos la variable que se separará en barras 
# a la estética x, y la variable que cambiará 
# los colores dentro de las barras a la estética de
#  relleno.

#TERCER GRAFICO