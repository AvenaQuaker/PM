# clase producto
class Producto:
    def __init__(self, nombre, precio, stock): # Constructor
        self.nombre = nombre 
        self.__precio = precio 
        self.stock = stock

    @property # Getter
    def precio(self): 
        return self.__precio

    def calcular_costo(self): # Metodo 
        return self.precio

    def __str__(self):  
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"
    
# Clase ProductoDigital
class ProductoDigital(Producto): 
    def __init__(self, nombre, precio): # Constructor 
        super().__init__(nombre, precio, -1)

    def calcular_costo(self): # Metodo
      return self.precio * 0.9

    def __str__(self): #    Metodo
        return f"{self.nombre} (Digital) - ${self.precio}"
    
# Clase Cliente
class Cliente: 
    def __init__(self, nombre, email): 
        self.nombre = nombre 
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nombre} ({self.email})"
    
# Clase Carrito
class Carrito: 
    def __init__(self): 
        self.productos = []

# Metodo para agregar un producto al carrito
    def agregar_producto(self, producto):
        if producto.stock > 0 or producto.stock == -1:  # -1 para digitales
            self.productos.append(producto)
            if producto.stock != -1:
                producto.stock -= 1
            return True
        return False

# Metodo para calcular el total del carrito
    def calcular_total(self):
        return sum(p.calcular_costo() for p in self.productos) if self.productos else 0

    def __str__(self):
        return "\n".join(str(p) for p in self.productos) or "Carrito vacío"
    
# Clase Tienda
class Tienda: 
    def __init__(self): 
        self.catalogo = []

# Metodo para agregar un producto al catalogo
    def agregar_al_catalogo(self, producto):
        self.catalogo.append(producto)

# Metodo para buscar un producto en el catalogo
    def buscar_producto(self, nombre):
        for producto in self.catalogo:
            if producto.nombre == nombre:
                return producto
        return None
    
# Metodo para realizar una compra
    def realizar_compra(self, cliente, carrito):
        if not carrito.productos:
            return "Compra cancelada: carrito vacío."
        total = carrito.calcular_total()
        return f"Compra de {cliente}:\n{carrito}\nTotal: ${total}"
    
# Simulación 
tienda = Tienda() 
tienda.agregar_al_catalogo(Producto("Libro", 20, 5)) 
tienda.agregar_al_catalogo(ProductoDigital("Ebook", 20)) 
tienda.agregar_al_catalogo(Producto("Costillas", 80, 19))
tienda.agregar_al_catalogo(Producto("Papas", 10, 100))
tienda.agregar_al_catalogo(ProductoDigital("Videojuego", 50))

cliente = Cliente("Jaime Aquino", "JaimeA@mail.com") 
carrito = Carrito() 

# Prueba de la simulación
print("Bievenido")
print("Catalogo de productos:")
for producto in tienda.catalogo:
    print(producto)

# Agregar productos al carrito
opcion = True
while(opcion == True):
    print("Teclee el nombre del producto deseado:")
    producto = input()
    producto = tienda.buscar_producto(producto)
    if producto != None:
        carrito.agregar_producto(producto)
    else:
        print("Producto no encontrado")
    print("Desea agregar otro producto? (S/N)")
    respuesta = input()
    if respuesta == "N":
        opcion = False

print(tienda.realizar_compra(cliente, carrito))
