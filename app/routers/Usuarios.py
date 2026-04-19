from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from configuracion_database import get_bd
from app.schemas.Usuarios import CreaterUser
from dependencies import get_conexion
from app.services.usuario_service import usuarioService

userRouter = APIRouter(prefix="/v1")

@userRouter.post("/user")
async def creater_user(user:CreaterUser,services_user:usuarioService =Depends(get_conexion)):
    """ crear un nuevo usuario """
    token = services_user.create_user(user)
    return token

@userRouter.post("/login")
async def login_user(user:CreaterUser, services_user: usuarioService=Depends(get_conexion)):
    """ login de usuario que se le devolvera un id o un token"""
    token = services_user.login_usuario(user)
    return token 