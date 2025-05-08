import datetime
from datetime import date

from src.datas.data import balancedb,fmes_ingresos,fmes_gastos
from src.helpers.helper_menu import ask_amount



def add_ingresos():
    nuevo_ingreso = dict
    value = ask_amount("Ingrese un monto: ")
    nuevo_ingreso = {"Monto": value, 
                    "Fecha": date.today().isoformat()}
    fmes_ingresos.append(nuevo_ingreso)
    for index, ingreso  in enumerate(fmes_ingresos, start=1):
        print(f"{index}. {{{ingreso['Monto']}, {ingreso['Fecha']}}}")


    
def delete_ingresos():
    try:
        if not fmes_ingresos:
            print("No hay ingresos que eliminar, agrega alguno: ") #pobre de toda pobreza
        else:
            for index, ingreso in enumerate(fmes_ingresos, start =1):
                print(f"{index}. {{{ingreso['Monto']}, {ingreso['Fecha']}}}")
            delete = ask_amount("Seleccione un valor: ")
            try:
                fmes_ingresos.pop(delete - 1)
            except IndexError as error:
                print("Por favor ingrese un numero dentro del rango mostrado", error)
                return delete_ingresos
        return
    except ValueError as error:
         print("Por favor ingrese un numero, NO texto.", error)
         return delete_ingresos

def add_gastos():    
    nuevo_egreso = dict
    value = ask_amount("Ingrese un monto: ")
    nuevo_egreso = {"Monto": value, 
                    "Fecha": date.today().isoformat()}
    fmes_gastos.append(nuevo_egreso)
    for index, gasto  in enumerate(fmes_gastos, start=1):
            print(f"{index}. {{{gasto['Monto']}, {gasto['Fecha']}}}")
   
 
def delete_gastos():
    try:
        if not fmes_gastos:
            print("No hay gastos que eliminar: ") 
        else:
            for index, gasto  in enumerate(fmes_gastos, start=1):
                print(f"{index}. {{{gasto['Monto']}, {gasto['Fecha']}}}")
            delete = int(input("Elija el numero del ingreso a eliminar: "))
            try:
                 fmes_ingresos.pop(delete - 1)
            except IndexError as error:
                print("Por favor ingrese un numero dentro del rango mostrado", error)
            return delete_gastos
            return
    except ValueError as error:
         print("Por favor ingrese un numero, NO texto.", error)
         return delete_gastos

def status():
    gastos_totales = 0
    ingresos_totales = 0
    balance = dict
    global balancedb
    if not fmes_gastos and not fmes_ingresos:
         print("No hay gastos ni ingresos por lo tanto: 0 pesos")
    else:
        for ingreso in fmes_ingresos:
             ingresos_totales += ingreso["Monto"]
        print(f"Los ingresos del mes fuero: {ingresos_totales}")
        for gasto in fmes_gastos:
             gastos_totales += gasto["Monto"]
        print(f"Los gastos del mes fuero: {gastos_totales}")
        total = ingresos_totales - gastos_totales

        balance = {"balance": total, 
                "fecha": [date.today().year, date.today().month]}
        
        if not balancedb:
            balancedb.append(balance)
        else:
            for fecha in balance:
                date.today().year, date.today().month != fecha[fecha]
                balancedb = balance
        print(balancedb)
