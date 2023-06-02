from dataclasses import dataclass
from datetime import datetime

@dataclass
class Lancamento:
    nome: str
    valor: float
    tipo: str
    categoria: str
    data_compra: datetime
    data_lancamento: datetime