from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def raiz():
    return {"msg": "alouu"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8080, log_level="info", reload="true")