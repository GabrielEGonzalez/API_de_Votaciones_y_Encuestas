from ..repositories.usuario_repo import userRepositorio
from app.schemas.Usuarios import CreaterUser

class usuarioService():
    def __init__(self,repo:userRepositorio):
        self.repo = repo
    
    def create_user(self,user:CreaterUser):
        return self.repo.createUser(user)