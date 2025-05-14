from typing import Optional

from .transaction_model import Transaction

class Investment(Transaction):
    def __init__(self, monto: int, TNA: float, periodo: int, fecha: str, comentario: Optional[str]):
        super().__init__(monto, fecha, comentario)
        self.TNA: int = TNA
        self.periodo: int = periodo
    
    @property
    def TNA(self) -> float:
        return self.TNA
    
    @TNA.setter
    def TNA(self, TNA: float) -> None:
        self.TNA = TNA

    @property
    def periodo(self) -> int:
        return self.periodo
    
    @periodo.setter
    def periodo(self, periodo: int) -> None:
        self.periodo = periodo