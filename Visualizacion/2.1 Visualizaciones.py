from lets_plot import * #importo libreria
from palmerpenguins import load_penguins # de libreria extraigo la data
LetsPlot.setup_html()# autorizo a que me muestre la data
penguins = load_penguins()#creo variable pinguinos
penguins #muestro a los pinguienos

#EJERCICIO
# Busco mostrar visualmente la relacion entre
#masa corporal y tamaño de alas en un grafico
ggplot(data = penguins) # paso 1. Creating a Plot

#paso 2. ahora tengo que decirle como representar la relación
ggplot(
  data = penguins,
  mapping = aes(x = "flipper_length_mm", y = "body_mass_g")
) #me tira error, porque codigo no articulado yet

#The mapping argument of the ggplot() function defines how variables 
# in your dataset are mapped to visual properties (aesthetics) of your plot. 
# The mapping argument is always defined in the aes() function, 
# and the x and y arguments of aes() specify which 
# variables to map to the x and y axes. 
# For now, we will only map flipper length to the x aesthetic and body mass to the y aesthetic. 

#Paso 4.we need to define a geom: 
#the geometrical object that a plot uses to represent data.
#available in letsplot with functions that start with geom_
(
    ggplot(data=penguins, mapping=aes(x="flipper_length_mm", y="body_mass_g"))
    + geom_point()
)
#La función geom_point() agrega una capa de puntos a su gráfico, 
# lo que crea un diagrama de dispersión. 
# letsplot viene con muchas funciones geom, 
# cada una de las cuales agrega un tipo diferente de capa a un gráfico.

#paso 5: Hacerlo mas estetico
#Añadiendo estética y capas
(
    ggplot(
        data=penguins,
        mapping=aes(x="flipper_length_mm", y="body_mass_g", color="species"),
    )
    + geom_point()
)
#Cuando una variable categórica se asigna a una estética, 
# letsplot asignará automáticamente 
# un valor único de la estética (aquí un color único) 
# a cada nivel único de la variable (cada una de las tres especies), 
# un proceso conocido como escala.

#A ESTA RELACION, LE AGREGO una capa más: 
# una curva suave que muestra la relación entre la masa corporal y la longitud de la aleta.

(
    ggplot(
        data=penguins,
        mapping=aes(x="flipper_length_mm", y="body_mass_g", color="species"),
    )
    + geom_point()
    + geom_smooth(method="lm")
)

#Dado que este es un nuevo objeto geométrico que representa nuestros datos, 
# añadiremos un nuevo geom como capa sobre nuestro punto geom: geom_smooth().
# Y especificaremos que queremos dibujar la línea de mejor ajuste 
# basándonos en un modelo lineal con el método ``lm``.

#Sin embargo, cada función geom en letplot también puede aceptar 
# un argumento de mapeo, lo que permite mapeos estéticos 
# a nivel local que se suman a los heredados del nivel global.
# queremos que los puntos se coloreen según la especie, 
# pero no que las líneas se separen para ellos, 
# debemos especificar color = especies solo para geom_point(): 
# por lo tanto, lo eliminamos del aes() global y lo añadimos a geom_point().

(
    ggplot(data=penguins, mapping=aes(x="flipper_length_mm", y="body_mass_g"))
    + geom_point(mapping=aes(color="species"))
    + geom_smooth(method="lm")
)

#We still need to use different shapes 
# for each species of penguins and improve labels.
#Por lo tanto, además del color, también 
# podemos asignar especies a la estética de la forma.

(
    ggplot(data=penguins, mapping=aes(x="flipper_length_mm", y="body_mass_g"))
    + geom_point(mapping=aes(color="species", shape="species"))
    + geom_smooth(method="lm")
)

#Se mejorar las etiquetas del gráfico usando la función labs() en una nueva capa. 
# Algunos argumentos de labs() pueden ser obvios:
#  "title" añade un título y "subtitle" añade un subtítulo al gráfico. 
# Otros argumentos coinciden con las asignaciones estéticas: 
# "x" es la etiqueta del eje x, "y" es la etiqueta del eje y, y "color" y "shape" definen la etiqueta de la leyenda.

(
    ggplot(data=penguins, mapping=aes(x="flipper_length_mm", y="body_mass_g"))
    + geom_point(aes(color="species", shape="species"))
    + geom_smooth(method="lm")
    + labs(
        title="Body mass and flipper length",
        subtitle="Dimensions for Adelie, Chinstrap, and Gentoo Penguins",
        x="Flipper length (mm)",
        y="Body mass (g)",
        color="Species",
        shape="Species",
    )
)