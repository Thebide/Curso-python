import os

def clean_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def ask_amount(message: str, blank = False) -> int:
    try:
        while True:  
            monto = input(message)
            if not monto and blank:
                print("Debe ingresar un valor.")
                continue
            if not monto.isnumeric():
                raise ValueError("El valor ingresado no es admisible, intente nuevamente.")
            monto = int(monto)
            return monto
    except ValueError as ex:
        print(ex)
        return ask_amount(message, blank)

def ask_commentary(message: str = "", blank = True) -> str:
    if len(message) > 120:
        print("Comentario demasiado largo, largo maximo 120 caracteres")
  
