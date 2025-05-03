import datetime
from datetime import date

from data import balancedb,fmes_ingresos,fmes_gastos

def add_ingresos():
    nuevo_ingreso = dict
    monto = int(input("Ingrese monto:"))
    if monto > 0:
            nuevo_ingreso = {"Monto": monto, 
                            "Fecha": date.today().isoformat()}
            fmes_ingresos.append(nuevo_ingreso)
            for index, ingreso  in enumerate(fmes_ingresos, start=1):
                print(f"{index}. {fmes_ingresos}")
    else:
            print("El valor ingresado tiene que ser mayor a 0 (cero).")
   
def delete_ingresos():
    if not fmes_ingresos:
         print("No hay ingresos que eliminar, agrega alguno: ") #pobre de toda pobreza
    else:
        for index, ingreso in enumerate(fmes_ingresos, start =1):
            print(f"{index}. {fmes_ingresos}")

def add_gastos():
    nuevo_egreso = dict
    monto = -int(input("Ingrese monto:"))
    if monto < 0:
        nuevo_egreso = {"Monto": monto, 
                        "Fecha": date.today().isoformat()}
        fmes_gastos.append(nuevo_egreso)
        for index, gasto  in enumerate(fmes_gastos, start=1):
                print(f"{index}. {fmes_gastos}")
    else:
        print("El valor ingresado tiene que ser positivo.")

def delete_gastos():
    if not fmes_gastos:
         print("No hay gastos que eliminar: ") 
    else:
        for index, gasto  in enumerate(fmes_gastos, start=1):
            print(f"{index}. {fmes_gastos}")

def status():
    gastos_totales = 0
    ingresos_totales = 0
    balance = dict
    if not fmes_gastos and not fmes_ingresos:
         print("No hay gastos ni ingresos por lo tanto: 0 pesos")
    else:
        for ingreso in fmes_ingresos:
             ingresos_totales += ingreso["Monto"]
        print(ingresos_totales)
        for gasto in fmes_gastos:
             gastos_totales += gasto["Monto"]
        print(gastos_totales)
        total = ingresos_totales + gastos_totales

        balance = {"balance": total, 
                "fecha": date.today().isoformat()}
        
        balancedb = balance, date.today().isoformat()
        print(balancedb)