from fastapi import APIRouter, Depends, Request
from app.controllers.recomendations import SongsController
from data.database import get_db
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

def crearRouter(templates:Jinja2Templates):
    router = APIRouter()

    @router.get("/", response_class=HTMLResponse)
    async def home(request: Request):
        from app.models.songs import songModel
        SM = songModel(get_db())
        songs = await SM.obtener_canciones_populares()
        return templates.TemplateResponse("login.html",{
            "request": request,
            "songs": songs
        })

    @router.get("/songs/popular", tags=["Songs"])
    async def get_popular_songs(db=Depends(get_db)):
        controller = SongsController(db)
        return await controller.get_popular_songs()

    @router.get("/songs", tags=["Songs"])
    async def get_all_songs(db=Depends(get_db)):
        controller = SongsController(db)
        return await controller.get_all_songs()

    @router.get("/songs/{song_id}", tags=["Songs"])
    async def get_song_by_id(song_id: str, db=Depends(get_db)):
        controller = SongsController(db)
        return await controller.get_song_by_id(song_id)

    @router.get("/songs/name/{name}", tags=["Songs"])
    async def get_song_by_name(name: str, db=Depends(get_db)):
        controller = SongsController(db)
        return await controller.get_song_by_name(name)

    @router.get("/songs/artist/{artist}", tags=["Songs"])
    async def get_songs_by_artist(artist: str, db=Depends(get_db)):
        controller = SongsController(db)
        return await controller.get_songs_by_artist(artist)
    
    return router