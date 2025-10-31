
#quiero ingresar un texto 
#aplico boleano false si no es palindromo y true si lo es
#Un palíndromo es una palabra o frase que se lee igual hacia adelante y hacia atrás, 
# ignorando mayúsculas, espacios y signos de puntuación.
def es_palindromo(texto):

    texto_minuscula = texto.lower()
    texto_sin_espacios = texto_minuscula.replace(" ", "")
    return texto_sin_espacios == texto_sin_espacios[::-1]


print(es_palindromo("Anita lava la tina"))  # True
print(es_palindromo("palindromo"))  # False