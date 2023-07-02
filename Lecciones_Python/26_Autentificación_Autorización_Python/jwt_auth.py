'''

API

'''

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext

ALGORITHM = 'HS256'
SECRET_KEY = 'your-secret-key'
ACCESS_TOKEN_EXPIRE_MINUTES = 1

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

class User(BaseModel):
    id: str
    name: str
    disabled: bool
    hashed_password: str

user_db = {
    'breativo': {
        'id': '1',
        'name': 'breativo',
        'disabled': True,
        'hashed_password': '$2a$12$IUuCQ8dpTcT4aT2yOCwTleTFeMTLMXSfnFUFzCIcddJLDJwRx8N0i'  # password: 0000
    },
    'mario': {
        'id': '2',
        'name': 'mario',
        'disabled': True,
        'hashed_password': '$2a$12$BdQnG7gnnLslkgSx2nKsC.NqpCOpDbpz1MQBWpzcr/ldyYg8/4Dbu'  # password: 1234
    }
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Función para verificar la contraseña
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Función para generar un token JWT
def create_access_token(data: dict):
    to_encode = data.copy()
    access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return access_token

# Busqueda de usuario
def search_user(username: str):
    if username in user_db:
        user_data = user_db[username]
        return User(**user_data)

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

    if not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password incorrecto",
        )

    # Generar un token JWT
    token_data = {
        'sub': user.id,
        'name': user.name,
        'disabled': user.disabled
    }
    access_token = create_access_token(token_data)

    return {"access_token": access_token, "token_type": "bearer"}

# Ruta protegida que requiere autenticación con token JWT
@app.get("/user/me")
async def me(token: str = Depends(oauth2_scheme)):
    try:
        # Verificar y decodificar el token JWT
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = User(**payload)
        return user
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token JWT inválido o expirado",
        )
