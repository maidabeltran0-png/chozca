# ============================================
# Configuración e importación de librerías
# ============================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro

# Reproducibilidad
np.random.seed(2024)

# ============================================
# Generar datos log-normales (típicos de ingresos)
# ============================================
ingresos = np.random.lognormal(mean=3.5, sigma=0.7, size=500)
datos = pd.DataFrame({"ingreso": ingresos})

# ============================================
# Estadísticas descriptivas
# ============================================
media = np.mean(ingresos)
mediana = np.median(ingresos)
desv_std = np.std(ingresos, ddof=1)
q1 = np.percentile(ingresos, 25)
q3 = np.percentile(ingresos, 75)
iqr = q3 - q1
skewness = np.mean((ingresos - media)**3) / (desv_std**3)
cv = desv_std / media

# ============================================
# Visualización: Histograma + densidad
# ============================================
plt.figure(figsize=(8, 5))
sns.histplot(ingresos, bins=30, kde=True, color="steelblue", alpha=0.7, stat="density")

# Líneas de referencia
plt.axvline(media, color="darkgreen", linestyle="--", linewidth=1.5, label=f"Media = {media:.1f}")
plt.axvline(mediana, color="orange", linestyle="--", linewidth=1.5, label=f"Mediana = {mediana:.1f}")

plt.title("Distribución de Ingresos Mensuales (n=500)", fontsize=14, fontweight="bold")
plt.suptitle(f"Asimetría = {skewness:.2f}", y=0.93, fontsize=10)
plt.xlabel("Ingreso Mensual (miles de pesos)")
plt.ylabel("Densidad")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# ============================================
# Resultados numéricos
# ============================================
print("\n=== ESTADÍSTICAS DESCRIPTIVAS ===")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desv. Estándar: {desv_std:.2f}")
print(f"Q1: {q1:.2f}")
print(f"Q3: {q3:.2f}")
print(f"IQR: {iqr:.2f}")
print(f"Coef. de Variación: {cv:.2f}")
print(f"Asimetría (skewness): {skewness:.2f}")

# ============================================
# Test de normalidad (Shapiro-Wilk)
# ============================================
shapiro_result = shapiro(ingresos)
print(f"\nShapiro-Wilk test p-value: {shapiro_result.pvalue:.6f}")

# ============================================
# Porcentaje de observaciones > media
# ============================================
pct_sobre_media = np.mean(ingresos > media) * 100
print(f"% observaciones > media: {pct_sobre_media:.1f}%")
