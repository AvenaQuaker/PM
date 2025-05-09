def obtener_canciones_populares(db,limite=5):
    return list(db.Songs.find().sort("Popularity", -1).limit(limite))