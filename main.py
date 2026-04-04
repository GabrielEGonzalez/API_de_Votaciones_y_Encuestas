from fastapi import FastAPI , responses , Request

app = FastAPI(title="api de encuesta y votaciones",version="0.0.1",routes=["/v1/votaciones","/v1/encuesta"],description="esta es una de votaciones y encuesta en vivo sera usada para majenar datos de los usuario y es una api restfull")

@app.get("/root")
async def root():
    return responses.HTMLResponse('<p>API DE ENCUESTA Y VOTACIONES</p>')