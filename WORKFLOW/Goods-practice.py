#Existen herramientas excelentes para rediseñar código existente rápidamente, como el paquete Black de Python
# reglas para codear de la mejor manera posible
# pip install black
import pandas as pd
import numpy as np

this_is_a_var = 5
#Al usar el encadenamiento de métodos (algo que puede ver en acción en Transformación de Datos), 
# es necesario colocar la cadena entre paréntesis y se recomienda usar una nueva 
# línea para cada método. El siguiente fragmento de código muestra 
# un ejemplo de cómo se ve correctamente:
import pandas as pd

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

# Chaining inside parentheses works

results = df.groupby(["col3", "col4"]).agg({"col1": "count", "col2": "mean"})

results
#5.5.1. Do not repeat yourself (DRY)
# Evite la repetición de código. Si encuentra que está copiando y pegando el mismo fragmento de código
# varias veces, considere escribir una función para ello. Esto hace que el código sea más fácil de mantener.
# Si necesita cambiar algo, solo tiene que hacerlo en un lugar.

#5.5.2. KISS (Keep It Simple, Stupid)
# Mantenga su código simple y fácil de entender. Evite la complejidad innecesaria. 
# i una solución simple funciona, no busque una más complicada.
# Use nombres descriptivos para variables y funciones.
# Use nombres de variables y funciones
# que sean fáciles de entender y recordar.
# Use comentarios para explicar el propósito del código.
# Use comentarios para explicar partes complejas del código.
# Use comentarios para explicar decisiones de diseño.

#5.5.3. SoC (Separation of Concerns) / Make it Modular
# Separe diferentes partes de su código en funciones o clases.
# Cada función o clase debe tener una única responsabilidad.
# Esto hace que el código sea más fácil de entender y mantener.
# Facilita la reutilización del código.
# Facilita las pruebas unitarias.
# Facilita la colaboración en equipo.
# Facilita la depuración.
# Facilita la extensión del código.
# Facilita la lectura del código.
# Facilita la documentación del código.
# Facilita la refactorización del código.
# Facilita la integración del código.
# Facilita la implementación del código.
# Facilita la optimización del código.
# Facilita la internacionalización del código.
# Facilita la localización del código.
# Facilita la accesibilidad del código. 
# Facilita la seguridad del código.
# Facilita la escalabilidad del código.
# Facilita la portabilidad del código.


#No tengas un solo archivo que lo haga todo. Si divides tu código en módulos separados
#  e independientes, será más fácil de leer, depurar, probar y usar. 
# Puedes consultar el capítulo sobre fundamentos de la codificación para ver
#  cómo crear e importar funciones desde otros scripts. Pero incluso dentro de un script, 
# puedes modularizar tu código definiendo funciones con entradas y salidas claras.
# Una buena regla general es que si un código que cumple un objetivo tiene más de 30 líneas,
# probablemente debería incluirse en una función. Los scripts de más de 500 líneas también son fáciles de dividir.
# En relación con esto, no tengas una sola función que intente hacerlo todo. 
# Las funciones también deben tener límites; deben hacer aproximadamente una sola cosa.
# Si estás nombrando una función y tienes que usar "y" en el nombre, 
# probablemente valga la pena dividirla en dos funciones.
# Las funciones tampoco deben tener "efectos secundarios"; es decir, solo deben aceptar valores 
# y generar valores mediante una declaración de retorno. No deben modificar variables 
# globales ni realizar otros cambios.
# Otra buena regla general es que cada función no debe tener muchos argumentos separados.
# Un último consejo para la modularidad y la creación de funciones 
# es no usar "banderas" en las funciones (también conocidas como condiciones booleanas). Aquí tienes un ejemplo:




# This is bad
"chozca", true
"CHOZCA"
def transform(text, uppercase):
    if uppercase:
        return text.upper()
    else:
        return text.lower()

# This is good
def uppercase(text):
    return text.upper()

def lowercase(text):
    return text.lower()
#COMPLEJIDAD CICLOMÁTICA
# La complejidad ciclomática es una métrica que mide la complejidad de un programa.
# Se calcula contando el número de caminos linealmente independientes a través del código fuente.
# Un valor más alto indica un código más complejo.
# La complejidad ciclomática se puede calcular utilizando la siguiente fórmula:
# M = E - N + 2P
# Donde:
# M = Complejidad ciclomática
# E = Número de aristas en el grafo de control de flujo
# N = Número de nodos en el grafo de control de flujo
# P = Número de componentes conectados (normalmente 1 para un programa)
# Un valor de complejidad ciclomática de 1-10 se considera simple y fácil de entender.
# Un valor de 11-20 se considera moderadamente complejo y puede ser difícil de entender
# Un valor de 21-50 se considera complejo y puede ser muy difícil de entender
# Un valor de más de 50 se considera muy complejo y es probable que sea casi imposible de entender
# Se recomienda mantener la complejidad ciclomática por debajo de 10.