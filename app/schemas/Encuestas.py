from pydantic import BaseModel,Field 
from pydantic.validate_call_decorator import validate_call
from datetime import date

class createEncuesta(BaseModel):
    titulo: str = Field(title="titulo de encuesta")
    descripcion: str = Field(title="descripcion de encuesta",description="descripcion de encuesta para creacion")
    creador_id: int = Field(title="id del usuario",gt=0)

class outEncuesta(createEncuesta):
    id:int
    fecha_creacion: date = Field(title="fecha de encuesta",description="fecha de creacion de encuesta")
    activa: bool = Field(title="estado de encuesta")
    
    
"""
id
titulo
descripcion
creador_id (FK usuario)
fecha_creacion
activa (boolean)
"""