from dataclasses import dataclass

@dataclass
class Lancamento:
    nome: str
    valor: float
    categoria: str