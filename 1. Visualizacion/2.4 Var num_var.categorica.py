
# To visualise the relationship between 
# a numerical and a categorical variable we can use side-by-side box plots.
from lets_plot import * #importo libreria
from palmerpenguins import load_penguins # de libreria extraigo la data
LetsPlot.setup_html()# autorizo a que me muestre la data
penguins = load_penguins()#creo variable pinguinos
penguins #muestro a los pinguienos

(ggplot(penguins, aes(x="species", y="body_mass_g")) + geom_boxplot())

#A box that indicates the range of the middle half of the data, 
# a distance known as the interquartile range (IQR), 
# stretching from the 25th percentile of the distribution to the 75th percentile. 
# In the middle of the box is a line that displays the median, 
# i.e. 50th percentile, of the distribution. 
# These three lines give you a sense of the spread of the distribution 
# and whether or not the distribution is symmetric about the median or skewed to one side.
#geom_boxplot():



#ADEMAS, we can make probability density plots 
# with geom_density().
(ggplot(penguins, aes(x="body_mass_g", color="species")) + geom_density(size=2))
#También hemos personalizado el grosor de las líneas 
# usando el argumento de tamaño para que 
# destaquen un poco más sobre el fondo.


#Además, podemos asignar especies 
# a las estéticas de color y relleno, 
# y usar la estética alfa para añadir transparencia 
# a las curvas de densidad rellenas. 
# Esta estética toma valores entre 0 (completamente transparente) 
# y 1 (completamente opaca). 
# En el siguiente gráfico, se establece en 0,5.
(
    ggplot(penguins, aes(x="body_mass_g", color="species", fill="species"))
    + geom_density(alpha=0.5)
)


