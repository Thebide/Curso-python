from src.helpers.helper_file import read_json
from src.constants import balancedb_json,fmes_gastos_json,fmes_ingresos_json
"""Almacen de los meses y años finalizados con datos
A futuro almacenar en mySQL o mongodb
"""

def initialize_data_balance() -> list[dict]:
    return read_json(balancedb_json)

def initialize_data_ingresos() -> list[dict]:
    return read_json(fmes_ingresos_json)

def initialize_data_gastos() -> list[dict]:
    return read_json(fmes_gastos_json)

 