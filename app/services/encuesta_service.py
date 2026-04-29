"""
Lógica fuerte aquí:

crear_encuesta_con_opciones
listar_encuestas
obtener_encuesta_por_id
obtener_resultados
obtener_top_encuestas
obtener_encuestas_sin_votos
cambiar_estado_encuesta
eliminar_encuesta

👉 Validaciones:

usuario creador existe
encuesta activa/inactiva
manejar creación de opciones automáticamente
"""

from ..repositories.encuesta_repo import EncuestaRepository
from ..schemas.Encuestas import createEncuesta, outEncuesta 

class EncuestaService():

    def __init__(self,encuestaRepo:EncuestaRepository) -> None:
        self.encuesta_repo = encuestaRepo

    def crear_encuesta_con_opciones(self,encuesta:createEncuesta,token:str):
        pass

    def listar_encuestas(self):
        return self.encuesta_repo.get_all_encuesta()

    def obtener_encuesta_por_id(self):
        pass

    def obtener_resultados(self):
        pass

    def obtener_top_encuestas(self):
        pass

    def obtener_encuestas_sin_votos(self):
        pass

    def cambiar_estado_encuesta(self):
        pass

    def eliminar_encuesta(self):
        pass
