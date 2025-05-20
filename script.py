import random
from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb+srv://Jaime:sonic123%40@clustermongo.ial5c.mongodb.net/")
db = client["Spotify"]
collection = db["Songs1"]

# Obtener todos los documentos
documents = collection.find()

# Para cada documento, asignar un género y un valor de popularidad aleatorio
for doc in documents:
    popularity = random.randint(0, 100)
    
    collection.update_one(
        {"_id": doc["_id"]},
        {"$set": {
            "popularity": popularity
        }}
    )

print("✅ Género y popularidad asignados aleatoriamente a cada canción.")
