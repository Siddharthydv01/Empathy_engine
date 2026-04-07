from fastapi import FastAPI
from app.routes import tts_routes

app = FastAPI()

app.include_router(tts_routes.router)

@app.get("/")
def root():
    return {"message": "Empathy Engine is running 🚀"}