#funciones puras para validar códigos de matrícula
from typing import Tuple

# Programa simple para validar matriculas de estudiantes de Universidad Random
def validar_longitud(codigo: str) -> bool:
    """Verifica si el código tiene exactamente 8 caracteres."""
    return len(codigo) == 8

def validar_prefijo(codigo: str) -> bool:
    """Verifica si el primer carácter es una letra (A-Z)."""
    return codigo[0].isalpha()

def validar_numeros(codigo: str) -> bool:
    """Verifica si los últimos 7 caracteres son números."""
    return codigo[1:].isdigit()

def validar_codigo_matricula(codigo: Tuple[str]) -> Tuple[str, bool]:
    """Valida un código de matrícula utilizando las tres reglas."""
    return codigo[0], (validar_longitud(codigo[0]) and 
                        validar_prefijo(codigo[0]) and 
                        validar_numeros(codigo[0]))

# Lista de códigos de prueba 
codigos_prueba = (
    ("A1234567",),  # Válido
    ("12345678",),  # Inválido (No inicia con letra)
    ("AB234567",),  # Inválido (Dos letras al inicio)
    ("X9876543",),  # Válido
    ("B12345",),    # Inválido (Menos de 8 caracteres)
)

# pruebas
resultados = [validar_codigo_matricula(c) for c in codigos_prueba]

# resultados
for codigo, es_valido in resultados:
    print(f"Código: {codigo} → {'Válido' if es_valido else 'Inválido'}")
