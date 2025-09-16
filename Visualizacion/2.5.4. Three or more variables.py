#Hasta ahora has aprendido sobre los diagramas de dispersión (creados con geom_point()) 
# y las curvas suaves (creadas con geom_smooth()) 
# Para visualizar la relación entre dos variables numéricas. 
# Un diagrama de dispersión es probablemente el gráfico 
# más utilizado para visualizar la relación entre dos variables numéricas.

from lets_plot import * #importo libreria
from palmerpenguins import load_penguins # de libreria extraigo la data
LetsPlot.setup_html()# autorizo a que me muestre la data
penguins = load_penguins()#creo variable pinguinos
penguins #muestro a los pinguinos

(ggplot(penguins, aes(x="flipper_length_mm", y="body_mass_g")) + geom_point())

#2.5.4. Three or more variables:
#Como ya vimos, podemos incorporar 
# más variables a un gráfico asignándolas a 
# elementos estéticos adicionales.
# Por ejemplo, en el siguiente diagrama de dispersión ()
# los colores de los puntos representan especies y sus formas, islas.


((ggplot(penguins, aes (x="flipper_length_mm", y= "body_mass_g"))
+ geom_point(aes(color= "species", shape= "island")))
)

#Sin embargo, agregar demasiados mapeos estéticos a una trama la hace 
# desordenada y difícil de entender.

#Resulta útil para las variables categóricas
# dividir el gráfico en facetas (también conocidas como múltiplos pequeños), 
# subgráficos que muestran cada uno un subconjunto de los datos.

#Para facetar el gráfico con una sola variable, utilice facet_wrap().
# El primer argumento de facet_wrap() indica 
# a la función qué variable debe tener en los gráficos sucesivos. 
# La variable que se pasa a facet_wrap() debe ser categórica.

((ggplot (penguins, aes(x="flipper_length_mm", y= "body_mass_g"))
  + geom_point (aes(color = "species", shape = "island")))
  + facet_wrap(facets="island")
)