from app import create_app
from app.models.songs import obtener_canciones_populares

app = create_app()

if __name__ == "__main__":
    canciones = obtener_canciones_populares(db = app.mongo_db)
    print("Canciones populares:")
    for cancion in canciones:
        print(f"{cancion['song']} - {cancion['Popularity']}")