# =========================
# INFERENCIA ESTADÍSTICA EN PYTHON
# =========================

#1 IMPORTAR LIBRERIAS
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns

# Opcional: gráficos más bonitos
sns.set_theme(style="whitegrid")
import skimpy as sk

#2 CARGAR DATOS
# Cambia "students.csv" por tu archivo
students = pd.read_csv("students.csv")

# Ver primeras filas
students.head()

# Resumen de columnas y tipos
students.info()

#3 ESTADISTICA DESCRIPTIVA
# Resumen numérico
students.describe()

# Medidas de tendencia central y dispersión
students['age'].mean()
students['age'].median()
students['age'].mode()
students['age'].std()
students['age'].var()

# Histograma de la edad
sns.histplot(students['age'], kde=True)
plt.show()

# Boxplot por grupo
sns.boxplot(x='meal_plan', y='age', data=students)
plt.show()

#4 LIMPIAR Y TRANSFORMAR DATOS
# Convertir columnas a tipos adecuados
students["favourite_food"] = students["favourite_food"].astype("string")
students["meal_plan"] = students["meal_plan"].astype("category")
students = students.astype({"student_id": "int", "full_name": "string", "age": "int"})

# Reemplazar valores mixtos
students["age"] = students["age"].replace("five", 5)

# Verificación
students.info()

#5 INTERVALOS DE CONFIANZA

# Para la media de la edad
n = len(students['age'])
mean = students['age'].mean()
std = students['age'].std(ddof=1)
conf_level = 0.95

z = stats.norm.ppf(1 - (1-conf_level)/2)
margin_error = z * (std / np.sqrt(n))
lower = mean - margin_error
upper = mean + margin_error

print(f"Intervalo de confianza 95% para la edad: ({lower:.2f}, {upper:.2f})")

# Alternativa usando t de scipy
stats.t.interval(conf_level, n-1, loc=mean, scale=std/np.sqrt(n))

#6 TEST DE HIPOTESIS
# Prueba t de una muestra
t_stat, p_val = stats.ttest_1samp(students['age'], popmean=10)
print(f"T-statistic: {t_stat:.3f}, p-value: {p_val:.3f}")

# Prueba t de dos muestras independientes
t_stat, p_val = stats.ttest_ind(
    students['age'][students['meal_plan']=='standard'],
    students['age'][students['meal_plan']=='premium'],
    equal_var=False
)
print(f"T-test 2 muestras: t={t_stat:.3f}, p={p_val:.3f}")

# Prueba de chi-cuadrado
contingency = pd.crosstab(students['meal_plan'], students['favourite_food'])
chi2, p, dof, expected = stats.chi2_contingency(contingency)
print(f"Chi2={chi2:.3f}, p={p:.3f}")

#7 CORRELACIÓN
# Pearson
r, p = stats.pearsonr(students['age'], students['student_id'])
print(f"Pearson r={r:.3f}, p={p:.3f}")

# Spearman
rho, p = stats.spearmanr(students['age'], students['student_id'])
print(f"Spearman rho={rho:.3f}, p={p:.3f}")

#8 REGRESIÓN
# Simple
model = smf.ols('age ~ student_id', data=students).fit()
print(model.summary())

# Múltiple (si hubiera más columnas numéricas)
# model = smf.ols('age ~ student_id + other_column', data=students).fit()
# print(model.summary())

#9 INFERENCIA NO PARAMETRICA 
# Mann-Whitney U (dos grupos independientes)
group1 = students['age'][students['meal_plan']=='standard']
group2 = students['age'][students['meal_plan']=='premium']
stat, p = stats.mannwhitneyu(group1, group2)
print(f"Mann-Whitney U: stat={stat}, p={p}")

# Kruskal-Wallis (más de dos grupos)
# stat, p = stats.kruskal(group1, group2, group3)

#10 GUARDAR DATAFRAME MODIFICADO
import os

# Crear carpeta 'data' si no existe
os.makedirs("data", exist_ok=True)

# Guardar CSV
students.to_csv("data/students-clean.csv", index=False)

# Verificación
df_check = pd.read_csv("data/students-clean.csv")
df_check.info()










