from pydantic import BaseModel , Field

class Opcion(BaseModel):
    text: str = Field(title="opcion de encuesta",description="opcion de la encuesta")

class OpcionOut(Opcion):
    id: int 