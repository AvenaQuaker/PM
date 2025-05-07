from dataclasses import dataclass
from typing import List, Union

# dataclasses para simplificar la creación de clasess
@dataclass(frozen=True)
class Archivo:
    nombre: str
    tamano: int 

@dataclass(frozen=True)
class Directorio:
    nombre: str
    contenido: List[Union['Archivo', 'Directorio']]

# Función que Calcula el tamaño total de un directorio
def calcular_tamano_total(elemento: Union[Archivo, Directorio]) -> int:
    if isinstance(elemento, Archivo):
        return elemento.tamano
    elif isinstance(elemento, Directorio):
        return sum(calcular_tamano_total(item) for item in elemento.contenido)

# Función que Busca un archivo o directorio por nombre 
def buscar_por_nombre(elemento: Union[Archivo, Directorio], nombre: str) -> Union[Archivo, Directorio, None]:
    if elemento.nombre == nombre:
        return elemento
    if isinstance(elemento, Directorio):
        for item in elemento.contenido:
            resultado = buscar_por_nombre(item, nombre)
            if resultado:
                return resultado
    return None

# Función que Lista todos los archivos del sistemaa
def listar_archivos(elemento: Union[Archivo, Directorio]) -> List[str]:
    if isinstance(elemento, Archivo):
        return [elemento.nombre]
    elif isinstance(elemento, Directorio):
        archivos = []
        for item in elemento.contenido:
            archivos.extend(listar_archivos(item))
        return archivos

# Ejemplo
archivo1 = Archivo("notas.txt", 50)
archivo2 = Archivo("foto.jpg", 200)
archivo3 = Archivo("script.py", 15)

subdir = Directorio("Documentos", [archivo1, archivo3])
raiz = Directorio("MiPC", [archivo2, subdir])

# Pruebas
print("Tamaño total:", calcular_tamano_total(raiz)) 
print("Buscar 'foto.jpg':", buscar_por_nombre(raiz, "foto.jpg"))  
print("Listar archivos:", listar_archivos(raiz))  
