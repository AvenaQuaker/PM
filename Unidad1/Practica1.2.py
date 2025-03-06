class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio
        self.stock = stock
    
    @property
    def precio(self):
        return self.__precio
    
    def disponible(self):
        return self.stock > 0
    
    def __str__(self):
        return f"Nombre: {self.nombre} Precio: {self.precio} Stock: {self.stock}"

    

# Test
catalogo = [
    Producto("Libro",15.99,5)
    ,Producto("Lapiz",2.5,10)
    ,Producto("Borrador",1.5,0)
    ,Producto("Cuaderno",5.0,3)
    ,Producto("Pluma",3.0,0)
    ]

for producto in catalogo:
    if producto.disponible():
        print(producto)
        print("Disponible")