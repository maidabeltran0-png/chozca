#Trabajar con mi propia data. Como leer archivos rectangulares de texto simple en Python.
#Apenas exploraremos superficialmente la importación de datos, pero muchos de los principios 
# se pueden aplicar a otros tipos de datos. Terminaremos con algunas sugerencias para abrir 
# otros tipos de datos.

#8.1.1 Requiere el paquete de pandas instalado.
import pandas as pd

#8.2. Hay una amplia gama de formatos de entrada y salida disponibles en pandas: 
# Stata (.dta), Excel (.xls, .xlsx), csv, tsv, formatos de big data (HDF5, parquet), 
# JSON, SAS, SPSS, SQL y más. "https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html"

#Si bien pandas tiene una gran cantidad de formas de leer datos y cargarlos en su sesión de Python, 
# aquí nos centraremos en el humilde archivo de tabla de texto sin formato; 
# por ejemplo, csv (valores separados por comas) y tsv (valores separados por tabulaciones).}

#8.2.1. Lectura de datos de un archivo.
#Toda la potencia necesaria para abrir archivos de tabla de texto plano se encuentra en una sola función, 
# pd.read_csv(). Acepta numerosos argumentos, pero los dos más importantes son 
# el primero (sin nombre): que proporciona la ruta a los datos, y 
# sep= (un argumento de palabra clave) que indica a Pandas si los valores deben estar separados por comas, tabulaciones u otro carácter. 

# Sin embargo, si deja este campo en blanco, Pandas lo adivinará automáticamente. 
# Para ver el conjunto completo de argumentos, ejecute help(pd.read_csv).
# Así se ve un archivo CSV simple con una fila para los nombres de columna 
# (también conocida como fila de encabezado) y seis filas de datos (usando la terminal).

students = pd.read_csv("students.csv")
students
#La función read CSV crea automáticamente un nuevo índice (que representa simplemente la posición de cada fila) 
# y toma la primera línea de datos como encabezado o nombre de columna. Sin embargo, puede ajustar 
# este comportamiento de varias maneras. A veces, el archivo contiene algunas líneas de metadatos. 
# Puede usar skiprows=n para omitir las primeras n líneas, 
# por ejemplo, pd.read_csv("data/students.csv", skiprows=2).
# Es posible que los datos no tengan nombres de columna. 7
# Puede usar names = a list para indicar a read_csv() que use una opción diferente para 
# los nombres de columna. Por ejemplo, pd.read_csv("data/students.csv", names=range(5)) colocaría 
# los números del 0 al 4 como nombres de columna.
# Puede cambiar la columna que se utiliza como índice. 
# El comportamiento predeterminado es crear un índice, pero para estos datos, 
# ya existe una columna de ID que podríamos usar. Para ello, use el argumento index_col=, 
# por ejemplo, pd.read_csv("data/students.csv", index_col=0).
# Esto es todo lo que necesita saber para leer aproximadamente el 75 % de los archivos CSV que encontrará 
# en la práctica. La lectura de archivos separados por tabulaciones y de ancho fijo se realiza con la misma función.

#8.2.2. First Steps

#Una vez que se leen los datos, el primer paso suele ser transformarlos para facilitar su uso en el resto 
# del análisis. Por ejemplo, los nombres de las columnas del archivo de estudiantes que leímos 
# tienen un formato no estándar.

#Podrías considerar renombrarlos uno por uno con .rename() o usar una función de otro paquete 
# para limpiarlos y convertirlos a todos en Snake Case a la vez. Usaremos el paquete skimpy para esto. 
# Skimpy es un paquete más pequeño, instálalo ejecutando pip install skimpy en la terminal.

#Desde skimpy, utilizaremos la función clean_columns(); esta toma un marco de datos y 
# devuelve un marco de datos con nombres de variables convertidos al formato snake.
import skimpy as sk 

from skimpy import clean_columns

students = clean_columns(students)
students
