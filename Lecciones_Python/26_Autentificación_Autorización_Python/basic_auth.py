'''

API

'''

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    id: str
    name: str
    disabled: bool
    password: str

user_db = {
    'breativo': {
        'id': '1',
        'name': 'breativo',
        'disabled': True,
        'password': '0000'
    },
    'mario': {
        'id': '2',
        'name': 'mario',
        'disabled': True,
        'password': '1234'
    },
}

# Búsqueda de usuarios
def search_user(name: str):
    if name in user_db:
        user_data = user_db[name]
        user_data['password'] = str(user_data['password'])  # Convertir a cadena
        return User(**user_data)

# Criterio de dependencia
async def current_user(token: str = Depends(oauth2_scheme)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrecto la autorización",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# Operación de autentificación
@app.post('/login')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    username = form.username
    password = form.password

    if not username or not password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Campos de formulario incompletos",
        )

    user = search_user(username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario incorrecto",
        )

    if not password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password incorrecto",
        )

    return {"access_token": user.name, "token_type": "bearer"}

# Operación autorización
@app.get("/user/me")
async def me(user: User = Depends(current_user)):
    return user


