#4.4.1. Creating New Columns
#vamos a crear nuevas columnas, usando info existente. Dado un dataframe df
#crear una nueva columnas con el mismo valor repetido
#usando corchetes con un string 
import numpy as np
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
df.head()
print(df)

df["new_column0"] = 5
