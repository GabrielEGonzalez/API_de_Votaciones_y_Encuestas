from fastapi import APIRouter, Depends, Path
from typing import Annotated
from dependencies import get_conexion_encuesta
from ..services.encuesta_service import EncuestaService
from ..schemas.Encuestas import createEncuesta
from fastapi.security import OAuth2PasswordBearer

from app.services import encuesta_service

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
async def crear_encuesta(encuesta:createEncuesta,service:EncuestaService=Depends(get_conexion_encuesta)):
    token = ""
    encuesta_creacion = service.crear_encuesta_con_opciones(encuesta,token)
    return encuesta_creacion

@encuesta_router.get('/encuestas')
async def obtener_encuesta(service:EncuestaService=Depends(get_conexion_encuesta)):
    return service.listar_encuestas()

@encuesta_router.get('/encuestas/{id}')
async def obtener_encuesta_id(id:Annotated[int,Path()],service:EncuestaService=Depends(get_conexion_encuesta)):
    return service.obtener_encuesta_por_id(id)

@encuesta_router.get('/encuesta/top')
async def ontener_encuesta_top(service:EncuestaService=Depends(get_conexion_encuesta)):
    return service.obtener_top_encuestas()
