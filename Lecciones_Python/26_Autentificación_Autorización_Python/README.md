# Autentificación and autorización Python

![](https://github.com/breativo/Python_by_breativo/blob/master/img/Banner_Python_by_breativo.png?raw=true)

# Lección 26. Autentificación and autorización Python.

FastAPI proporciona varias herramientas para ayudarlo a manejar la seguridad de manera fácil, rápida y estándar, sin tener que estudiar y aprender todas las especificaciones de seguridad.

<h2 style="color:#15A7E1">Autentificación.</h2>
La autenticación en FastAPI se refiere al proceso de verificar y validar la identidad de los usuarios que interactúan con una aplicación web desarrollada con FastAPI. Permite proteger ciertas rutas o recursos de la aplicación para que solo los usuarios autorizados puedan acceder a ellos.

<br>

Todas las autentificaciones se realizan con estándares de seguridad. 

<h2 style="color:#15A7E1">Autorización.</h2>
La autorización en FastAPI se refiere al proceso de determinar qué usuarios autenticados tienen permiso para acceder a recursos específicos de una aplicación. Mientras que la autenticación se centra en verificar la identidad de un usuario, la autorización se encarga de definir los roles y los permisos asociados a esos roles para controlar el acceso a diferentes partes de la aplicación.

<h2 style="color:#15A7E1">OAuth2.</h2>
OAuth2 (Open Authorization 2.0) es un protocolo de autorización estándar utilizado para permitir que las aplicaciones obtengan acceso limitado a los recursos en nombre de un usuario sin compartir sus credenciales de inicio de sesión. Proporciona un flujo seguro y flexible para la autenticación y autorización en aplicaciones web y móviles.

<br>

Aquí hay una descripción general de los conceptos clave en OAuth2:

<br>

Actores principales:

* Propietario del recurso: Es el usuario final que posee los datos protegidos y decide compartir el acceso a estos recursos con una aplicación de terceros.
* Cliente: Es la aplicación de terceros que solicita acceso a los recursos en nombre del propietario del recurso.
* Servidor de autorización: Es el servidor que autentica al propietario del recurso y emite tokens de acceso al cliente después de la autenticación exitosa.
* Servidor de recursos: Es el servidor que aloja los recursos protegidos a los que el cliente desea acceder en nombre del propietario del recurso.
Flujo de autorización: OAuth2 define varios flujos de autorización para obtener tokens de acceso. Algunos flujos comunes son:

<br>

Authorization Code Grant: Este flujo se utiliza para aplicaciones web y se basa en la emisión de un código de autorización que luego se intercambia por un token de acceso.
* Implicit Grant: Este flujo se utiliza principalmente en aplicaciones de un solo página (SPA) o aplicaciones móviles, donde el token de acceso se envía directamente al cliente sin la necesidad de un intercambio de código de autorización.
* Client Credentials Grant: Este flujo se utiliza para autenticar aplicaciones en lugar de usuarios individuales. El cliente autentica directamente con el servidor de autorización y obtiene un token de acceso.

<br>

Tokens:
* Access Token: Es un token emitido por el servidor de autorización que permite al cliente acceder a los recursos protegidos en nombre del propietario del recurso. Este token es de corta duración y debe incluirse en cada solicitud al servidor de recursos.
* Refresh Token: Es un token opcional que se emite junto con el token de acceso. Puede utilizarse para obtener un nuevo token de acceso una vez que el token original ha expirado.

<br>

Ámbitos (Scopes): Los ámbitos definen los permisos específicos que el cliente solicita al acceder a los recursos protegidos. El servidor de autorización valida los ámbitos solicitados por el cliente y emite tokens de acceso con permisos limitados según estos ámbitos.

<br>

OAuth2 es ampliamente utilizado por proveedores de servicios como Google, Facebook, GitHub y muchos otros para permitir que las aplicaciones de terceros accedan a los datos y servicios de los usuarios de manera segura y controlada.

<br>
<br>

````py
# Entrada
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

# Base da datos usuarios
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

# Busca el usuario en la base de datos
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
````
````sh
# Salida
# Salida navegador 127.0.0.1:8000/login (POST)
username: 'breativo'
password:'0000'
{
  "access_token": "breativo",
  "token_type": "bearer"
}
````
Disponemos de una autentificación de type 'beare' y el token de acceso es 'breativo'.

A continuacion vamos a la operación autenticada.

<br>
<br>

````py
# Entrada
# Operación autorización
@app.get("/user/me")
async def me(user: User = Depends(current_user)):
    return user
````
````sh
# Salida
# Salida navegador 127.0.0.1:8000/user/me (GET) a la que pasamos el tokeb creado anteriormente 'breativo'
{
  "id": "1",
  "name": "breativo",
  "disabled": true,
  "password": "0000"
}
````
<h2 style="color:#15A7E1">JWT.</h2>
JWT significa "JSON Web Token" (Token de Web JSON) y es un estándar abierto (RFC 7519) que define un formato compacto y seguro para transmitir información entre partes como un objeto JSON. Un JWT consta de tres partes: encabezado (header), carga útil (payload) y firma (signature).

<br>

El encabezado contiene información sobre el tipo de token y el algoritmo de firma utilizado.
La carga útil es donde se puede incluir la información adicional que se quiere transmitir. Por ejemplo, datos de usuario, roles, permisos u otra información relevante.
La firma es utilizada para verificar la integridad del token y asegurar que no ha sido alterado durante su transmisión. La firma se crea utilizando una clave secreta conocida solo por el servidor emisor del token.

<br>

Los JWT son ampliamente utilizados para la autenticación y autorización en aplicaciones web y API. Cuando un usuario inicia sesión en una aplicación, se le proporciona un JWT que puede incluir información sobre su identidad y permisos. Este token se envía en cada solicitud posterior como una forma de autorización. El servidor puede verificar la firma del token y extraer la información necesaria para tomar decisiones de seguridad.

<br>

Los JWT son autónomos, lo que significa que contienen toda la información necesaria para ser validados sin necesidad de consultar una base de datos o realizar llamadas adicionales al servidor. Esto los hace eficientes y escalables.

<br>

Además, los JWT son utilizados en entornos distribuidos y permiten la implementación de autenticación sin estado (stateless authentication), lo que significa que el servidor no necesita mantener información sobre la sesión del usuario. Esto facilita la construcción de sistemas escalables y tolerantes a fallos.

Instalación del paquete jose de Python para generar y verificar los tokens JWT en Python:

<br>
<br>

````py
# Entrada
pip install "python-jose[cryptography]"
````

PassLib es un excelente paquete de Python para manejar hashes de contraseñas.

Admite muchos algoritmos de hash seguros y utilidades para trabajar con ellos.

El algoritmo recomendado es "Bcrypt".

Instalación de PassLib con Bcrypt:

<br>
<br>

````py
# Entrada
Instalación pip "passlib[bcrypt]"
````

Una vez disponemos de los paquetes instalados, ahora vamos a crear el codigo que nos permita autentificarnos con jwt.

<br>
<br>

````py
# Entrada
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

````
````py
# Entrada
# Generar un token JWT
    token_data = {
        'sub': user.id,
        'name': user.name,
        'disabled': user.disabled
    }
    access_token = create_access_token(token_data)

    return {"access_token": access_token, "token_type": "bearer"}
````
````sh
# Salida
# Salida navegador 127.0.0.1:8000/login (POST) con los datos de acceso breativo como username y password 0000
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwibmFtZSI6ImJyZWF0aXZvIiwiZGlzYWJsZWQiOnRydWV9.vUJwNqRv3MWhUQlaGWA_RYvtbzcPpTA2nZfS9qUsi1g",
  "token_type": "bearer"
}
````

Una vez disponemos del token de autentificación ya tendríamos acceso a los datos en la ruta indicada. Esta clave de autentificación dispone de un tiempo, una vez superado el tiempo indicado de expiración no será valido y tendríamos que crear un código nuevo de autentificación.

<br>
<br>

````py
# Entrada
# Entrada del token generado del usuario breativo
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwibmFtZSI6ImJyZWF0aXZvIiwiZGlzYWJsZWQiOnRydWV9.vUJwNqRv3MWhUQlaGWA_RYvtbzcPpTA2nZfS9qUsi1g
````
````sh
# Salida
# Salida navegador 127.0.0.1:8000/user/me con el token de autentificación expirada.
{
  "detail": "Token JWT inválido o expirado"
}
````
En este caso generamos un nuevo Token de acceso.

<br>
<br>

````sh
# Salida
# Salida de navegador 127.0.0.1:8000/user/me con el token de autentificación correcto.
{
    id': '1',
    name': 'breativo',
    disabled': True,
    hashed_password':    '$2a$12$IUuCQ8dpTcT4aT2yOCwTleTFeMTLMXSfnFUFzCIcddJLDJwRx8N0i' 
 }
````
<br>
<br>

🎉 Enhorabuena has superado la lección 🎉

<br>

[<< 25 REcursos estáticos](../25_Recursos_Estáticos_Python) | [ 27 MongoDB>>](../27_MongoDB_Python)

![https://github.com/breativo](https://raw.githubusercontent.com/breativo/breativo/master/img/img_breativo/Banner_negro.png)





