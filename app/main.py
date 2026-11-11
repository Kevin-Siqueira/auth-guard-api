from fastapi import FastAPI
from app.core.config import settings
from app.core.database import Base, engine
from app.api.v1.router import api_router

# Cria as tabelas na base de dados (em ambiente de desenvolvimento/produção inicial)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"message": "AuthGuard API está online!", "docs": "/docs"}