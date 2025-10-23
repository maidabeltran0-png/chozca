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

#Otra tarea común tras leer datos es considerar los tipos de variables. 
# En la columna favourite_food, hay varios alimentos 
# y, a continuación, el valor NaN, que se ha leído como un número de punto flotante 
# en lugar de una cadena faltante. Podemos solucionar esto convirtiendo esa 
# columna explícitamente en cadenas:
students["favourite_food"] = students["favourite_food"].astype("string")
students
#Pero si el archivo original tenía un formato raro (por ejemplo, "NaN" sin comillas),
# pandas podría interpretarlo como un número de punto flotante.
#Si pandas interpreta una columna de texto como número (float), 
# muchas funciones no van a funcionar correctamente.
#Al convertirla a string, asegurás que todos los métodos de texto funcionen bien.
#El tipo string de pandas usa el valor <NA>, que se comporta 
# mejor que NaN (de NumPy) en operaciones lógicas o de texto.


#De forma similar, "edad" tiene tipos de datos mixtos: cadena y entero. 
# Mapeemos el "cinco" con el número cinco.

students["age"] = students["age"].replace("five", 5)
students["age"]

# Otro ejemplo donde el tipo de dato es incorrecto es meal_type. 
# Esta es una variable categórica con un conjunto conocido de posibles valores. 
# Pandas tiene un tipo de dato especial para estos: No tiene infinitos valores posibles, ni un orden numérico continuo.
# Eso la diferencia de, por ejemplo, age, que sí es una variable numérica (4, 5, 6, 7, 8…).
# Pero si la convertís a category, gana ventajas: menos uso de memoria y operaciones más rápidas.

students["meal_plan"] = students["meal_plan"].astype("category")
students["meal_plan"]
#Tenga en cuenta que los valores de la variable meal_type se han mantenido exactamente iguales, 
# pero el tipo de variable ha cambiado de objeto a categoría.
# Resulta un poco tedioso tener que revisar las columnas una por una, asignando una sola línea 
# para aplicar el tipo. 
# Una alternativa es pasar un diccionario que asigne los nombres de las columnas a los tipos, 
# como se muestra a continuación:
students = students.astype({"student_id": "int", "full_name": "string", "age": "int"})
students.info()

#Convierte la columna favourite_food al tipo cadena de texto (string), 
# para que todos sus valores (incluidos los faltantes <NA>) se traten como texto,
# y no como números ni valores flotantes.

#8.2.3. Exercises
#What function would you use to read a file where fields were separated with “|”?
#pd.read_csv("file.txt", sep="|")

#8.3. Reading data from multiple files
#A veces, los datos se dividen en varios archivos. Por ejemplo, puede tener un archivo por mes o por año. 
# En tales casos, puede leer cada archivo por separado y luego concatenarlos en un solo marco de datos.
#Aquí hay un ejemplo simple que lee tres archivos CSV y los concatena en un solo marco de datos.

#Con pd.read_csv() puede leer estos datos uno por uno y luego apilarlos en un único marco 
# de datos mediante la función pd.concat(). Esto se ve así:

#list_of_dataframes = [
  #  pd.read_csv(x) # for x in ["data/01-sales.csv", "data/02-sales.csv", "data/03-sales.csv"]
#]
#sales_files = pd.concat(list_of_dataframes)
#sales_files
#Aquí, usamos una lista de comprensión para leer cada archivo en una lista de marcos de datos,
# y luego pasamos esa lista a pd.concat() para apilarlos en un solo marco de datos.
#Tenga en cuenta que los índices originales de cada archivo se han mantenido.
# Si desea restablecer el índice para que sea único, puede usar el método .reset_index().
#sales_files = sales_files.reset_index(drop=True)

#Si tiene muchos archivos que desea leer, puede resultar complicado escribir sus nombres como una lista. 
# En su lugar, puede usar el paquete glob (integrado en Python) para encontrar los archivos 
# automáticamente mediante la búsqueda de un patrón en los nombres. 
# Tenga en cuenta que puede haber otros archivos CSV en el directorio data/, 
# por lo que aquí especificamos "*-sales.csv" para asegurarnos de obtener solo los archivos que 
# incluyan la palabra "sales". Aquí, "*" actúa como comodín: representa cualquier serie de caracteres.

#import glob

#list_of_csvs = glob.glob("data/*-sales.csv")
#print("List of csvs is:")
#print(list_of_csvs, "\n")
#sales_files = pd.concat([pd.read_csv(x) for x in list_of_csvs])
#sales_files
#Aquí, glob.glob() devuelve una lista de todos los archivos que coinciden con el patrón dado.
# Luego, usamos esa lista para leer y concatenar los archivos como antes.
# Tenga en cuenta que el orden de los archivos en la lista puede no ser el esperado,
# ya que glob los devuelve en el orden en que el sistema operativo los encuentra.


# 8.4. Writing to a file 

#Así como el patrón típico para leer archivos es pd.read_FILETYPE(), donde el tipo de archivo puede ser, 
# por ejemplo, CSV, todas las formas de escribir marcos de datos de Pandas en el disco siguen el patrón 
# DATAFRAME.to_FILETYPE(). Por lo tanto, para escribir nuestros datos de ventas en un archivo CSV, 
# el código será sales_files.to_csv(FILEPATH), donde filepath es la ubicación y el nombre del archivo 
# donde se desea escribir.

#Veamos un ejemplo de escritura de datos en un archivo usando los datos de nuestros estudiantes, 
# cuyos tipos de datos ya configuramos con gran éxito:

#Veamos un ejemplo de escritura de datos en un archivo usando los datos de nuestros estudiantes, 
# en cuyos tipos de datos ya hicimos un buen trabajo al configurarlos:

students.to_csv("data/students-clean.csv")
pd.read_csv("data/students-clean.csv").info()

#¿Has notado algo? ¡Perdimos gran parte del buen trabajo con los tipos de datos! 
# Aunque Pandas adivinó que algunas columnas son enteros, perdimos las variables de cadena y categóricas. 
# Esto se debe a que los archivos de texto plano no pueden contener información contextual 
# (aunque Pandas sí adivinó algunos tipos de datos de columna).
# Si quieres guardar datos en un archivo y que este recuerde los tipos de datos, 
# requiere usar un formato de datos diferente. 
# Para almacenamiento temporal, recomendamos usar el formato feather, ya que es muy rápido 
# e interoperable con otros lenguajes de programación. 
# La interoperabilidad es una buena razón para evitar formatos de archivo específicos de cada lenguaje, 
# como .dta de Stata, .rds de R y .pickle de Python.
# Ten en cuenta que el formato feather tiene una dependencia adicional: un paquete llamado pyarrow. 
# Aquí tienes un ejemplo de escritura en un archivo feather:
students.to_feather("data/students-clean.feather")

#Ahora volvamos a abrir ese archivo de plumas y echemos un vistazo a la información adjunta a él.
pd.read_feather("data/students-clean.feather").info()
#Al guardar en este formato se conserva nuestra información del tipo de datos.