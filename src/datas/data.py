from src.helpers.helper_file import read_json
from src.constants import balancedb_json
"""Almacen de los meses y años finalizados con datos
A futuro almacenar en mySQL o mongodb
"""

def initialize_data() -> list[dict]:
    return read_json(balancedb_json)


fmes_ingresos: list[dict] = []

fmes_gastos: list[dict] = []


balancedb: list[dict] = []

