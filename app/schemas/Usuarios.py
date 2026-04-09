from pydantic import BaseModel , Field

class CreaterUser(BaseModel):
    nombre: str = Field(title="nombre de usuario")
    correo: str = None
    password: str