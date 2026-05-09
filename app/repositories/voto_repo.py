""" 
voto_repo

Acceso a datos:

crear_voto
buscar_voto_por_usuario_y_encuesta
contar_votos_por_encuesta
verificar_opcion_existe
obtener_encuesta_id_por_opcion
"""

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from ..model.Votos import Votos
from sqlalchemy.orm import Session
from ..model.Opciones import Opciones

class VotoRepository():

    def __init__(self,db:Session):
        self.db = db

    def crear_voto(self,votos:Votos):
        try:
            self.db.add(votos)
            self.db.commit()
            self.db.refresh(votos)

            return votos
        except SQLAlchemyError as e:
            raise(e)

    def buscar_voto_por_usuario_y_encuesta(self):
        pass

    def contar_votos_por_encuesta(self):
        pass

    def verificar_opcion_existe(self,id:int):

        try:
            opcion = self.db.execute(select(Opciones).where(Opciones.id == id)).scalars().first()         
            return opcion
        except SQLAlchemyError as e:
            raise(e)

    def obtener_encuesta_id_por_opcion(self):
        pass

