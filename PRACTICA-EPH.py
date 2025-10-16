import pandas as pd
import numpy as np

#1)Ejercicio 1: Selección y filtrado básico
#Consigna: Selecciona las variables CODUSU, NRO_HOGAR, COMPONENTE, 
# CH04 (sexo), CH06( edad), NIVEL_ED (nivel educativo), CH15 (lugar de nacimiento), 
# ESTADO (condición de actividad), P21(ingreso de la ocupación principal) y 
# PONDERA (factor de expansión). Luego filtra para considerar solo personas de 25 años o más.
#Carga el archivo CSV.
#seleccionar variables clave y quedarte solo con personas de 25 años o más.

import pandas as pd

datos = r"C:\Users\Usuario\Desktop\UBA\DATOS\Bases de datos\usu_individual_T324.txt"

df = pd.read_csv(datos, sep=";", quotechar='"', low_memory=False)
df 

#En Python usamos .loc[] o df[['col1', 'col2']] y un filtro booleano.
df_seleccionado= df[["CODUSU", "NRO_HOGAR", "COMPONENTE", "CH04", "CH06", 
"NIVEL_ED", "CH15", "ESTADO", "P21", "PONDERA"]].loc[df["CH06"]>=25].copy()
df_seleccionado

#Ejercicio 2: Creación de variables categóricas

#Consigna: A partir del conjunto de datos obtenido en el ejercicio anterior, 
# crea las siguientes variables nuevas utilizando mutate() y case_when()
#• sexo_desc: Descripción del sexo (“Varón” o “Mujer”) a partir de CH04
#• nivel_educativo: Descripción del nivel educativo 
# (Primaria incompleta, Primaria completa, etc.) a partir de NIVEL_ED
#• lugar_nacimiento: Descripción del lugar de nacimiento a partir de CH15
#• condicion_actividad: Descripción de la condición de actividad 
# (Ocupado, Desocupado, Inactivo) a partir de ESTADO

# Crea variables descriptivas a partir de códigos numéricos
# En Python usamos np.select() o np.where()
# np.select() es más adecuado para múltiples condiciones
# .map() es útil para reemplazos directos basados en un diccionario
df_seleccionado["sexo_descr"]= df_seleccionado ["CH04"].map({
    1: "Varón", 
    2: "Mujer"
})

#.isin() es útil para verificar si un valor está en una lista dada
df_seleccionado["nivel_educativo"] = df_seleccionado["NIVEL_ED"].map({
    1: "Primaria incompleta",
    2: "Primaria completa",
    3: "Secundaria incompleta",
    4: "Secundaria completa",
    5: "Superior incompleto",
    6: "Superior completo",
    7: "Sin instrucción",
    8: "Ns/Nr",
})
#aca .map() asigna directamente los valores
# si el valor no esta en el diccionario, asigna NaN, que es el comportamiento por defecto
# Si quieres asignar un valor por defecto, puedes usar .fillna()

df_seleccionado["lugar_nacimiento"] = df_seleccionado["CH15"].map({
    1: "Argentina",
    2: "Otra provincia",
    3: "Extranjero"
})

df_seleccionado["condicion_actividad"] = df_seleccionado["ESTADO"].map({
    1: "Ocupado",
    2: "Desocupado",
    3: "Inactivo"
})

#Ejercicio 3: Filtrado múltiple
#Consigna: Filtra los datos para analizar 
# solo a las personas ocupadas (ESTADO == 1) 
# que tienen entre 30 y 60 años, 
# y que hayan nacido en otra provincia o en el extranjero.

df_filtrado = df_seleccionado.query(
    "ESTADO == 1 and 30 <= CH06 <= 60 and CH15 in [2, 3]"
)
#query() me sirve para filtrar con multiples condiciones y tambien para condiciones complejas
#tambien puedo usar boolean indexing, pero es menos legible para multiples condiciones
#query () sirve para condiciones complejas y legibles
# boolean indexing es más directo para condiciones simples


#Ejercicio 4: Ordenamiento de datos
#Consigna: Ordena los datos de manera 
#descendente por nivel educativo (NIVEL_ED) 
# y luego de manera ascendente por edad (CH06).
#  Muestra los primeros 15 registros del resultado.

df_ordenado = df_seleccionado.sort_values(
    by=["NIVEL_ED", "CH06"], 
    ascending=[False, True]
).head(15)

#sort_values() es para ordenar y tiene varios argumentos
# by= columna o lista de columnas para ordenar  
# ascending= True (ascendente) o False (descendente)
#en este caso, NIVEL_ED descendente y CH06 ascendente,
#NIVEL_ED --> False= descendente
#CH06 --> True= ascendente

#Ejercicio 5: Estadísticas por nivel educativo
#Consigna: Agrupa los datos por nivel educativo y calcula:
# •La cantidad de personas (ponderada)
# • La edad promedio (ponderada)
# • El ingreso promedio de la ocupación principal (ponderado)
# • El porcentaje de ocupados Ordena los resultados por ingreso promedio de manera descendente.


#Explicación paso a paso: Agrupación: groupby("nivel_educativo") crea un grupo por cada nivel educativo.
#Aplicación de funciones: Se usa apply(lambda g: ...) para calcular varias métricas dentro de cada grupo.
#Ponderaciones: np.average(..., weights=...) calcula promedios ponderados usando la variable PONDERA.
#Ordenamiento: .sort_values(by="ingreso_promedio_ponderado", ascending=False) ordena los resultados de mayor a menor ingreso promedio.
# Porcentaje de ocupados: Calculado como el promedio ponderado de (ESTADO == 1) *

#Usar groupby().apply() o directamente agg() con expresiones compactas.

df_estadisticas = (df_seleccionado.groupby("nivel_educativo").apply(lambda g: pd.Series({
        "cantidad_personas_ponderada": g["PONDERA"].sum(),
        "edad_promedio_ponderada": np.average(g["CH06"], weights=g["PONDERA"]),
        "ingreso_promedio_ponderado": np.average(g["P21"], weights=g["PONDERA"]),
        "porcentaje_ocupados": np.average((g["ESTADO"] == 1).astype(int), weights=g["PONDERA"]) * 100
    }))
    .sort_values("ingreso_promedio_ponderado", ascending=False)
)
df_estadisticas
#groupby() agrupa por nivel educativo, estos ahora son fila
#apply() aplica una función a cada grupo
#Dentro de apply(), usamos pd.Series({...}) para devolver múltiples estadísticas como una serie.
# np.average(..., weights=...) calcula promedios ponderados usando la variable PONDERA.
# Finalmente, sort_values() ordena el DataFrame resultante por ingreso promedio de manera descendente.
#El resultado es un DataFrame con una fila por nivel educativo y columnas para cada estadística calculada.
#El índice del DataFrame resultante es nivel_educativo, y las columnas son las estadísticas calculadas.
#Cada fila representa un nivel educativo con sus respectivas métricas.
#estás calculando un promedio ponderado, no un promedio simple.

#Weights Esto significa que cada observación de x (por ejemplo, una persona) no vale lo mismo:
# su peso (w) determina cuánto representa en la población total.

#Ejercicio 6: Estadísticas por lugar de nacimiento
#Consigna: Agrupa los datos por lugar de nacimiento y calcula:
# • La cantidad de personas (ponderada)
# • El porcentaje de personas con educación superior completa
# • El ingreso promedio de la ocupación principal (ponderado)
# • La edad promedio (ponderada)
# Ordena los resultados por porcentaje de educación superior de manera descendente.

# Agrupa por lugar de nacimiento y calcula las estadísticas solicitadas
#as_index=False para que lugar_nacimiento sea una columna normal, sino el índice sería lugar_nacimiento


df_est_lugar_nacimiento = (df_seleccionado.groupby("lugar_nacimiento", as_index=False).apply(
    lambda g: pd.Series({ "personas_pond": g["PONDERA"].sum(),
    "porc_superior_completo": np.average(g["nivel_educativo"].eq("Superior completo"),
    weights=g["PONDERA"] ) * 100,
    "ingreso_promedio": np.average(g["P21"], weights=g["PONDERA"]),
    "edad_promedio": np.average(g["CH06"], weights=g["PONDERA"])
    })
    )
    .sort_values("porc_superior_completo", ascending=False)
    .reset_index(drop=True)
)
df_est_lugar_nacimiento
#Paso	Código	Qué hace
#1. df_seleccionado.groupby("lugar_nacimiento", as_index=False)	Agrupa el DataFrame por lugar de nacimiento.
#2. apply(lambda g: ...)	Aplica una función a cada grupo g (subtabla).
#3.	pd.Series({...})	Crea una fila con las métricas resumidas.
#4.	"personas_pond": g["PONDERA"].sum()	Suma los factores de expansión → total ponderado.
#5.	"porc_superior_completo": np.average(..., weights=g["PONDERA"]) * 100	Calcula el % ponderado de personas con educación superior completa.
#6.	"ingreso_promedio": np.average(g["P21"], weights=g["PONDERA"])	Promedio ponderado del ingreso principal.
#7. "edad_promedio": np.average(g["CH06"], weights=g["PONDERA"])	Promedio ponderado de la edad.
#8.	.sort_values("porc_superior_completo", ascending=False)	Ordena los resultados de mayor a menor.
#9. .reset_index(drop=True)	Limpia el índice y deja filas numeradas.


