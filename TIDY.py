#Para organizar tu  data en python usando el principio de Tidy data
#esto no es apropiado para todo, pero para muchos casos es muy util
#Una vez que tenga datos ordenados, pasará mucho menos tiempo transfiriendo 
# datos de una representación a otra

#6.2.1 Introducción a Tidy Data
#1. Cada variable debe tener su propia columna.
#2. Cada observación debe tener su propia fila.
#3. Cada valor debe tener su propia celda.

#¿Por qué asegurar la organización de sus datos? Hay dos ventajas principales:
#Elegir una forma consistente de almacenar datos tiene una ventaja general. 
# Si se cuenta con una estructura de datos consistente, 
# es más fácil aprender las herramientas que la utilizan, 
# ya que presentan una uniformidad subyacente. El paquete de visualización de datos Seaborn, 
# están diseñadas pensando en la organización de datos.
# Usar variables en columnas tiene una ventaja específica: 
# permite aprovechar las operaciones vectorizadas de Pandas (operaciones más eficientes).
#La tidy data no siempre son apropiados, pero son una excelente opción predeterminada 
# para datos tabulares. Una vez que se usan como predeterminados, es más fácil pensar en 
# cómo realizar operaciones posteriores.
#6.3. Tools to Make Data Tidy with pandas
#melt() puede ayudarte a pasar de datos “más amplios” a datos “más largos” y es muy bueno recordarlo.

import pandas as pd
# Import the main pyarrow library
import pyarrow as pa

# Import the csv module
import pyarrow.csv as pv

df = pd.DataFrame(
    {
        "first": ["John", "Mary"],
        "last": ["Doe", "Bo"],
        "job": ["Nurse", "Economist"],
        "height": [5.5, 6.0],
        "weight": [130, 150],
    }
)
print("\n UNME: ")
print(df)
print("\n ME: ")
df.melt(id_vars=["first", "last"], var_name="quantity", value_vars=["height", "weight"])

#La función melt() se usa para reorganizar el DataFrame de formato ancho (“wide”) a formato largo (“long”).
# id_vars=["first", "last"] → columnas que no se tocan, se mantienen fijas como identificadores.
# value_vars=["height", "weight"] → columnas que se “derriten” o se convierten en filas.
# var_name="quantity" → el nuevo nombre para la columna que indicará qué variable era (height o weight).


#EJEMPLO
df_tb = pd.read_parquet(
    "https://github.com/aeturrell/python4DS/raw/refs/heads/main/data/who_tb_cases.parquet"
)
df_tb.head()

#ACA HAY DOS VARIABLES EN UNA COLUMNA. Ahora, vamos a COMBINAR esto.
df_tb.melt(
    id_vars=["country"],
    var_name="year",
    value_vars=["1999", "2000"],
    value_name="cases",
)
#df_tb.melt(...) convierte tu DataFrame de ancho a largo, dejando country fijo, 
# poniendo los años en la columna year y los valores (casos) en cases.
#los valores cases son ahora todos numéricos, se refieren a una sola variable (casos de TB) y
# los años están en una columna separada, incluyen cada año como una fila separada.

#6.3.2. Un método más simple de ancho a largo
#también existe wide_to_long(), que es realmente útil para casos típicos 
# de limpieza de datos donde tiene datos como estos
import numpy as np

df = pd.DataFrame(
    {
        "A1970": {0: "a", 1: "b", 2: "c"},
        "A1980": {0: "d", 1: "e", 2: "f"},
        "B1970": {0: 2.5, 1: 1.2, 2: 0.7},
        "B1980": {0: 3.2, 1: 1.3, 2: 0.1},
        "X": dict(zip(range(3), np.random.randn(3))),
        "id": dict(zip(range(3), range(3))),
    }
)
df
#Es decir, datos con diferentes variables y períodos de tiempo en las columnas. 
# La opción "Ancho a largo" nos permitirá proporcionar información sobre los nombres
#  de los stubs ('A', 'B'), el nombre de la variable que siempre aparece en 
# las columnas (en este caso, un año), cualquier valor (X en este caso) y una columna de ID.

pd.wide_to_long(df, stubnames=["A", "B"], i="id", j="year")
#stubnames=["A", "B"] → los nombres de las variables que se encuentran en las columnas.
#i="id" → la columna que contiene el identificador único para cada fila.
#j="year" → el nombre de la nueva columna que contendrá los valores que siempre aparecen en las columnas (año).
#El resultado es un DataFrame de formato largo con un índice jerárquico (id, year) y columnas A y B.    

#6.3.3. Apilar y desapilar
#Stack, stack() es un atajo para tomar un solo tipo de variable de datos
#  ancha de las columnas y convertirlo en un conjunto de datos de formato largo, 
# pero con un índice adicional.
tuples = list(
    zip(
        *[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]
    )
)
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
df
#Apilemos esto para crear un conjunto de datos ordenado:

#Esto convierte las columnas A y B en una sola columna,     
# con un nuevo nivel en el índice que indica si el valor era de A o B.      
#El método opuesto a stack() es unstack(), que toma un nivel del índice y lo convierte en columnas.

df = df.stack()
df

#6) ¿Por qué usar stack()? — Intuición práctica
#stack() convierte datos anchos (varias columnas por unidad) en datos largos 
# (una fila por observación/variable), lo que facilita:
# agrupaciones por niveles del índice,
# uso de funciones como groupby, pivot, melt,
# graficar series múltiples como una sola columna,
# análisis por variable cuando las columnas representan la misma medida en distintas condiciones.

#Esto ha creado automáticamente un índice multicapa, pero puede revertirse a 
# un índice numerado mediante df.reset_index().

# Ahora veamos cómo desapilar. En lugar de desapilar las variables "A" y "B" con las que comenzamos, 
# desapilaremos la primera columna pasando level=0 (el valor predeterminado 
# es desapilar el índice más interno). Este diagrama muestra lo que sucede:

df.unstack(level=0)

#El nivel 0 del índice (first) se convierte en columnas,
# y las columnas A y B se mantienen como columnas.
#El resultado es un DataFrame con un índice de segundo nivel (second) y columnas
# que son un MultiIndex (first, A) y (first, B).
#stack() → lleva columnas a filas.
#unstack() → lleva un nivel de filas a columnas.
#level=0 indica qué nivel del índice quieres “desapilar”.



#6.3.4. Pivot tables
#pivot_table() es una herramienta poderosa para reorganizar datos.
# Es similar a pivot(), pero tiene más funciones, como agregar datos.

df_tb_cp = pd.read_parquet(
    "https://github.com/aeturrell/python4DS/raw/refs/heads/main/data/who_tb_case_and_pop.parquet"
)
df_tb_cp
#Verás que tenemos, para cada año-país, “caso” y “población” en filas diferentes.
#let’s pivot this to see the difference:
pivoted = df_tb_cp.pivot(
    index=["country", "year"], columns=["type"], values="count"
).reset_index()
pivoted

#ahora tenemos una fila por país-año, con columnas separadas para casos y población.
#pivot() toma tres argumentos:      
#index=["country", "year"] → las columnas que desea mantener como identificadores.
#columns=["type"] → la columna cuyos valores desea convertir en nuevas columnas.
#values="count" → la columna que contiene los valores que desea colocar en las nuevas columnas

#Los pivotes son especialmente útiles para datos de series temporales, 
# donde operaciones como shift() o diff() suelen aplicarse asumiendo que una entrada 
# en una fila sigue (en el tiempo) a la anterior. 
# Al usar shift(), solemos querer desplazar una sola variable en el tiempo, 
# pero si una sola observación (en este caso, una fecha) ocupa varias filas, 
# la sincronización puede fallar. Veamos un ejemplo.
import numpy as np

data = {
    "value": np.random.randn(20),
    "variable": ["A"] * 10 + ["B"] * 10,
    "date": (
        list(pd.date_range("1/1/2000", periods=10, freq="M"))
        + list(pd.date_range("1/1/2000", periods=10, freq="M"))
    ),
}
df = pd.DataFrame(data, columns=["date", "variable", "value"])
df.sample(5)
#Aquí, cada fecha tiene dos filas, una para cada variable.
#Si intentamos usar shift() para calcular la diferencia entre fechas consecutivas,
# obtendremos resultados incorrectos, ya que las filas no están en orden cronológico.
#Si simplemente ejecutamos shift() en lo anterior, se desplazarán las variables B y A juntas, 
# aunque se superpongan en el tiempo y sean variables diferentes. 
# Por lo tanto, pivotamos a un formato más amplio (y entonces podemos desplazarnos 
# en el tiempo de forma segura).

df.pivot(index="date", columns="variable", values="value").shift(1)
#Aquí, cada fecha tiene su propia fila y las variables A y B son columnas separadas.
#Ahora, cuando usamos shift(), cada variable se desplaza independientemente en el tiempo.
#6.3.5. Resumen
#Aquí hay un resumen rápido de las funciones que hemos visto para reorganizar datos:
# melt() → de ancho a largo.
# wide_to_long() → de ancho a largP, para casos comunes.
# stack() → de ancho a largo, para una sola variable.
# unstack() → de largo a ancho, para una sola variable.
# pivot() → de largo a ancho, para una o más variables.
# pivot_table() → como pivot(), pero con agregación.
#La primera fila es NAN porque no hay un valor anterior con el que restar.
#La segunda fila es NAN porque no hay un valor anterior con el que restar.
#La tercera fila es 0.5 porque 2.5 - 2.0 = 0.5.
#La cuarta fila es -0.5 porque 2.0 - 2.5 = -0.5.