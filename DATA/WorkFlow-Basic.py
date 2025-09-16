
import numpy as py
primes = [1, 2, 3, 5, 7, 11, 13]
print(primes)

#To do basic arithmetic on a list, 
# use a list comprehension which has the structure 
# “for every element in this list, perform an 
# operation”. For example, to multiply each element by three.

[element * 3 for element in primes]

#Note that the word “element” above could have been 
# almost any word because we define it 
# by saying ...for element in .... You can try 
# the above with a different word, 
# eg [entry*3 for entry in primes].

#3.3. Keeping Track of Variables
#You can always inspect an already-created 
# object by typing its name into the interactive 
# window: primes
#type (primes) me devuelve el tipo de dato.

#3.5. Calling Functions. 
#In coding, a function has inputs, it performs its function, 
# and it returns any outputs. Let’s see a built-in function, sum():
sum(primes)

#La estructura general de las funciones es el nombre de la función, 
# seguido de corchetes y uno o más argumentos. 
# También se incluyen argumentos de palabra clave. Por ejemplo, sum() 
# incluye un argumento que indica a la función que empiece a 
# contar desde un número específico. 
# Veamos esto en acción empezando desde 100:
sum(primes,start=10)

#If you’re ever unsure of what a function does, 
# you can call help() on it (itself a function):
help(sum)

from lets_plot import *
import pandas as pd
from palmerpenguins import load_penguins
LetsPlot.setup_html()
penguins = load_penguins()

(
    ggplot(
        penguins,
        mapping=aes(x="flipper_length_mm", y="body_mass_g", color="species"),
    )
    + geom_smooth(method="lm")
)

