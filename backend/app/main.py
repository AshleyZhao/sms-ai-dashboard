from fastapi import FastAPI
from app.api import generate

app = FastAPI()
app.include_router(generate.router, prefix="/api")