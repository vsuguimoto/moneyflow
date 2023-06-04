from dataclasses import dataclass
from datetime import datetime

@dataclass
class Lancamento:
    nome: str
    valor: float
    tipo: str
    data_compra: datetime
    categoria_id: int
    pessoa_id: int