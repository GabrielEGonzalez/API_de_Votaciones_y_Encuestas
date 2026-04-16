from sqlalchemy.orm import Session
from sqlalchemy import select
from ..model.Usuario import Usuarios

class userRepositorio():
    def __init__(self,db:Session):
        self.db = db
    
    def createUser(self,user=Usuarios):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def getUserByID(self,password:str,correo:str): #metodo no funcionando logica incloclusa
        user_id = self.db.query(select(Usuarios).where(Usuarios.correo == correo))