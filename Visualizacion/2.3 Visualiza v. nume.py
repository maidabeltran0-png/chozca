#A variable is numerical (or quantitative) 
# if it can take on a wide range of numerical values, 
# and it is sensible to add, subtract, or take averages with those values. 
# Numerical variables can be continuous or discrete.

#One commonly used visualisation for distributions of continuous variables is a histogram.

from lets_plot import * #importo libreria
from palmerpenguins import load_penguins # de libreria extraigo la data
LetsPlot.setup_html()# autorizo a que me muestre la data
penguins = load_penguins()#creo variable pinguinos
penguins #muestro a los pinguinos

(ggplot(penguins, aes(x="body_mass_g")) + geom_histogram(binwidth=200))
#obtengo un histograma que muestra cantidad 
#observaciones en eje y con eje x= body_mass

#An alternative visualisation for distributions 
# of numerical variables is a density plot. 
# A density plot is a smoothed-out version of a 
# histogram and a practical alternative, 
# particularly for continuous data that comes from 
# an underlying smooth distribution.

(ggplot(penguins, aes(x="body_mass_g")) + geom_density())