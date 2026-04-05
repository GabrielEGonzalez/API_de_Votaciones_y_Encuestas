from sqlalchemy.orm import sessionmaker , declarative_base
from sqlalchemy import create_engine

#conexion a la base de datos 
engine = create_engine("ruta_base_de_dato",echo=True) 
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

#dependecia de base de datos
def get_bd():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()