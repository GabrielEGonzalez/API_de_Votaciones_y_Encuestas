from fastapi import APIRouter

voto_router = APIRouter(prefix="/v1")


@voto_router.post("/votar")
async def agregar_voto():
    pass

