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
    services_user.create_user(user)
    return user

@userRouter.post("/login")
async def login_user(user:CreaterUser, db:Session=Depends(get_bd)):
    """ login de usuario que se le devolvera un id o un token"""
    return 