from fastapi import FastAPI
from variables import letters


app = FastAPI()


@app.get('/')
def getword():
    return (letters)


@app.post('/posted')
def postword():
    return {'a': 1, 'b': 2}
