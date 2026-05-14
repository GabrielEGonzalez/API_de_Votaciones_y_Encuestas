"""
Aquí está la lógica crítica del sistema:

registrar_voto
validar_usuario_existe
validar_opcion_existe
verificar_usuario_ya_voto
obtener_encuesta_por_opcion

👉 ⚠️ Esta parte es CLAVE:

evitar votos duplicados
validar integridad
"""

from ..repositories.voto_repo import VotoRepository

class VotoService:
    def __init__(self, voto_repository:VotoRepository, encuesta_repository, usuario_repository):
        self.voto_repo = voto_repository
        self.encuesta_repo = encuesta_repository
        self.usuario_repo = usuario_repository

    def registrar_voto(self, usuario_id: int, opcion_id: int):
        """
        Orquestador principal que coordina las validaciones 
        y la creación final del voto.
        """

        return self.voto_repo.crear_voto(usuario_id,opcion_id)

    def validar_usuario_existe(self, usuario_id: int):
        """
        Verifica en el repositorio de usuarios si el ID es válido.
        """
        pass

    def validar_opcion_existe(self, opcion_id: int):
        """
        Verifica en el repositorio de encuestas si la opción existe.
        """
        opcion_existe = self.voto_repo.verificar_opcion_existe(opcion_id)
        return opcion_existe

    def verificar_usuario_ya_voto(self, usuario_id: int, encuesta_id: int):
        """
        Consulta si existe un registro previo para evitar duplicidad.
        """
        pass

    def obtener_encuesta_por_opcion(self, opcion_id: int):
        """
        Recupera la entidad Encuesta vinculada a la opción seleccionada.
        """
        encuesta = self.voto_repo.obtener_encuesta_id_por_opcion(opcion_id)
        return encuesta
