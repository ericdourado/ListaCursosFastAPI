from typing import List, Optional
from fastapi import FastAPI, HTTPException, status, Response, Path, Query, Header
from fastapi.responses import JSONResponse
from models import Curso, cursos
app = FastAPI()


@app.get('/cursos')
async def getCursos():
    return cursos


@app.get('/cursos/{id}')
async def getCurso(id: int = Path(default=None, title='Id do curso', description='ID DO CURSO', gt=0, lt=3)):
    try:
        return ({id: cursos[id]})
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos.insert(next_id,curso)
    # del curso.id
    return curso
    
@app.put('/cursos/{id}')
async def put_curso(id: int, curso: Curso):
    if id in cursos:
        cursos[id] = curso
        del curso.id
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id do curso digitado não existe: {id}')
    return curso


@app.delete('/cursos/{id}')
async def delete_curso(id: int):
    if id in cursos:
        del cursos[id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id do curso digitado não existe: {id}')
    

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True)
