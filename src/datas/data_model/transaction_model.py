from typing import Optional

class Transaction():
    def __init__(self, monto: int, fecha: str, comentario: Optional[str]= ""):
        self.monto: int = monto 
        self.fecha: str = fecha
        self.comentario: str = comentario
    
    @property
    def monto(self) -> int:
        return self.monto
    
    @monto.setter
    def monto(self, monto: int) -> None:
        self.monto = monto
    
    @property
    def fecha(self) -> str:
        return self.fecha