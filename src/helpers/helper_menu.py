import os

def clean_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def ask_amount(message: str, blank = False) -> int:
    try:
        while True:  
            value = input(message)
            if not value and blank:
                print("Debe ingresar un valor.")
                continue
            if not value.isnumeric():
                raise ValueError("El valor ingresado no es admisible, intente nuevamente.")
            value = int(value)
            return value
    except ValueError as ex:
        print(ex)
        return ask_amount(message, blank)