from configuracion_database import get_bd
from sqlalchemy.orm import Session
from fastapi import Depends
from app.repositories.usuario_repo import userRepositorio
from app.services.usuario_service import usuarioService
from app.services.encuesta_service import EncuestaService
from app.repositories.encuesta_repo import EncuestaRepository

def get_conexion(bd:Session=Depends(get_bd))-> usuarioService:
    repo = userRepositorio(bd)
    return usuarioService(repo)

def get_conexion_encuesta(db:Session=Depends(get_bd))-> EncuestaService:
    repo = EncuestaRepository(db)
    return EncuestaService(repo)
