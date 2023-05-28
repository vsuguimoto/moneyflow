from dataclasses import dataclass

@dataclass
class Lancamento:
    nome: str
    valor: float
    tipo: str
    categoria: str