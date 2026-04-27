from sqlalchemy.orm import Session
from sqlalchemy import select
from ..model.Usuario import Usuarios
from ..model.Encuestas import Encuestas
from app.model import Usuario

class userRepositorio():
    def __init__(self,db:Session):
        self.db = db
    
    def createUser(self,user:Usuarios):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def getUserByEmail(self,correo:str)-> Usuarios | None :
        usuario_correo = self.db.execute(select(Usuarios).where(Usuarios.correo == correo)).scalars().first()
        return usuario_correo
    
    def getUserById(self,id:int)-> Usuarios | None :
        user_id = self.db.execute(select(Usuarios).where(Usuarios.id == id)).scalars().first()
        return user_id
    
    
    def obtener_encuestas_por_usuario_id(self,id:int):
        result = self.db.execute(
                select(Usuarios.nombre,Encuestas.nombre,Encuestas.descripcion)
                .join(Encuestas, Usuarios.id == Encuestas.creador_id)
                .where(Usuarios.id == id)
                ).all()

        return result
