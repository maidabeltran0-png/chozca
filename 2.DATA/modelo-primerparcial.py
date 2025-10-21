import pandas as pd
import numpy as np
df = pd.DataFrame(
    data={
        "id_vendedor": [0, 1, 2, 3, 4, 5, 6, 7],
        "nombre": ["García", "Lopez", "Martín", "Silva", "Rodríguez","Fernandez", "Morales", "Castro"],
        "sucursal": ["Norte", "Sur", "Centro", "Norte", "Sur", "Centro", "Este", "Este"],
        "region": ["CABA", "GBA", "CABA", "CABA", "GBA", "CABA", "Interior", "Interior"],
        "ventas_q1": [45000, 38000, 67000, 29000, 54000, 41000, 33000, 28000],
        "ventas_q2": [52000, 41000, 58000, 35000, 49000, 46000, 38000, 31000],
        "años_empresa": [3, 7, 2, 5,1,4,6,2],
        "categoria_contrato": ["Planta", "Planta", "Contrato", "Planta", "Contrato", "Planta", "Planta", "Contrato"],
        "comision_base": [0.02, 0.025, 0.015, 0.02, 0.015, 0.02,0.025, 0.015],

    },
)
# 1.Obtener una tabla que muestre el nombre del vendedor, la sucursal y 
# las ventas totales del semestre (suma de Q1 y Q2), ordenada de mayor a menor por ventas totales.

#RESULTADO. PASO 1. CREO NUEVA COLUMNA CON VENTAS TOTALES
df["ventas_totales"] = df["ventas_q1"] + df["ventas_q2"]
#RESULTADO. PASO 2. SELECCIONO COLUMNAS REQUERIDAS Y ORDENO
#para ordenar de mayor a menor uso el parametro ascending = False en sort_values
resultado_uno= df[["nombre", "sucursal", "ventas_totales"]].sort_values("ventas_totales", ascending=False)
#paso 3. muestro resultado
print(resultado_uno)
#sort_values sirve para ordenar los valores de un DataFrame por una o más columnas.
# el parametro  ascending = False ordena de mayor a menor, True de menor a mayor

#ASCENDENTE DE MENOR A MAYOR
#DESCENDENTE DE MAYOR A MENOR

# query sirve para filtrar filas en un DataFrame basado en una condición booleana.

# 2. Objetivo: Mostrar una tabla con la región, la cantidad de vendedores 
# y el promedio de años de experiencia por región.

resultado_dos = df.groupby(["region", "nombre"]).size().reset_index()[["region", "nombre"]]
print(resultado_dos)


