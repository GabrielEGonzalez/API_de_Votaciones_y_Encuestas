from pydantic import BaseModel , Field


class UserBase(BaseModel):
    nombre: str = Field(title="nombre de usuario")
    correo: str = None

class CreaterUser(UserBase):
    password: str

class OutUser(UserBase):
    id: int