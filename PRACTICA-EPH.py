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


#Ejercicio 7: Medidas de dispersión por nivel educativo
#Consigna: Para las personas ocupadas, calcula por nivel educativo:
# • El desvío estándar del ingreso
# • El coeficiente de variación (desvío estándar / media * 100)
# • El ingreso mínimo y máximo
# • El rango de ingresos (máximo - mínimo)
# Ordena los resultados por coeficiente de variación.

df_dispersión = (df_seleccionado[df_seleccionado["ESTADO"] == 1]
    .groupby("nivel_educativo")
).apply(lambda g: pd. Series({
    "desvio_estandar_ingreso": np.sqrt(np.cov(g["P21"], aweights=g["PONDERA"])),
    "coef_variacion": (np.sqrt(np.cov(g["P21"], aweights=g["PONDERA"])) / 
    np.average(g["P21"], weights=g["PONDERA"])) * 100,
    "ingreso_minimo": g["P21"].min(),
    "ingreso_maximo": g["P21"].max(),
    "rango_ingresos": g["P21"].max() - g["P21"].min()
}))
df_dispersión = df_dispersión.sort_values("coef_variacion")
df_dispersión

#Paso	Código	Qué hace
#1. df_seleccionado[df_seleccionado["ESTADO"] == 1]	Filtra solo personas ocupadas.
#2. .groupby("nivel_educativo")	Agrupa por nivel educativo.
#3.	apply(lambda g: ...)	Aplica una función a cada grupo g.
#4.	pd.Series({...})	Crea una fila con las métricas de dispersión.
#5.	"desvio_estandar_ingreso": np.sqrt(np.cov(..., aweights=g["PONDERA"]))	
# Calcula el desvío estándar ponderado del ingreso.
#6.	"coef_variacion": (...)	Calcula el coeficiente de variación.
#7.	"ingreso_minimo": g["P21"].min()	Encuentra el ingreso mínimo.
#8.	"ingreso_maximo": g["P21"].max()	Encuentra el ingreso máximo.
#9.	"rango_ingresos": g["P21"].max() - g["P21"].min()	Calcula el rango de ingresos.
#10.	.sort_values("coef_variacion")	Ordena los resultados por coeficiente de variación.
#El coeficiente de variación es una medida relativa de dispersión que indica
# qué tan grande es el desvío estándar en relación con la media.
# Se expresa como un porcentaje y es útil para comparar la variabilidad entre diferentes conjuntos de datos.


#apply recorre cada grupo creado por groupby y aplica la función definida en lambda g: ...
# Cada grupo (g) es un subconjunto del DataFrame original, que contiene solo las filas 
# correspondientes a una categoría.
# Dentro de la función lambda, se crea una nueva Serie de pandas
# que contiene las estadísticas calculadas para ese grupo específico.
# El resultado final es un DataFrame donde cada fila representa un grupo
# (nivel educativo) y las columnas contienen las estadísticas calculadas.
#np.sqrt(np.cov(..., aweights=g["PONDERA"])) calcula el desvío estándar ponderado.
# La función np.cov calcula la covarianza, y al tomar la raíz cuadrada obtenemos el desvío estándar.
# El argumento aweights=g["PONDERA"] indica que se deben usar los valores de PONDERA
# como pesos para el cálculo, lo que ajusta la medida de dispersión según la importancia de cada observación.


#Ejercicio 8: Análisis por sexo y nivel educativo
#Consigna: Agrupa los datos por sexo y nivel educativo, y calcula:
#• La cantidad de personas (ponderada)
#• El ingreso promedio (ponderado)
#• La tasa de ocupación (porcentaje de ocupados)
# Luego calcula la brecha de ingresos entre varones y mujeres para cada nivel educativo.

df_nivel_educ_sexo = (df_seleccionado.groupby(["sexo_descr", "nivel_educativo"])).apply(lambda g: pd.Series ({
    "cantidad_personas_ponderada": g["PONDERA"].sum(),
    ##La función apply() aplica una operación personalizada a cada grupo. En este caso, esa operación 
    # devuelve una Serie de pandas con varios indicadores.
    #Suma los pesos muestrales del grupo.
    # Esto representa la cantidad total de personas en la población (no solo en la muestra), 
    # porque cada individuo cuenta con su peso.

    "ingreso_promedio_ponderado": np.average(g["P21"], weights=g["PONDERA"]),
    #Calcula el ingreso promedio ponderado usando los pesos muestrales. 
    # Esto da un ingreso medio representativo de la población, no solo de la muestra.

    "tasa_ocupacion": np.average((g["ESTADO"] == 1).astype(int), weights=g["PONDERA"]) * 100
    # Calcula el promedio de los ocupados y los convierte en enteros (1 para ocupado, 0 para no ocupado).
    # con weights=g["PONDERA"] se pondera por el factor de expansión.
    #Calcula la tasa de ocupación como el promedio ponderado de la condición de actividad.

}))
df_nivel_educ_sexo = df_nivel_educ_sexo.reset_index()
# .reset_index() convierte los índices de fila actuales (sexo_descr, nivel_educativo)
# en columnas normales, lo que facilita el acceso y la manipulación de los datos.
#Aplico lambda a cada grupo definido por la combinación de sexo y nivel educativo. Obteniendo
# un DataFrame con múltiples filas por nivel educativo (una para cada sexo) en columnas con las 
# estadísticas calculadas.

# Calculo la brecha de ingresos entre varones y mujeres para cada nivel educativo
brecha_ingresos = df_nivel_educ_sexo.pivot(
    index="nivel_educativo", 
    columns="sexo_descr", 
    values="ingreso_promedio_ponderado"
)
#pivot() reorganiza el DataFrame para que cada nivel educativo tenga una fila,
# y las columnas sean los ingresos promedio para varones y mujeres.

brecha_ingresos["brecha_varones_mujeres"] = (
    (brecha_ingresos["Varón"] - brecha_ingresos["Mujer"]) / brecha_ingresos["Mujer"]
) * 100 
# Calcula la brecha porcentual entre varones y mujeres considerando el ingreso promedio ponderado.
# La fórmula es: ((Ingreso Varones - Ingreso Mujeres) / Ingreso Mujeres) * 100
brecha_ingresos = brecha_ingresos.reset_index()
# Resetea el índice para que nivel_educativo vuelva a ser una columna normal.

brecha_ingresos




#Ejercicio 9: Cuartiles de ingreso por nivel educativo
# Consigna: Para las personas ocupadas, calcula por nivel educativo:
#• El primer cuartil de ingresos (P25)
#• La mediana de ingresos (P50)
#• El tercer cuartil de ingresos (P75)
#• El rango intercuartílico (IQR = P75 - P25)
#Ordena los resultados por mediana de ingresos.

df_cuartiles = (df_seleccionado[df_seleccionado["ESTADO"] == 1]).groupby("nivel_educativo").apply(lambda g: 
    pd.Series({
    "P25": np.percentile(g["P21"], 25),
    "P50": np.percentile(g["P21"], 50),
    #calculo de la mediana
    "P75": np.percentile(g["P21"], 75), }))
    #calculo del tercer cuartil
df_cuartiles["IQR"] = df_cuartiles["P75"] - df_cuartiles["P25"]# calculo del rango intercuartilico
df_cuartiles = df_cuartiles.sort_values("P50") #Ordeno por mediana de ingresos (P50)
df_cuartiles
#de mi dataframe seleccionado, filtro solo personas ocupadas y los agrupo por nivel educativo
#Luego, aplico una función a cada grupo que calcula los percentiles 25, 50 y 75 del ingreso (P21).
#Después, calculo el rango intercuartílico (IQR) restando P25 de P75.
#Finalmente, ordeno los resultados por la mediana de ingresos (P50) de manera ascendente.
#np.percentile() calcula los percentiles especificados del ingreso (P21) para cada grupo.
#El rango intercuartílico (IQR) es una medida de dispersión que indica la amplitud del
# rango central de los datos, ayudando a identificar la variabilidad en los ingresos dentro de cada nivel educativo.

#Ejercicio 10: Estadísticas por lugar de nacimiento y sexo
#Consigna: Agrupa los datos por lugar de nacimiento y sexo, y calcula:
#• La cantidad de personas (ponderada)
#• El porcentaje de personas con nivel secundario completo o superior
#• La edad promedio (ponderada)
#• La tasa de actividad (porcentaje de personas económicamente activas)
# Finalmente, elimina la agrupación y ordena los resultados por lugar de nacimiento 
# y luego por tasa de actividad de manera descendenteactividad de manera descendente

df_lugar_nacimiento_sexo = (df_seleccionado.groupby(["lugar_nacimiento", "sexo_descr"])).apply(
    lambda g: pd.Series ({
    "cantidad_personas_ponderada": g["PONDERA"].sum(),
    "porc_secundario_superior": np.average(g["nivel_educativo"].isin(["Secundaria completa", "Superior incompleto", "Superior completo"]), weights=g["PONDERA"]) * 100,
    "edad_promedio_ponderada": np.average(g["CH06"], weights=g["PONDERA"]),
    "tasa_actividad": np.average(g["ESTADO"].isin([1, 2]).astype(int), weights=g["PONDERA"]) * 100
})
)
#de mi dataframe seleccionado, agrupo por lugar de nacimiento y sexo
#Luego, aplico una función a cada grupo que calcula las estadísticas solicitadas.
#cantidad_personas_ponderada: Suma los pesos muestrales del grupo.
#porc_secundario_superior: Calcula el porcentaje ponderado de personas con nivel secundario completo o superior. Weights=g["PONDERA"] pondera por el factor de expansión.
#edad_promedio_ponderada: Calcula la edad promedio ponderada usando los pesos muestrales.
#tasa_actividad: Calcula la tasa de actividad como el promedio ponderado de personas económicamente activas (ocupados o desocupados).
#.isin() verifica si el nivel educativo está en la lista dada (1 OCUPADO Y 2 DESOCUPADO)
#.astype(int) convierte el booleano en 1 y 0 para el cálculo del promedio ponderado.


df_lugar_nacimiento_sexo = df_lugar_nacimiento_sexo.reset_index()
# Elimino la agrupación para que lugar_nacimiento y sexo_descr sean columnas normales
df_lugar_nacimiento_sexo = df_lugar_nacimiento_sexo.sort_values(by=["lugar_nacimiento", "tasa_actividad"], 
ascending=[True, False]
)
# Ordeno lugar de nacimiento ascendente y tasa de actividad descendente
df_lugar_nacimiento_sexo


#Desafío final (Opcional)
#Consigna: Combina las funciones de Tidyverse para crear un análisis que responda a la siguiente pregunta:
#¿Cómo varían los ingresos y la educación según el lugar de nacimiento y qué grupos tienen mayor desigualdad
#interna?
#Para ello deberás:
#1. Filtrar solo personas ocupadas entre 25 y 65 años
#2. Agrupar por lugar de nacimiento y calcular estadísticas de ingresos (promedio, mediana, desvío, CV)
#3. Calcular la proporción de personas con diferentes niveles educativos por lugar de nacimiento
#4. Ordenar los resultados según algún criterio relevante

#Paso	Código	Qué hace
df_desafio = (df_seleccionado 
    .loc[(df_seleccionado["ESTADO"] == 1) & (df_seleccionado["CH06"].between(25, 65))]
    .groupby("lugar_nacimiento"))
#1.	.De los ocupados aplico Filtrado: .loc[...]	Filtrando solo personas ocupadas entre 25 y 65 años.
#2.	Agrupación: .groupby("lugar_nacimiento") Agrupa por lugar de nacimiento.

df_desafio = df_desafio.apply(lambda g: pd.Series({
#3.Aplicación de funciones: .apply(lambda g: ...)	Calcula estadísticas de ingresos y educación para cada grupo.
#4.Estadísticas de ingresos: calculo promedio, mediana, desvío estándar y coeficiente de variación ponderados.
    "ingreso_promedio": np.average(g["P21"], weights=g["PONDERA"]),
    "ingreso_mediana": np.percentile(g["P21"], 50),                 
    "desvio_estandar_ingreso": np.sqrt(np.cov(g["P21"], aweights=g["PONDERA"])),
    "coef_variacion": (np.sqrt(np.cov(g["P21"], aweights=g["PONDERA"])) / np.average(g["P21"], weights=g["PONDERA"])) * 100,
    #coeficiente de variación = desvío estándar / media * 100, indica la dispersión relativa de los ingresos. 
    # Que tanto varían los ingresos en relación con el promedio de ingresos.

#5.Proporción de niveles educativos: Calcula el porcentaje ponderado de personas con diferentes niveles educativos.
    "porc_primaria_completa": np.average(g["nivel_educativo"].  eq("Primaria completa"), weights=g["PONDERA"]) * 100,     
    #.eq() compara cada valor de nivel_educativo con "Primaria completa", devolviendo una serie booleana.
    # de los que son True (cumplen la condición), calcula el promedio ponderado usando PONDERA.  
    # Multiplico por 100 para obtener el porcentaje.
    

    "porc_secundaria_completa": np.average(g["nivel_educativo"].  eq("Secundaria completa"), weights=g["PONDERA"]) * 100,
    # similar al anterior, pero para "Secundaria completa".
    "porc_superior_completo": np.average(g["nivel_educativo"].  eq("Superior completo"), weights=g["PONDERA"]) * 100
})) 
#6.	Ordenamiento: .sort_values("coef_variacion", ascending=False)    
# Ordena los resultados por coeficiente de variación de ingresos de manera descendente.
df_desafio = df_desafio.sort_values("coef_variacion", ascending=False)
df_desafio

#¿Cómo varían los ingresos y la educación según el lugar de nacimiento y qué grupos tienen mayor desigualdad
#interna?
# Respuesta:
# Los ingresos varían significativamente según el lugar de nacimiento, con diferencias notables en el ingreso promedio y mediano.
# La desigualdad interna, medida por el coeficiente de variación, también difiere entre los grupos,
# indicando que algunos lugares de nacimiento tienen una mayor dispersión en los ingresos que otros.
# Además, la proporción de personas con diferentes niveles educativos varía según el lugar de nacimiento,
# lo que sugiere que la educación también está influenciada por el origen geográfico.

#Hay una variacion muy importante en el ingreso promedio de acuerdo al lugar de nacimiento. 
# Siendo argentina el pais de nacimiento con menor ingreso promedio. 
# Los extranjeros tiene un salario promedio levemente superior de 17.030 unidades monetarias absolutas, 
# siendo superado por los nacidos en otras provincias con un ingreso promedio de 17.500 unidades monetarias absolutas.
#La desigualdad se hace avidente cuando observamos que los que nacen en otra provincia 
# tienen niveles de educacion superior que casi llegan a duplicar al de los nacidos en argentina 
# y en el extranjero.

# La desigualdad interna, medida por el coeficiente de variación,
# indica que los nacidos en otra provincia tienen una mayor dispersión en los ingresos (CV= 66.27%)
# en comparación con los nacidos en Argentina (CV= 60.45%) y en el extranjero (CV= 59.12%).
# Esto sugiere que, aunque los nacidos en otra provincia tienen un ingreso promedio más alto,
# también enfrentan una mayor desigualdad en sus ingresos en comparación con los otros grupos.  
# Además, la proporción de personas con diferentes niveles educativos varía según el lugar de nacimiento.
# Los nacidos en otra provincia tienen una mayor proporción de personas con nivel secundario completo
# y superior completo en comparación con los nacidos en Argentina y en el extranjero.
