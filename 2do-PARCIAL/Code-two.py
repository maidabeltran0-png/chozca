# ============================================
# CONFIGURACIÓN
# ============================================
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import random

# Estilo general
sns.set_theme(style="whitegrid")
np.random.seed(2024)

# ============================================
# GENERACIÓN DE DATOS
# ============================================
n = 85

# Ingresos ANTES del programa (desempleados o subempleados)
ingreso_antes = np.random.normal(loc=25, scale=8, size=n)

# Efecto del programa: aumento promedio de 6.5 con variabilidad
efecto_individual = np.random.normal(loc=6.5, scale=4.5, size=n)

# Ingresos DESPUÉS
ingreso_despues = ingreso_antes + efecto_individual

# Crear DataFrame
datos = pd.DataFrame({
    "participante": np.arange(1, n + 1),
    "antes": ingreso_antes,
    "despues": ingreso_despues
})
datos["diferencia"] = datos["despues"] - datos["antes"]

# ============================================
# ESTADÍSTICAS DESCRIPTIVAS
# ============================================
print("=== ESTADÍSTICAS DESCRIPTIVAS ===\n")

def resumen(variable, nombre):
    print(f"{nombre}:")
    print(f"  Media: {np.mean(variable):.2f} mil pesos")
    print(f"  Mediana: {np.median(variable):.2f} mil pesos")
    print(f"  SD: {np.std(variable, ddof=1):.2f}\n")

resumen(datos["antes"], "ANTES del programa")
resumen(datos["despues"], "DESPUÉS del programa")

print("DIFERENCIAS (Después - Antes):")
print(f"  Media: {np.mean(datos['diferencia']):.2f} mil pesos")
print(f"  Mediana: {np.median(datos['diferencia']):.2f} mil pesos")
print(f"  SD: {np.std(datos['diferencia'], ddof=1):.2f}")
print(f"  Min: {np.min(datos['diferencia']):.2f}")
print(f"  Max: {np.max(datos['diferencia']):.2f}")

pct_mejora = np.mean(datos["diferencia"] > 0) * 100
print(f"  % con mejora (diferencia > 0): {pct_mejora:.1f}%\n")

# ============================================
# TEST T PAREADO
# ============================================
print("=== TEST T PAREADO ===\n")
print("H0: La media de las diferencias es 0 (no hay efecto)")
print("H1: La media de las diferencias ≠ 0 (hay efecto)\n")

t_stat, p_value = stats.ttest_rel(datos["despues"], datos["antes"])
df = n - 1
mean_diff = np.mean(datos["diferencia"])
sd_diff = np.std(datos["diferencia"], ddof=1)
ci_95 = stats.t.interval(0.95, df=df, loc=mean_diff, scale=sd_diff / np.sqrt(n))

print(f"Estadístico t: {t_stat:.3f}")
print(f"Grados de libertad: {df}")
print(f"P-valor: {p_value:.4f}\n")
print(f"Diferencia promedio: {mean_diff:.2f} mil pesos")
print(f"IC 95%: [{ci_95[0]:.2f}, {ci_95[1]:.2f}]\n")

# Tamaño del efecto (Cohen's d para muestras pareadas)
cohens_d = mean_diff / sd_diff
print(f"Tamaño del efecto (Cohen's d): {cohens_d:.3f}")
if abs(cohens_d) < 0.2:
    print("  Interpretación: efecto pequeño")
elif abs(cohens_d) < 0.5:
    print("  Interpretación: efecto pequeño-moderado")
elif abs(cohens_d) < 0.8:
    print("  Interpretación: efecto moderado")
else:
    print("  Interpretación: efecto grande")
print()

# ============================================
# VERIFICACIÓN DE SUPUESTOS
# ============================================
print("=== VERIFICACIÓN DE SUPUESTOS ===\n")

# Test de normalidad de las DIFERENCIAS
w_stat, p_shapiro = stats.shapiro(datos["diferencia"])
print("Shapiro-Wilk test (normalidad de diferencias):")
print(f"  W = {w_stat:.4f}")
print(f"  p-valor = {p_shapiro:.4f}")

if p_shapiro > 0.05:
    print("  ✓ No se rechaza normalidad (p > 0.05)\n")
else:
    print("  ✗ Se rechaza normalidad (p < 0.05)")
    print("  Considerar test de Wilcoxon como alternativa\n")

# Test de Wilcoxon (no paramétrico)
w_stat, p_wilcox = stats.wilcoxon(datos["despues"], datos["antes"])
print("Test de Wilcoxon (alternativa no paramétrica):")
print(f"  Estadístico W = {w_stat}")
print(f"  p-valor = {p_wilcox:.4f}\n")

# ============================================
# VISUALIZACIONES
# ============================================

# 1. Boxplot comparativo
datos_long = datos.melt(
    id_vars="participante",
    value_vars=["antes", "despues"],
    var_name="momento",
    value_name="ingreso"
)

plt.figure(figsize=(7,5))
sns.boxplot(data=datos_long, x="momento", y="ingreso", palette=["coral", "steelblue"], boxprops=dict(alpha=0.7)) # ✅ transparencia aplicada correctamente)
sns.stripplot(data=datos_long, x="momento", y="ingreso", color="black", alpha=0.3, size=3, jitter=0.2)
plt.title(f"Comparación de Ingresos: Antes vs Después del Programa\nn = {n} participantes", fontsize=12, fontweight="bold")
plt.xlabel("Momento de Medición")
plt.ylabel("Ingreso Mensual (miles de pesos)")
plt.tight_layout()
plt.show()

# 2. Histograma de las diferencias
plt.figure(figsize=(7,5))
sns.histplot(datos["diferencia"], bins=20, kde=True, color="darkgreen", alpha=0.7, stat="density")
plt.axvline(0, linestyle="--", color="black", linewidth=1)
plt.axvline(mean_diff, color="blue", linewidth=1)
plt.title(f"Distribución de las Diferencias (Después - Antes)\nDiferencia media = {mean_diff:.2f} mil pesos | p-valor = {p_value:.3f}", fontsize=12, fontweight="bold")
plt.xlabel("Cambio en Ingreso (miles de pesos)")
plt.ylabel("Densidad")
plt.tight_layout()
plt.show()

# 3. Gráfico de líneas pareadas (muestra aleatoria de 30 participantes)
random.seed(123)
muestra_visual = random.sample(range(n), min(30, n))
datos_muestra = datos.iloc[muestra_visual]
datos_muestra_long = datos_muestra.melt(
    id_vars="participante",
    value_vars=["antes", "despues"],
    var_name="momento",
    value_name="ingreso"
)

plt.figure(figsize=(7,5))
for i, df_i in datos_muestra_long.groupby("participante"):
    plt.plot(df_i["momento"], df_i["ingreso"], color="gray", alpha=0.3)
sns.scatterplot(data=datos_muestra_long, x="momento", y="ingreso", hue="momento",
                palette={"antes": "coral", "despues": "steelblue"}, s=60, alpha=0.7)
plt.title("Trayectorias Individuales (muestra de 30 participantes)\nCada línea representa un participante", fontsize=12, fontweight="bold")
plt.xlabel("Momento de Medición")
plt.ylabel("Ingreso Mensual (miles de pesos)")
plt.legend([], [], frameon=False)
plt.tight_layout()
plt.show()

# 4. Q-Q plot de las diferencias
plt.figure(figsize=(6,5))
stats.probplot(datos["diferencia"], dist="norm", plot=plt)
plt.title("Q-Q Plot de las Diferencias\nVerificación de normalidad", fontsize=12, fontweight="bold")
plt.xlabel("Cuantiles Teóricos")
plt.ylabel("Cuantiles de la Muestra")
plt.tight_layout()
plt.show()
