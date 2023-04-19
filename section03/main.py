from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from models import Curso
app = FastAPI()

cursos = {
    1: {
        "titulo": "Programacao",
        "aulas": 112,
        "horas": 58,
    },
    2: {
        "titulo": "teste",
        "aulas": 50,
        "horas": 25,
    }
}

@app.get('/cursos')
async def getCursos():
    return cursos


@app.get('/cursos/{id}')
async def getCurso(id: int):
    try:
        return ({id: cursos[id]})
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso
    

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
