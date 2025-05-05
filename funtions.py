import datetime
from datetime import date

from data import balancedb,fmes_ingresos,fmes_gastos


nuevo_ingreso = dict
def add_ingresos():
    try:    
        monto = int(input("Ingrese monto:"))
        if monto >= 0:
                nuevo_ingreso = {"Monto": monto, 
                                "Fecha": date.today().isoformat()}
                fmes_ingresos.append(nuevo_ingreso)
                for index, ingreso  in enumerate(fmes_ingresos, start=1):
                    print(f"{index}. {{{ingreso['Monto']}, {ingreso['Fecha']}}}")
        else:
                print("El valor ingresado tiene que ser mayor a 0 (cero).")
        return
    except ValueError as error:
         print("Por favor ingrese un numero, NO texto.", error)
         return add_ingresos
    
def delete_ingresos():
    try:
        if not fmes_ingresos:
            print("No hay ingresos que eliminar, agrega alguno: ") #pobre de toda pobreza
        else:
            for index, ingreso in enumerate(fmes_ingresos, start =1):
                print(f"{index}. {{{ingreso['Monto']}, {ingreso['Fecha']}}}")
                delete = int(input("Elija el numero del ingreso a eliminar: "))
                try:
                    fmes_ingresos.pop(delete-1)
                except IndexError as error:
                     print("Por favor ingrese un numero dentro del rango mostrado", error)
                     return delete_ingresos
        return
    except ValueError as error:
         print("Por favor ingrese un numero, NO texto.", error)
         return delete_ingresos

def add_gastos():
    try:
        nuevo_egreso = dict
        monto = -int(input("Ingrese monto:"))
        if monto <= 0:
            nuevo_egreso = {"Monto": monto, 
                            "Fecha": date.today().isoformat()}
            fmes_gastos.append(nuevo_egreso)
            for index, gasto  in enumerate(fmes_gastos, start=1):
                    print(f"{index}. {{{gasto['Monto']}, {gasto['Fecha']}}}")
        else:
            print("El valor ingresado tiene que ser positivo.")
            return
    except ValueError as error:
         print("Por favor ingrese un numero, NO texto.", error)
         return add_gastos

def delete_gastos():
    try:
        if not fmes_gastos:
            print("No hay gastos que eliminar: ") 
        else:
            for index, gasto  in enumerate(fmes_gastos, start=1):
                try:
                    print(f"{index}. {{{gasto['Monto']}, {gasto['Fecha']}}}")
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
