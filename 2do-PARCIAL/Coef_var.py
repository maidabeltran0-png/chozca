# Ingresar valores para A
media_a = float(input("Ingrese la media de A: "))
desvio_a = float(input("Ingrese el desvío estándar de A: "))

# Ingresar valores para B
media_b = float(input("Ingrese la media de B: "))
desvio_b = float(input("Ingrese el desvío estándar de B: "))

# Calcular coeficiente de variación
coef_variacion_a = desvio_a / media_a
coef_variacion_b = desvio_b / media_b

# Calcular cociente
cociente = coef_variacion_a / coef_variacion_b
print(f"\nCociente de coeficientes de variación: {cociente:.2f}")

# Comparar variabilidad
if cociente > 1:
    print("La variable A tiene una variabilidad mayor que B")
else:
    print("La variable A no tiene una variabilidad mayor que B")

# Mostrar coeficientes de variación
print(f"El coeficiente de variación del Conjunto A y B es respectivamente: {coef_variacion_a:.2f} y {coef_variacion_b:.2f}")
