""" 
voto_repo

Acceso a datos:

crear_voto
buscar_voto_por_usuario_y_encuesta
contar_votos_por_encuesta
verificar_opcion_existe
obtener_encuesta_id_por_opcion
"""

from ..model.Votos import Votos
from sqlalchemy.orm import Session
from sqlalchemy import select 

class VotoRepository():

    def __init__(self,db:Session):
        self.db = db

    def crear_voto(self):
        pass

    def buscar_voto_por_usuario_y_encuesta(self):
        pass

    def contar_votos_por_encuesta(self):
        pass

    def verificar_opcion_existe(self):
        pass

    def obtener_encuesta_id_por_opcion(self):
        pass

