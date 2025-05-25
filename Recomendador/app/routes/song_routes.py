from fastapi import APIRouter, Depends, Request,HTTPException
from app.controllers.recomendations import SongsController
from app.controllers.users import UsersController
from data.database import get_db
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from collections import Counter

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
    
    @router.get("/songs",response_class=HTMLResponse)
    async def principal(request: Request,db=Depends(get_db)):
        username = request.cookies.get("username")
        if not username:
            raise HTTPException(status_code=401, detail="No estás autenticado")
        
        SongController = SongsController(db)
        UserController = UsersController(db)
        featuredSongs = await SongController.get_popular_songs()
        user = await UserController.getUserByName(username)
        userSongs = user.get("LastListened", [])
        newAccount = False

        if userSongs != []:
            songs = await SongController.get_songs_by_names(userSongs)
        else:
            songs = featuredSongs
            newAccount = True

        artistNames = [song["artist"] for song in songs]
        genresNames = [song["genre"] for song in songs]
        print(songs)
        emotionNames = [song["emotion"] for song in songs]
        contadorArtista = Counter(artistNames)
        contadorGeneros = Counter(genresNames)
        contadorEmociones = Counter(emotionNames)
        artistaMasRepetido = contadorArtista.most_common(1)[0][0]
        generoMasRepetido = contadorGeneros.most_common(1)[0][0]
        emocionMasRepetida = contadorEmociones.most_common(1)[0][0]
        artistaSongs = await SongController.get_songs_by_artist(artistaMasRepetido)
        genresSongs = await SongController.get_songs_by_genre(generoMasRepetido)
        emotionSongs = await SongController.get_songs_by_emotion(emocionMasRepetida)    

        return templates.TemplateResponse("app.html",{
            "request": request,
            "songs": songs,
            "artists":featuredSongs,
            "MRArtist": artistaMasRepetido,
            "artistSongs": artistaSongs,
            "user": username,
            "MRGenre": generoMasRepetido,
            "genreSongs": genresSongs,
            "MREmotion": emocionMasRepetida,
            "emotionSongs": emotionSongs,
            "new": newAccount
        })

    @router.get("/songs1", tags=["Songs"])
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