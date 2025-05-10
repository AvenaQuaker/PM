from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient('mongodb+srv://Jaime:sonic123%40@clustermongo.ial5c.mongodb.net/')
db = client['Spotify']

def get_db():
    return db
