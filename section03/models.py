from typing import Optional
from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value: str):
        palavras = value
        if len(palavras) < 1:
            raise ValueError('O titulo não pode estar vazio')
        
        return value

cursos = [
    Curso(id=1, titulo="Programacao", aulas=112, horas=58),
    Curso(id=2, titulo="teste", aulas=50, horas=25),
    Curso(id=3, titulo="blabla", aulas=25, horas=13)
]