"""Almacen de los meses y años finalizados con datos
A futuro almacenar en mySQL o mongodb 
"""
#balancedb almacena los ultimos datos de cada mes para un calculo anual
balancedb: list[dict] = []

"""
fmes (general) 
id(operación diaria): int (autogenerado) (enumerate???)
monto = int
fecha = dia/mes/año 
""" 
#sub lista (mes) almacena todos los ingresos diarios para luego realizar un balance que se almacena en "balancedb"
fmes_ingresos: list[dict] = [
    {"Monto": 890.00, "Fecha": "23/03/24"},
    {"Monto": 1200.50, "Fecha": "03/04/24"},
    {"Monto": 999.99, "Fecha": "29/04/24"},
    {"Monto": 1500.00, "Fecha": "02/05/24"} ]

fmes_gastos: list[dict] = [
    {"Monto": -420.30, "Fecha": "10/03/24"},
    {"Monto": -350.75, "Fecha": "15/04/24"},
    {"Monto": -275.40, "Fecha": "12/05/24"} ]
