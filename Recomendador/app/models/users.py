from bson import ObjectId

class userModel:
    def __init__(self, db):
        self.db = db

    async def login(self, username, password):
        try:
            user = await self.db.Users.find_one({"username": username, "password": password})
            if user:
                user["_id"] = str(user["_id"])
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
                    "password": password
                }
                result = await self.db.Users.insert_one(new_user)
                new_user["_id"] = str(result.inserted_id)
                return new_user
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
            return {"error": str(e)}
    
    