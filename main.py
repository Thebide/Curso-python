
def run():
    while True:
        cdprint("---Finanzas---", attrs=["bold","blink"])
        cdprint("1. Ver estado de cuenta", "white")
        cdprint("2. Agregar un ingreso", "white")
        cdprint("3. Editar un ingreso", "white")
        cdprint("4. Eliminar un ingreso","white")
        cdprint("5. Agregar un gasto","white")
        cdprint("6. Editar un gasto","white")
        cdprint("7. Eliminar un gasto","white")
        cdprint("8. Agregar una inversión","white")
        cdprint("9. Editar una inversión","white")
        cdprint("10. Eliminar una inversión","white")        
        cdprint("0. Salir del programa","white")
if __name__ == "__main__":
    run()