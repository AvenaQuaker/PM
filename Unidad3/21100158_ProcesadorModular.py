import string
from collections import Counter
from toolz import compose

# funcion que elimina los signos de puntuacion
def limpiar_puntuacion(texto):
    return texto.translate(str.maketrans('', '', string.punctuation))

# funcion que convierte todo a minusculas
def normalizar_minusculas(texto):
    return texto.lower()

# funcion que elimina todas las papalabras de menos de 4 letras
def eliminar_palabras_cortas(texto, min_largo=4):
    return ' '.join([p for p in texto.split() if len(p) >= min_largo])

# funcion que cuenta la veces q se repite una palabra en el texto
def contar_palabras(texto):
    return Counter(texto.split())

# Pipeline funcional para el procesamiento de texto
pipeline_procesamiento = compose(
    contar_palabras,
    lambda t: eliminar_palabras_cortas(t, 4),
    normalizar_minusculas,
    limpiar_puntuacion
)

# Ejemplo
if __name__ == "__main__":
    texto_ejemplo = "Trigger lo mas duro del sistema, no hay nada que hacer, no hay nada que hacer, no hay nada que hacer"
    resultado = pipeline_procesamiento(texto_ejemplo)
    print(resultado)
