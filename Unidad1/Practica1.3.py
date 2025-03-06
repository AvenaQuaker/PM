# Herencia

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar_datos(self):
        return f"Nombre: {self.nombre} Email: {self.email}"
    
class Cliente(Usuario):
    def __init__(self, nombre, email, id_cliente):
        super().__init__(nombre, email)
        self.id_cliente = id_cliente
    
    def mostrar_datos(self):
        return f"Cliente: {self.nombre} Email: {self.email} ID: {self.id_cliente}"
    
class Administrador(Usuario):
    def __init__(self, nombre, email, nvl_acceso):
        super().__init__(nombre, email)
        self.nvlAcceso = nvl_acceso
    
    def mostrar_datos(self):
        return f"Admin: {self.nombre} Email: {self.email} ID: {self.nvlAcceso}"
    
# Test
cliente = Cliente("Juan","juan.av@nvladreod.tecnm.mx","D654")
admin = Administrador("Antonio","JoseAntonio@nalrdeo.tencm.mx","Alto")
print(cliente.mostrar_datos())
print(admin.mostrar_datos())

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio
        self.stock = stock

    @property
    def precio(self):
        return self.__precio
    
    def calcularCosto(self):
        return self.__precio
    
    def __str__(self):
        return f"Nombre: {self.nombre} Precio: {self.precio} Stock: {self.stock} es PRODUCTO"
    
class ProductoFisico(Producto):
    def __init__(self, nombre, precio, stock, peso):
        super().__init__(nombre, precio, stock)
        self.peso = peso
        
    def calcularCosto(self):
        return super().calcularCosto() + self.peso * 0.1

class ProductoDigital(Producto):
    def __init__(self, nombre, precio,stock,costo_envio):
        super().__init__(nombre, precio,stock)
        self.costo_envio = costo_envio
        
    def calcularCosto(self):
        return self.precio + self.costo_envio
    
# Polimorfismo

productos = [ Producto("Libro",20,10), ProductoFisico("Laptop",20000,5,12), ProductoDigital("Celular",5000,10,50) ]

for producto in productos:
    print(f"Producto: {producto.nombre} Precio: {producto.calcularCosto()}")

class ProductoMalo:
    def __init__(self, nombre, precio, tipo):
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
    
    def calcularCosto(self):
        if self.tipo == "Fisico":
            return self.precio * 0.9
        else:
            return self.precio + 5
        return self.precio
    
class ProductoDigital2(Producto):
    def __init__(self, nombre, precio, stock = -1):
        super().__init__(nombre, precio, stock)
    
    def calcularCosto(self):
        return self.precio * 1.1

    def disponible(self):
        return True
    
    def __str__(self):
        return f"Producto: {self.nombre} Precio: {self.precio} es DIGITAL"

class ProductoFisico2(Producto):
    def __init__(self, nombre, precio, costoEnvio,stock ):
        super().__init__(nombre, precio, stock)
        self.costoEnvio = costoEnvio
    
    def calcularCosto(self):
        return self.precio + self.costoEnvio
    
    def disponible(self):
        return self.stock > 0
    
    def __str__(self):
        return f"Producto: {self.nombre} Precio: {self.precio} es FISICO"
    
# Test Polimorfismo
prod = Producto("Libro",20,5)
digital = ProductoDigital2("Laptop",20000)
fisico = ProductoFisico2("Celular",5000,50,100)

print(prod)
print(digital)
print(fisico)