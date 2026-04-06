from configuracion_database import Base
from sqlalchemy import Column, String , Integer ,  DateTime , ForeignKey
from sqlalchemy.orm import relationship

class Votos(Base):
    __tablename__ = "votos"
    
    id = Column(Integer,autoincrement=True,primary_key=True)
    usuario_id = Column(Integer,ForeignKey("usuarios.id"))
    opcion_id = Column(Integer,ForeignKey("encuestas.id"))
    
    encuesta = relationship("Encuestas",back_populates="voto")
    usuario = relationship("Usuarios",back_populates="votos")