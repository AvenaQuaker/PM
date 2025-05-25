from fastapi import APIRouter, HTTPException
from app.models.songs import songModel
from app.models.users import userModel

class SongsController:
    def __init__(self, db):
        self.song_model = songModel(db)

    async def get_popular_songs(self):
        songs = await self.song_model.obtener_canciones_populares()
        if "error" in songs:
            raise HTTPException(status_code=500, detail=songs["error"])
        return songs

    async def get_all_songs(self):
        songs = await self.song_model.getALL()
        if "error" in songs:
            raise HTTPException(status_code=500, detail=songs["error"])
        return songs

    async def get_song_by_id(self, song_id):
        song = await self.song_model.getById(song_id)
        if not song:
            raise HTTPException(status_code=404, detail=song["error"])
        if "error" in song:
            raise HTTPException(status_code=500, detail=song["error"])
        return song

    async def get_song_by_name(self, name):
        song = await self.song_model.getByName(name)
        if not song:
            raise HTTPException(status_code=404, detail=song["error"])
        if "error" in song:
            raise HTTPException(status_code=500, detail=song["error"])
        return song

    async def get_songs_by_artist(self, artist):
        songs = await self.song_model.getByArtistNames(artist)
        if "error" in songs:
            raise HTTPException(status_code=500, detail=songs["error"])
        return songs
    
    async def get_songs_by_names(self, userSongs):
        songs = await self.song_model.getByNames(userSongs)
        if "error" in songs:
            raise HTTPException(status_code=500, detail=songs["error"])
        return songs
    
    async def get_songs_by_genre(self, genre):
        songs = await self.song_model.getByGenre(genre)
        if "error" in songs:
            raise HTTPException(status_code=500, detail=songs["error"])
        return songs
    
    async def get_songs_by_emotion(self, emotion):
        songs = await self.song_model.getByEmotion(emotion)
        if "error" in songs:
            raise HTTPException(status_code=500, detail=songs["error"])
        return songs