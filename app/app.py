import random
import string

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def getword():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(10))


@app.post('/posted')
def postword():
    return {'a': 1, 'b': 2}
