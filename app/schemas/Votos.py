from pydantic import BaseModel , Field

class Votos():
    usuario_id: int | None = None
    opcion_id: int