import string

def eliminar_puntuacion(texto):
    return texto.translate(str.maketrans("","",string.punctuation))

def a_minusculas(texto):
    return texto.lower()

def eliminar_stopwords(texto,stopwords):
    return " ".join([palabra for palabra in texto.split() if palabra not in stopwords])    

#Composicion normal
def procesar_texto(texto,stopwords):
    texto = eliminar_puntuacion(texto)
    texto = a_minusculas(texto)
    texto = eliminar_stopwords(texto,stopwords)
    return texto

#Usando Tool.zCompose
from toolz import compose
procesar_texto = compose(
    lambda t:eliminar_stopwords(t,["el","la","de"]),
    a_minusculas,
    eliminar_puntuacion
)

texto = "El rapido Zorro Marron, salta sobre el perro perezeoso"
print(procesar_texto(texto)) # rapido zorro marron salta sobre perro perezeoso