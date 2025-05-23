from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.routes.song_routes import crearRouter
from app.routes.user_routes import userRouter

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(crearRouter(templates))
app.include_router(userRouter())
