from configuracion_database import Base
from sqlalchemy import Column, String , Integer ,  DateTime , ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Usuarios(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer,autoincrement=True,primary_key=True)
    nombre = Column(String)
    correo = Column(String)
    password = Column(String)
    fecha_creacion = Column(DateTime, server_default=func.now())
    
    encuestas = relationship("Encuestas",back_populates="usuario")
    votos = relationship("Votos",back_populates="usuario")