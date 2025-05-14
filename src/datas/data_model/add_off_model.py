from typing import Optional

from .transaction_model import Transaction

class Add_Off(Transaction):
    def __init__(self, monto: int, fecha: str, comentario: Optional[str]):
        super().__init__(monto, fecha, comentario)
    
    def to_json(self):
        return self.__dict__