from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from app.routes.song_routes import crearRouter

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.include_router(crearRouter(templates))
