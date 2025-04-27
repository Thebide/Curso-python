import os

from termcolor import cprint

def main_menu ():
    while True:
        cprint("---Finanzas---", attrs=["bold"])
        cprint("1. Ver estado de cuenta", "white")
        cprint("2. Agregar un ingreso", "white")
        cprint("3. Editar un ingreso", "white")
        cprint("4. Eliminar un ingreso","white")
        cprint("5. Agregar un gasto","white")
        cprint("6. Editar un gasto","white")
        cprint("7. Eliminar un gasto","white")
        cprint("8. Agregar una inversión","white")
        cprint("9. Editar una inversión","white")
        cprint("10. Eliminar una inversión","white")        
        cprint("0. Salir del programa","red")
        

        option = input("Elija su opción [0-10]: ")
