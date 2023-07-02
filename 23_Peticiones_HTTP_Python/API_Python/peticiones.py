'''

Peticiones HTTP

'''


from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    name: str
    url: str

app = FastAPI()

users_list = [
    User(id=1, name="breativo", url="https://breativo.com"),
    User(id=2, name="breativo", url="https://breativo.es"),
    User(id=3, name="breativo", url="https://breativo.dev")
]

# Operación GET para obtener todos los usuarios
@app.get("/")
async def get_users():
    return users_list

# Operación GET para obtener un usuario por su ID
@app.get("/user/{user_id}")
async def get_user(user_id: int):
    for user in users_list:
        if user.id == user_id:
            return user
    return {"error": "Usuario no encontrado"}

# Operación POST para crear un nuevo usuario
@app.post("/users")
async def create_user(user: User):
    users_list.append(user)
    return user

# Operación PUT para actualizar un usuario existente
@app.put("/users/{user_id}")
async def update_user(user_id: int, updated_user: User):
    for user in users_list:
        if user.id == user_id:
            user.name = updated_user.name
            user.url = updated_user.url
            return user
    return {"error": "Usuario no encontrado"}

# Operación DELETE para eliminar un usuario por su ID
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for user in users_list:
        if user.id == user_id:
            users_list.remove(user)
            return {"message": "Usuario eliminado"}
    return {"error": "Usuario no encontrado"}


