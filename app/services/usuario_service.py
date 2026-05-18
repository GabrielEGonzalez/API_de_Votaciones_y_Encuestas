from ..repositories.usuario_repo import userRepositorio
from fastapi import HTTPException
from app.schemas.Usuarios import CreaterUser
from app.model.Usuario import Usuarios
from passlib.hash import pbkdf2_sha256
from app.schemas.Usuarios import OutUser
from jose import jwt
from datetime import  datetime, timedelta, timezone

class usuarioService():
    def __init__(self,repo:userRepositorio):
        self.repo = repo
    
    def create_user(self,user:CreaterUser) -> str:
        passhash = pbkdf2_sha256.hash(user.password)
        modelo_user = Usuarios(nombre=user.nombre,correo=user.correo,password=passhash)
        bd_user = self.repo.createUser(modelo_user)
        return bd_user
    
    def login_usuario(self,user:CreaterUser)-> str:
        usuario = self.repo.getUserByEmail(user.correo)
        if not usuario:
            raise HTTPException(status_code=404,detail="usuario no encontrado")
        
        if not self.verify_password(user.password,usuario.password):
            raise HTTPException(status_code=401,detail="incorrect password")
        
        expire = datetime.now(timezone.utc) + timedelta(minutes=30)
        data = {
            "id":usuario.id,
            "nombre":usuario.nombre,
            "correo":usuario.correo,
            "exp": int(expire.timestamp())
        }
        token = jwt.encode(data,"secret",algorithm="HS256")
        return token
        
    
    def obtener_usuario_id(self,id:int) -> OutUser:
        usuario_id = self.repo.getUserById(id)
        return usuario_id
    
    def obtener_encuestas_usuario(self,id:int):
        encuesta_usuario = self.repo.obtener_encuestas_por_usuario_id(id)
        return encuesta_usuario
    
    def verify_password(self,plain,hashed):
        return pbkdf2_sha256.verify(plain,hashed)
