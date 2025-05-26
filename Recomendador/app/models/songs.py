from bson import ObjectId
import re

class songModel:
    def __init__(self, db):
        self.db = db

    async def obtener_canciones_populares(self):
        try:
            songs = await self.db.Songs.find().sort("Popularity", -1).limit(10).to_list(length=10)
            for song in songs:
                song["_id"] = str(song["_id"])
            return songs
        except Exception as e:
            print(f"Error al obtener canciones populares: {e}")
            return {"error": str(e)}

    async def getALL(self):
        try:
            songs = await self.db.Songs.find().to_list(length=1000)
            for song in songs:
                song["_id"] = str(song["_id"])
            return songs
        except Exception as e:
            print(f"Error al obtener todas las canciones: {e}")
            return {"error": str(e)}

    async def getById(self, id):
        try:
            song = await self.db.Songs.find_one({"_id": id})
            song["_id"] = str(song["_id"])
            return song
        except Exception as e:
            print(f"Error al obtener canción por ID: {e}")
            return {"error": str(e)}

    async def getByName(self, name):
        try:
            if isinstance(name, list):  
                regex_filters = [{"name": {"$regex": re.escape(kw), "$options": "i"}} for kw in name]
                regex_filters += [{"artist": {"$regex": re.escape(kw), "$options": "i"}} for kw in name]

                query = {"$or": regex_filters}
                result = await self.db.Songs.find(query).to_list(length=None)
                for song in result:
                    song["_id"] = str(song["_id"])
                return result if result else None
            elif isinstance(name, str):  
                song = await self.db.Songs.find_one({"name": name})
                if song:
                    song["_id"] = str(song["_id"])
                    return song
                else:
                    return None
            else:
                return {"error": "Tipo de dato no válido"}
    
        except Exception as e:
            print(f"Error al obtener canción(es) por nombre: {e}")
            return {"error": str(e)}
        
    async def getByArtist(self, artist):
        try:
            songs = await self.db.Songs.find({"artist": artist}).to_list(length=None)
            for song in songs:
                song["_id"] = str(song["_id"])
            return songs
        except Exception as e:
            print(f"Error al obtener canciones por artista: {e}")
            return {"error": str(e)}
        
    async def getByNames(self,userSongs):
        try:
            songs = await self.db.Songs.find({"name": {"$in": userSongs}}).to_list(length=None)
            for song in songs:
                song["_id"] = str(song["_id"])
            return songs
        except Exception as e:
            print(f"Error al obtener canciones por nombre: {e}")
            return {"error": str(e)}
        
    async def getByArtistNames(self,artist):
        try:
            songs = await self.db.Songs.find({"artist": artist}).to_list(length=None)
            for song in songs:
                song["_id"] = str(song["_id"])
            if not songs:
                return {"error": "No se encontraron canciones de este artista"}
            return songs
        except Exception as e:
            print(f"Error al obtener canciones por artista: {e}")
            return {"error": str(e)}
    
    async def getByGenre(self, genre):
        try:
            songs = await self.db.Songs.aggregate([{"$match": {"genre": genre}},{"$sample": {"size": 5}}]).to_list(length=5)
            for song in songs:
                song["_id"] = str(song["_id"])
            if not songs:
                return {"error": "No se encontraron canciones de este género"}
            return songs
        except Exception as e:
            print(f"Error al obtener canciones por género: {e}")
            return {"error": str(e)}
    
    async def getByEmotion(self, emotion):
        try:
            songs = await self.db.Songs.aggregate([{"$match": {"emotion": emotion}},{"$sample": {"size": 5}}]).to_list(length=5)
            for song in songs:
                song["_id"] = str(song["_id"])
            if not songs:
                return {"error": "No se encontraron canciones de esta emoción"}
            return songs
        except Exception as e:
            print(f"Error al obtener canciones por emoción: {e}")
            return {"error": str(e)}
        
    