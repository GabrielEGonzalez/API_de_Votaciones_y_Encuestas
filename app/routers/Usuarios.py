from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from configuracion_database import get_bd

userRouter = APIRouter(prefix="/v1")

@userRouter.post("/user")
async def creater_user(db:Session=Depends(get_bd())):
    """ crear un nuevo usuario """
    user = []
    return await user

@userRouter.post("/login")
async def login_user(db:Session=Depends(get_bd())):
    """ login de usuario que se le devolvera un id o un token"""
    return 