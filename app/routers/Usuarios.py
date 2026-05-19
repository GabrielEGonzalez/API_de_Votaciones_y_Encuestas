from fastapi import APIRouter , Depends
from app.schemas.Usuarios import CreaterUser
from dependencies import get_conexion
from app.services.usuario_service import usuarioService
from dependencies import oauth2_scheme, get_current_user

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

@userRouter.get("/user")
async def obtener_saludo(usuario:oauth2_scheme=Depends(get_current_user)):
    return {"massege":f"hol, bienvenido {usuario}"}
