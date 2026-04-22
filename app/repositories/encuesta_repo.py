from ..model.Encuestas import Encuestas
from ..model.Opciones import Opciones
from sqlalchemy.orm import Session
from sqlalchemy import select

class Encuesta():

    def __init__(self,db:Session):
        self.db = db

    def crear_encuesta(self,encuesta:Encuestas):
        self.db.add(encuesta)
        self.db.commit()
        self.db.refresh(encuesta)
        return encuesta

    def crear_opciones(self):
        pass

    def get_all_encuesta(self):
        pass

    def get_encuesta_id(self):
        pass

    def eliminar_encuesta(self):
        pass

    def actualizar_estado(self):
        pass

    def obtener_encuestas_sin_votos(self):
        pass

    def obtener_opciones_por_encuesta(self):
        pass

    def contar_votos_por_opcion(self):
        pass

    def obtener_top_encuestas(self):
        pass
