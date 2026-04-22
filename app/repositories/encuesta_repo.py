"""
crear_encuesta
crear_opciones
obtener_todas
obtener_por_id
obtener_opciones_por_encuesta
contar_votos_por_opcion (GROUP BY)
obtener_top_encuestas (COUNT + ORDER)
obtener_encuestas_sin_votos
actualizar_estado
eliminar_encuesta
"""

from ..model.Encuestas import Encuestas
from ..model.Opciones import Opciones
from sqlalchemy.orm import Session
from sqlalchemy import select

class Encuesta():

    def __init__(self,db:Session):
        self.db = db

    def crear_encuesta():
        pass

    def crear_opciones():
        pass

    def get_all_encuesta():
        pass

    def get_encuesta_id():
        pass

