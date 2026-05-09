from pydantic import BaseModel , Field

class Votos(BaseModel):
    usuario_id: int = Field(description="el id de el usuario que envia su voto") 
    opcion_id: int = Field(description="el id de la opcion de la respuesta")
