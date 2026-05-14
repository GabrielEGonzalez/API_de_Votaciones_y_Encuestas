""" 
voto_repo

Acceso a datos:

crear_voto
buscar_voto_por_usuario_y_encuesta
contar_votos_por_encuesta
verificar_opcion_existe
obtener_encuesta_id_por_opcion
"""

from operator import and_
from sqlalchemy import func, select
from sqlalchemy.exc import SQLAlchemyError

from app.model.Encuestas import Encuestas
from ..model.Votos import Votos
from sqlalchemy.orm import Session
from ..model.Opciones import Opciones

class VotoRepository():

    def __init__(self,db:Session):
        self.db = db

    def crear_voto(self,id_usuario:int,opcion_id:int):
        try:
            votos = Votos(usuario_id=id_usuario,opcion_id=opcion_id)
            self.db.add(votos)
            self.db.commit()
            self.db.refresh(votos)

            return votos
        except SQLAlchemyError as e:
            raise(e)

    def buscar_voto_por_usuario_y_encuesta(self,id_usuario:int,id_encuesta:int):

        try:
            verificacion_usuario_encuesta = self.db.execute(
                    select(Votos)
                    .outerjoin(Opciones, Opciones.id == Votos.opcion_id)
                    .where(and_(Votos.id_usuario == id_usuario ,Opciones.id_encuesta == id_encuesta))
                    ).scalars().first()
            return verificacion_usuario_encuesta
        except SQLAlchemyError as e:
            raise(e)


    def contar_votos_por_encuesta(self,id_encuesta:int):
        try:

            conteo = self.db.execute(
                    select(Opciones.texto,func.count(Votos.opcion_id).label("total_votos"))
                    .outerjoin(Votos,Opciones.id == Votos.opcion_id)
                    .where(Opciones.encuesta_id == id_encuesta)
                    .group_by(Opciones.id,Opciones.texto)
                    ).all()

            return conteo

        except SQLAlchemyError as e:
            raise(e)

    def verificar_opcion_existe(self,id:int):

        try:
            opcion = self.db.execute(select(Opciones).where(Opciones.id == id)).scalars().first()         
            return opcion
        except SQLAlchemyError as e:
            raise(e)

    def obtener_encuesta_id_por_opcion(self,opcion_id:int):
        try:
            encuesta = self.db.execute(
                    select(Encuestas)
                    .join(Opciones , Opciones.encuesta_id == Encuestas.id  )
                    .where(Opciones.id == opcion_id)
                    ).scalars().first()

            return encuesta
        except SQLAlchemyError as e:
            raise(e)

