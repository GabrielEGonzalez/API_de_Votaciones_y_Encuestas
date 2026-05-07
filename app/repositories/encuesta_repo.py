from ..model.Encuestas import Encuestas
from ..model.Opciones import Opciones
from ..model.Votos import Votos
from sqlalchemy.orm import Session
from sqlalchemy import select, update , func
from sqlalchemy.exc import SQLAlchemyError

class EncuestaRepository():

    def __init__(self,db:Session):
        self.db = db

    def crear_encuesta(self,encuesta:Encuestas):
        self.db.add(encuesta)
        self.db.commit()
        self.db.refresh(encuesta)
        return encuesta

    def crear_opciones(self,opciones:Opciones) -> Opciones:
        try:
              self.db.add(opciones)
              self.db.commit()
              self.db.refresh(opciones)
              return opciones
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

    def actualizar_estado(self, encuesta_id: int):
        estado_actual = self.obtener_estado_encuesta(encuesta_id)

        if estado_actual is None:
            return None

        nuevo_estado = 0 if estado_actual == 1 else 1

        self.db.execute(
            update(Encuestas)
            .where(Encuestas.id == encuesta_id)
            .values(activo=nuevo_estado)
        )

        self.db.commit()

        return nuevo_estado


    def obtener_estado_encuesta(self, encuesta_id: int):

        estado_encuesta = self.db.execute(
            select(Encuestas.activo)
            .where(Encuestas.id == encuesta_id)
        ).scalar()

        return estado_encuesta 

    def obtener_encuestas_sin_votos(self):
        stmt = (
                select(Encuestas)
                .outerjoin(Votos) # Esto hace el LEFT JOIN
                .where(Votos.id.is_(None)) # Filtra: solo los que NO tienen relación en la tabla Voto
                )

        results = self.db.execute(stmt).scalars().all()
        return results

    def obtener_opciones_por_encuesta(self):
        opciones = self.db.execute(select(Opciones).where(Opciones.encuesta_id == Encuestas.id)).scalars().all()

        return opciones


    def contar_votos_por_opcion(self):
        result = self.db.execute(
                select(Opciones.texto,func.count(Votos.id)
                       .label("total_votos"))
                .outerjoin(Votos,Opciones.id == Votos.opcion_id)
                .group_by(Opciones.id)).all()
        return result

    def obtener_encuestas_top(self, limite=5):
        sql = (
        select(
            Encuestas.titulo, 
            func.count(Votos.id).label("total_votos")
        )
        # 1. Unimos las tablas (Encuesta -> Opciones -> Votos)
        .join(Opciones, Encuestas.id == Opciones.encuesta_id)
        .join(Votos, Opciones.id == Votos.opcion_id)
        # 2. Agrupamos por la encuesta
        .group_by(Encuestas.id)
        # 3. Ordenamos de mayor a menor según el conteo
        .order_by(func.count(Votos.id).desc())
        # 4. Limitamos el resultado (el "Top X")
        .limit(limite)
        )
    
        return self.db.execute(sql).all()
