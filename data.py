"""Almacen de los meses y años finalizados con datos
A futuro almacenar en mySQL o mongodb 
"""
#balancedb almacena los ultimos datos de cada mes para un calculo anual
balancedb = list[dict] = []

"""
fmes (general) 
id(operación diaria): int (autogenerado) (enumerate???)
monto = int
fecha = dia/mes/año 
""" 
#sub lista (mes) almacena todos los ingresos diarios para luego realizar un balance que se almacena en "balancedb"
fmes_ingresos = list[dict] = []
fmes_gastos = list[dict] = []
fmes_inversiones = list[dict] = []