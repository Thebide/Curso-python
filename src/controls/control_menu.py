from termcolor import cprint

# from src.controls.control_utility import status,add_ingresos,delete_ingresos,add_gastos,delete_gastos
from src.controls import funtion
from src.helpers.helper_code import clean_screen

def main_menu ():
    while True:
        cprint("---Finanzas---", attrs=["bold"])
        cprint("1. Ver estado de cuenta", "white")
        cprint("2. Agregar un ingreso","white")
        cprint("3. Eliminar un ingreso","white")
        cprint("4. Agregar un gasto","white")
        cprint("5. Eliminar un gasto","white")
        print()
        cprint("0. Salir del programa","red")
        

        option = input("Elija su opción [0-5]: ")
        clean_screen()
        match option:
            case "1": funtion.status()
            case "2": funtion.add_ingresos()
            case "3": funtion.delete_ingresos()
            case "4": funtion.add_gastos()
            case "5": funtion.delete_gastos()
            case "0": 
                print("Salida del programa")
                break
            case _: print("Opción no valida")


