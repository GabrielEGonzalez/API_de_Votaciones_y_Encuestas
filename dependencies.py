from configuracion_database import get_bd
from sqlalchemy.orm import Session
from fastapi import Depends
from app.repositories.usuario_repo import userRepositorio
from app.services.usuario_service import usuarioService


def get_conexion(bd:Session=Depends(get_bd))-> usuarioService:
    repo = userRepositorio(bd)
    return usuarioService(repo)