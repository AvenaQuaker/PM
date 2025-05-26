import random
from pymongo import MongoClient

# Lista de géneros populares
emotions = [
    "joy",
    "love",
    "anger",
    "fear",
    "surprise",
    "sadness"
]
# Conexión a MongoDB
client = MongoClient("mongodb+srv://Jaime:sonic123%40@clustermongo.ial5c.mongodb.net/")
db = client["Spotify"]
collection = db["Songs"]

# Buscar solo los documentos que no tienen el campo "genre"
documents = collection.find({"emotion": {"$exists": False}})

# Asignar género aleatorio a los documentos seleccionados
for doc in documents:
    random_emotion= random.choice(emotions)

    collection.update_one(
        {"_id": doc["_id"]},
        {"$set": {"emotion": random_emotion}}
    )

print("✅ Géneros aleatorios asignados a canciones sin emotion.")

