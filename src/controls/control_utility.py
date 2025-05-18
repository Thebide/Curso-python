import datetime
from datetime import date

from src.datas import balancedb,fmes_ingresos,fmes_gastos
from src.helpers.helper_code import ask_amount,ask_commentary
from src.helpers.helper_file import write_json
from src.constants import fmes_gastos_json,fmes_ingresos_json,balancedb_json


class ControlUtility():
    def add_ingresos(self):
        nuevo_ingreso = dict
        monto = ask_amount("Ingrese un monto: ")
        comentario = ask_commentary("Ingrese un comentario: ")
        nuevo_ingreso = {"Monto": monto, 
                        "Fecha": date.today().isoformat(),
                        "Comentario": comentario }
        fmes_ingresos.append(nuevo_ingreso)
        write_json(fmes_ingresos_json , fmes_ingresos)
        for index, ingreso  in enumerate(fmes_ingresos, start=1):
            print(f"{index}. {{{ingreso['Monto']}, {ingreso['Fecha']}}}")


        
    def delete_ingresos(self):
        try:
            if not fmes_ingresos:
                print("No hay ingresos que eliminar, agrega alguno: ") #pobre de toda pobreza
            else:
                for index, ingreso in enumerate(fmes_ingresos, start =1):
                    print(f"{index}. {{{ingreso['Monto']}, {ingreso['Fecha']}}}")
                delete = ask_amount("Seleccione un valor: ")
                try:
                    fmes_ingresos.pop(delete - 1)
                    write_json(fmes_ingresos_json , fmes_ingresos)
                except IndexError as error:
                    print("Por favor ingrese un numero dentro del rango mostrado", error)
                    return self.delete_ingresos
        except ValueError as error:
            print("Por favor ingrese un numero, NO texto.", error)
            return self.delete_ingresos

    def add_gastos(self):    
        nuevo_egreso = dict
        value = ask_amount("Ingrese un monto: ")
        comentario = ask_commentary("Ingrese un comentario: ")
        nuevo_egreso = {"Monto": value, 
                        "Fecha": date.today().isoformat()}
        fmes_gastos.append(nuevo_egreso)
        write_json(fmes_gastos_json , fmes_gastos)
        for index, gasto  in enumerate(fmes_gastos, start=1):
                print(f"{index}. {{{gasto['Monto']}, {gasto['Fecha']}}}")
    
    
    def delete_gastos(self):
        try:
            if not fmes_gastos:
                print("No hay gastos que eliminar: ") 
            else:
                for index, gasto  in enumerate(fmes_gastos, start=1):
                    print(f"{index}. {{{gasto['Monto']}, {gasto['Fecha']}}}")
                delete = int(input("Elija el numero del ingreso a eliminar: "))
                try:
                    fmes_gastos.pop(delete - 1)
                    write_json(fmes_gastos_json , fmes_gastos)
                except IndexError as error:
                    print("Por favor ingrese un numero dentro del rango mostrado", error)
                return self.delete_gastos
        except ValueError as error:
            print("Por favor ingrese un numero, NO texto.", error)
            return self.delete_gastos

    def status(self):
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
            balancedb = balance
            write_json(balancedb_json, balancedb)
            print(balancedb)
