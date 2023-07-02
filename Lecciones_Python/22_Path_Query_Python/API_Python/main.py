'''

Path and Query

'''

# Path
# Parámetro
from fastapi import FastAPI
app = FastAPI()
@app.get("/users/{id}")
async def read_item(id):
    return {"item_id": id}


# Parámetro tipados
from fastapi import FastAPI
app = FastAPI()
@app.get("/items/{id}")
async def read_item(id: str):
    return {"item_id": id}


# Parámetros por defecto
from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    my_name = "breativo"
    
app = FastAPI()

@app.get("/models/{name}")
async def get_model(name: ModelName):
    if name is ModelName.my_name:
        return {"name": name, "message": "Hola breativo."}


# Query
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    url: str

app = FastAPI()

users_list = [User(id=1, name="breativo", url="https://breativo.com"),
              User(id=2, name="breativo", url="https://breativo.es"),
              User(id=3, name="breativo",  url="https://breativo.dev")]

@app.get('/userquery')
async def user (id:int):
    users=filter(lambda user: user.id ==id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el registro"}



