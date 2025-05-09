from flask import Flask
from pymongo import MongoClient

client = MongoClient('mongodb+srv://Jaime:sonic123%40@clustermongo.ial5c.mongodb.net/')
db = client['Spotify']

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb+srv://Jaime:sonic123%40@clustermongo.ial5c.mongodb.net/"

    app.mongo_db = db

    return app