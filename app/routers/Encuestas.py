from fastapi import APIRouter, Depends, Path
from typing import Annotated
from dependencies import get_conexion_encuesta
from ..services.encuesta_service import EncuestaService
from ..schemas.Encuestas import createEncuesta , outEncuesta

encuesta_router = APIRouter(prefix="/v1")

@encuesta_router.post('/encuestas',response_model=outEncuesta)
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

@encuesta_router.get('/encuestas/top')
async def obtener_encuesta_top(service:EncuestaService=Depends(get_conexion_encuesta)):
    return service.obtener_top_encuestas()

@encuesta_router.get('/encuestas/sin-votos')
async def obtener_encuesta_sin_votos(service:EncuestaService=Depends(get_conexion_encuesta)):   return service.obtener_encuestas_sin_votos()

@encuesta_router.patch('/encuestas/{id}/estado')
async def estado_encuesta(id:Annotated[int,Path(gt=0)],service:EncuestaService=Depends(get_conexion_encuesta)):
    return service.cambiar_estado_encuesta()

@encuesta_router.delete('/encuestas/{id}')
async def eliminar_encuesta(id:Annotated[int,Path(gt=0)],service:EncuestaService=Depends(get_conexion_encuesta)):
    return service.eliminar_encuesta(id)

@encuesta_router.get('/encuestas/resultados')
async def obtener_resultados(service:EncuestaService=Depends(get_conexion_encuesta)):
    return service.obtener_resultados()
