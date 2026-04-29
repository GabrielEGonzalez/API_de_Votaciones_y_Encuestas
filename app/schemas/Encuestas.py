from pydantic import BaseModel,Field 
from datetime import date
from ..schemas.Opciones import Opcion , OpcionOut

class createEncuesta(BaseModel):
    titulo: str = Field(title="titulo de encuesta")
    descripcion: str = Field(title="descripcion de encuesta",description="descripcion de encuesta para creacion")
    opciones: list[Opcion] = Field(description="lista de opciones de encuesta")
    creador_id: int = Field(title="id del usuario",gt=0)

class outEncuesta(BaseModel):
    id: int
    titulo: str
    descripcion: str
    opciones: list[OpcionOut]
    creador_id: int
    fecha_creacion: date = Field(
        title="fecha de encuesta",
        description="fecha de creacion de encuesta"
    )
    activa: bool = Field(
        title="estado de encuesta"
    )
