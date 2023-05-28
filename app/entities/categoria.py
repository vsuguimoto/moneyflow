from dataclasses import dataclass
from typing import Optional

@dataclass
class Categoria:
    nome: str
    descricao: Optional[str] = 'Vazio'