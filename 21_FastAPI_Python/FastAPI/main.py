'''

API main

'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/") # Lamada al servidor
async def message(): # Función asíncrona
    return "Hola mundo" 
# Salida navegador 127.0.0.1:8000
# Hola mundo

@app.get("/url") 
async def url(): 
    return ['url'':''https://breativo.com']
# Salida navegador 127.0.0.1:8000/url
# ["url:https://breativo.com"]

