from fastapi import FastAPI
from app.routes.song_routes import router as songs_router

app = FastAPI()

app.include_router(songs_router)
