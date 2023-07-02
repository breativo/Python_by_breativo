'''

API

'''
'''
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return "Obteniendo lista de usuarios"


users_list=['breativo', 'brea', 'tivo']

@router.get("/users/{user_id}")
def get_user(user_id: int):
    return users_list[id]
'''

# Parametro prefix
from fastapi import APIRouter

router = APIRouter(prefix='/u')

users_list=['breativo', 'brea', 'tivo']

@router.get("/")
def get_users():
    return users_list

@router.get("/{id}")
def get_user(id: int):
    return users_list[id]

# Parametro tags
from fastapi import APIRouter

router = APIRouter(tags=['usuarios'])

@router.get("/users")
def get_users():
    return "Obteniendo lista de usuarios"