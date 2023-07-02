'''

API

'''

from fastapi import APIRouter

router = APIRouter()

@router.get("/skill")
def get_skill():
    return "Obteniendo información de la habilidad"

@router.get("/skill/{skill_id}")
def get_skill_by_id(skill_id: int):
    return f"Obteniendo información de la habilidad {skill_id}"
