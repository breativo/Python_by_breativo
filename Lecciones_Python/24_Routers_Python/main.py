'''

API

'''

from fastapi import FastAPI
from router import users, skill


app = FastAPI()

# Routers
app.include_router(users.router)
app.include_router(skill.router)

@app.get("/") 
async def message(): 
    return "Hola mundo"
