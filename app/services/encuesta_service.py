from ..repositories.encuesta_repo import EncuestaRepository
from ..schemas.Encuestas import createEncuesta
from ..model.Opciones import Opciones
from ..model.Encuestas import Encuestas
from fastapi.exceptions import HTTPException

class EncuestaService():

    def __init__(self,encuestaRepo:EncuestaRepository) -> None:
        self.encuesta_repo = encuestaRepo

    def crear_encuesta_con_opciones(self,encuesta:createEncuesta,token:str):

        encuesta_db = Encuestas(titulo=encuesta.titulo,descripcion=encuesta.descripcion,creador_id=token)
        encuesta_res_db = self.encuesta_repo.crear_encuesta(encuesta_db)

        #creacion de opciones de encuesta por id_encuesta , id_opcion , texto o descripcion
        if not encuesta_res_db:
            raise(HTTPException(status_code=301))
        
        lista_op = list()

        for opcion in encuesta.opciones:
            nueva_opcion = Opciones(encuesta_id=encuesta_res_db.id,texto=opcion.text)
            opciones = self.encuesta_repo.crear_opciones(nueva_opcion)
            lista_op.append(opciones)

    def listar_encuestas(self):
        return self.encuesta_repo.get_all_encuesta()

    def obtener_encuesta_por_id(self,id_encuesta:int):

        if not id_encuesta:
            raise(HTTPException(status_code=200))

        encuesta_encontrada = self.encuesta_repo.get_encuesta_id(id_encuesta)
        return encuesta_encontrada

    def obtener_resultados(self):
        opciones = self.encuesta_repo.obtener_opciones_por_encuesta()
        votos_opciones = self.encuesta_repo.contar_votos_por_opcion()

        return {
                "resultados":[
                    {"opciones":opciones},
                    {"votos_opciones":votos_opciones}
                    ]
                }

    def obtener_top_encuestas(self):
        top_encuesta = self.encuesta_repo.obtener_encuestas_top(10)
        return top_encuesta

    def obtener_encuestas_sin_votos(self):
        return self.encuesta_repo.obtener_encuestas_sin_votos()

    def cambiar_estado_encuesta(self,id:int):
        return self.encuesta_repo.actualizar_estado(id)

    def eliminar_encuesta(self,id_encuesta:int):
        encuesta_eliminada = self.encuesta_repo.eliminar_encuesta(id_encuesta)
        return encuesta_eliminada
