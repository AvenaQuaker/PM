from bson import ObjectId

class userModel:
    def __init__(self, db):
        self.db = db

    async def login(self, username, password):
        try:
            user = await self.db.Users.find_one({"username": username, "password": password})
            if user:
                user["_id"] = str(user["_id"])
                print(f"Usuario encontrado: {user}")
                return user
            else:
                return None
        except Exception as e:
            print(f"Error al iniciar sesión: {e}")
            return {"error": str(e)}
        
    async def register(self, username, password):
        try:
            user = await self.db.Users.find_one({"username": username})
            if user:
                return {"error": "El nombre de usuario ya existe"}
            else:
                new_user = {
                    "username": username,
                    "password": password,
                    "LastListened": [],
                }
                result = await self.db.Users.insert_one(new_user)
                new_user["_id"] = str(result.inserted_id)
                return new_user
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
            return {"error": str(e)}
    
    async def getUserByName(self, username):
        try:
            user = await self.db.Users.find_one({"username": username})
            if user:
                user["_id"] = str(user["_id"])
                return user
            else:
                return None
        except Exception as e:
            print(f"Error al obtener usuario: {e}")
            return {"error": str(e)}
        
    async def addSongToUser(self, username, song_name):
        try:
            user = await self.db.Users.find_one({"username": username})
            if not user:
                return {"error": "Usuario no encontrado"}
            if "LastListened" not in user:
                user["LastListened"] = []
            if song_name not in user["LastListened"]:
                if len(user["LastListened"]) >= 10:
                    user["LastListened"].pop(0)
                    
                user["LastListened"].append(song_name)
                await self.db.Users.update_one({"username": username}, {"$set": {"LastListened": user["LastListened"]}})
                return {"message": "Canción añadida correctamente"}
            else:
                return {"message": "La canción ya está en la lista de escuchadas"}
        except Exception as e:
            print(f"Error al añadir canción al usuario: {e}")
            return {"error": str(e)}
        

