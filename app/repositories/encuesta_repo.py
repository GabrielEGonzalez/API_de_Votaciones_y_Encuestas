from typing import List
from ..model.Encuestas import Encuestas
from ..model.Opciones import Opciones
from sqlalchemy.orm import Session
from sqlalchemy import delete, select, update
from sqlalchemy.exc import SQLAlchemyError

class Encuesta():

    def __init__(self,db:Session):
        self.db = db

    def crear_encuesta(self,encuesta:Encuestas):
        self.db.add(encuesta)
        self.db.commit()
        self.db.refresh(encuesta)
        return encuesta

    def crear_opciones(self,opciones:List[Opciones]) -> List[Opciones]:
        try:
            lista_opciones = []
            for opcion in opciones:
              self.db.add(opcion)
              self.db.commit()
              self.db.refresh(opcion)
              lista_opciones.append(opciones)
            return lista_opciones
        except SQLAlchemyError as e:
            raise e

    def get_all_encuesta(self):
        try:
            lista_encuestas = self.db.execute(select(Encuestas)).scalars().first()
            return lista_encuestas
        except Exception as e:
            raise e

    def get_encuesta_id(self,encuesta_id: int):
        encuesta = self.db.execute(select(Encuestas).where(Encuestas.id == encuesta_id)).scalars().first()
        return encuesta

    def eliminar_encuesta(self,encuesta_id:int):
        encuesta = self.db.execute(select(Encuestas).where(Encuestas.id == encuesta_id)).first()
        self.db.delete(encuesta)
        self.db.commit()
        self.db.refresh(encuesta)

        return encuesta

    def actualizar_estado(self,encuesta_id:int):
        encuesta_encontrada = self.db.execute(select(Encuestas).where(Encuestas.id == encuesta_id)).scalars().first()
        pass

    def obtener_encuestas_sin_votos(self):
        pass

    def obtener_opciones_por_encuesta(self):
        pass

    def contar_votos_por_opcion(self):
        pass

    def obtener_top_encuestas(self):
        pass
