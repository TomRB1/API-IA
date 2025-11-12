# app/main.py
from fastapi import FastAPI
from routes.cliente import router as cliente_router
from routes.marca import router as marca_router
from routes.categoria import router as categoria_router
from routes.componente import router as componente_router
from routes.pedido import router as pedido_router

app = FastAPI(title="API ComponentesPC")

app.include_router(cliente_router)
app.include_router(marca_router)
app.include_router(categoria_router)
app.include_router(componente_router)
app.include_router(pedido_router)
