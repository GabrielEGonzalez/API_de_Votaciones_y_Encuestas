from ..repositories.usuario_repo import userRepositorio
from app.schemas.Usuarios import CreaterUser
from app.model.Usuario import Usuarios
from passlib.hash import pbkdf2_sha256
import bcrypt

class usuarioService():
    def __init__(self,repo:userRepositorio):
        self.repo = repo
    
    def create_user(self,user:CreaterUser):
        passhash = pbkdf2_sha256.hash(user.password)
        modelo_user = Usuarios(nombre=user.nombre,correo=user.correo,password=passhash)
        return self.repo.createUser(modelo_user)
    
    def login_usuario(self):
        pass
    
    def obtener_usuario_id(sefl):
        pass
    
    def obtener_encuestas_usuario(self):
        pass