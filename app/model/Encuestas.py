from configuracion_database import Base
from sqlalchemy import Boolean, Column, String , Integer , ForeignKey
from sqlalchemy.orm import relationship

class Encuestas(Base):
    __tablename__ = "encuestas"
    
    id = Column(Integer,autoincrement=True,primary_key=True)
    titulo = Column(String)
    descripcion = Column(String)
    creador_id = Column(Integer,ForeignKey("usuarios.id"))
    activo = Column(Boolean)
    
    usuario = relationship("Usuarios",back_populates="encuestas")
    opciones = relationship("Opciones",back_populates="encuesta")
