from fastapi import APIRouter, Path
from typing import Annotated

""""
POST /encuestas
GET /encuestas
GET /encuestas/{id}
GET /encuestas/{id}/resultados
GET /encuestas/top
GET /encuestas/sin-votos
PATCH /encuestas/{id}/estado
DELETE /encuestas/{id}
"""

encuesta_router = APIRouter(prefix="/v1")

@encuesta_router.post('/encuestas')
async def crear_encuesta():
    pass

@encuesta_router.get('/encuestas')
async def obtener_encuesta():
    pass

@encuesta_router.get('/encuestas/{id}')
async def obtener_encuesta_id(id:Annotated[int,Path()]):
    pass