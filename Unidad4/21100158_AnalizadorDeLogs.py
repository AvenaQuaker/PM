from itertools import groupby
from functools import reduce
from typing import List, Tuple, Dict
from operator import itemgetter

# Se Define un log como una tupla inmutable usando el timestamp el tipo y el mensaje
Log = Tuple[str, str, str]

# Funcion pura que agrupa los logs por tipo
def agrupar_por_tipo(logs: List[Log]) -> Dict[str, List[Log]]:
    # Se tiene que ordenar para que el groupby pos funcione
    logs_ordenados = sorted(logs, key=itemgetter(1))
    agrupados = {
        tipo: list(grupo)
        for tipo, grupo in groupby(logs_ordenados, key=itemgetter(1))
    }
    return agrupados

# Función pura que agrupa los logs por fecha
def agrupar_por_fecha(logs: List[Log]) -> Dict[str, List[Log]]:
    logs_ordenados = sorted(logs, key=lambda x: x[0][:10])
    return {
        fecha: list(grupo)
        for fecha, grupo in groupby(logs_ordenados, key=lambda x: x[0][:10])
    }

# Función pura que cuenta la cantidad total de logs de tipo "ERROR"
def contar_errores(logs: List[Log]) -> int:
    return reduce(lambda acc, log: acc + (1 if log[1] == "ERROR" else 0), logs, 0)

# Generar un reporte final
def generar_reporte(logs: List[Log]) -> Tuple[Dict[str, List[Log]], Dict[str, List[Log]], int]:
    return (
        agrupar_por_tipo(logs),
        agrupar_por_fecha(logs),
        contar_errores(logs)
    )

# Ejemplo de uso con logs ficticios (inmutables)
logs_prueba: List[Log] = [
    ("2025-04-03 10:00", "ERROR", "Timeout"),
    ("2025-04-03 10:05", "INFO", "User login"),
    ("2025-04-03 10:10", "WARNING", "Low disk space"),
    ("2025-04-04 11:00", "ERROR", "Connection lost"),
    ("2025-04-04 11:15", "INFO", "File uploaded"),
    ("2025-04-04 11:20", "ERROR", "Disk full"),
]

reporte = generar_reporte(logs_prueba)

# resultados
print("Logs agrupados por tipo:")
for tipo, grupo in reporte[0].items():
    print(f"{tipo}: {len(grupo)} logs")

print("\nLogs agrupados por fecha:")
for fecha, grupo in reporte[1].items():
    print(f"{fecha}: {len(grupo)} logs")

print(f"\nTotal de errores: {reporte[2]}")
