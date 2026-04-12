from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from app.routers.Usuarios import userRouter
from configuracion_database import Base , engine

app = FastAPI(
    title="API de encuesta y votaciones",
    version="1.0.0",
    description="Esta es una API de votaciones y encuestas en vivo. Será usada para manejar datos de los usuarios y es una API RESTful."
)

Base.metadata.create_all(bind=engine)

@app.get("/root", response_class=HTMLResponse)
async def root():
    return '<p>API DE ENCUESTA Y VOTACIONES</p>'

app.include_router(userRouter)