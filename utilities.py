import os

from termcolor import cprint
from funtions import status,add_ingresos,delete_ingresos,add_gastos,delete_gastos,add_inversiones,delete_inversiones

def main_menu ():
    while True:
        cprint("---Finanzas---", attrs=["bold"])
        cprint("1. Ver estado de cuenta", "white")
        cprint("2. Agregar un ingreso","white")
        cprint("3. Eliminar un ingreso","white")
        cprint("4. Agregar un gasto","white")
        cprint("5. Eliminar un gasto","white")
        cprint("6. Agregar una inversión","white")
        cprint("7. Eliminar una inversión","white")
        print()
        cprint("0. Salir del programa","red")
        

        option = input("Elija su opción [0-7]: ")
        clean_screen()
        match option:
            case "1": status
            case "2": add_ingresos
            case "3": delete_ingresos
            case "4": add_gastos
            case "5": delete_gastos
            case "6": add_inversiones
            case "7": delete_inversiones  
            case "0": 
                print("Salida del programa")
                break
            case _: print("Opción no valida")


def clean_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
