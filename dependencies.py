from app.repositories.voto_repo import VotoRepository
from app.services.voto_service import VotoService
from configuracion_database import get_bd
from sqlalchemy.orm import Session
from fastapi import Depends
from app.repositories.usuario_repo import userRepositorio
from app.services.usuario_service import usuarioService
from app.services.encuesta_service import EncuestaService
from app.repositories.encuesta_repo import EncuestaRepository
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session


def get_conexion(bd:Session=Depends(get_bd))-> usuarioService:
    repo = userRepositorio(bd)
    return usuarioService(repo)

def get_conexion_encuesta(db:Session=Depends(get_bd))-> EncuestaService:
    repo = EncuestaRepository(db)
    return EncuestaService(repo)

def get_conexion_votos(db:Session=Depends(get_bd))-> VotoService:
    repo = VotoRepository(db)
    return VotoService(repo)


# 1. Define de dónde sacará el token (en la ruta /login)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


SECRET_KEY = "tu_clave_secreta_super_segura"
ALGORITHM = "HS256"

def get_current_user(
    token: str = Depends(oauth2_scheme), 
    db: Session = Depends(get_bd)
):
    """
    Esta es la dependencia que usarás en tus rutas.
    Extrae el ID del usuario del token y lo busca en la DB.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # 2. Decodificar el token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # 3. Extraer el 'sub' (donde guardaste el ID del usuario)
        user_id: str = payload.get("sub")
        
        if user_id is None:
            raise credentials_exception
            
    except JWTError:
        raise credentials_exception

    # 4. Buscar al usuario en la base de datos
    # Aquí usas tu repositorio o lógica de consulta
    repo = userRepositorio(db)
    user = repo.getUserById(int(user_id))
    
    
    if user is None:
        raise credentials_exception
        
    # 5. Retornar el objeto usuario completo
    return user
