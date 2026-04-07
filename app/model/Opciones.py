from configuracion_database import Base
from sqlalchemy import Column, String , Integer ,  DateTime , ForeignKey
from sqlalchemy.orm import relationship

class Opciones(Base):
    
    __tablename__ = "opciones"
    
    id = Column(Integer,autoincrement=True,primary_key=True)
    encuesta_id = Column(Integer,ForeignKey("encuestas.id"))
    texto = Column(String)
    
    encuesta = relationship("Encuestas",back_populates="opciones")
    votos = relationship("Votos",back_populates="opcion")