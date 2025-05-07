import unittest
from Unidad2.Jaime_Aquino_SimuladorTienda import Tienda, Producto, ProductoDigital, Cliente, Carrito

class TestTienda(unittest.TestCase):
    def setUp(self): # Inicializacion del modulo unitest
        self.tienda = Tienda()
        self.tienda.agregar_al_catalogo(Producto("Libro", 20, 5))
        self.tienda.agregar_al_catalogo(ProductoDigital("Ebook", 20))
        self.tienda.agregar_al_catalogo(Producto("Costillas", 80, 19))
        self.tienda.agregar_al_catalogo(Producto("Papas", 10, 100))
        self.tienda.agregar_al_catalogo(ProductoDigital("Videojuego", 50))
        self.cliente = Cliente("Jaime Aquino", "JaimeA@gmail.com")
        self.carrito = Carrito()

    # Probar si se agrega un producto al catalogo
    def test_agregar_al_catalogo(self):
        self.assertEqual(len(self.tienda.catalogo), 5)

    # Probar si se busca un producto existente
    def test_buscar_producto_existente(self):
        producto = self.tienda.buscar_producto("Libro")
        self.assertIsNotNone(producto)
        self.assertEqual(producto.nombre, "Libro")

    # Probar si se busca un producto inexistente
    def test_buscar_producto_inexistente(self):
        producto = self.tienda.buscar_producto("Inexistente")
        self.assertIsNone(producto)

    # Probar si se agrega un producto al carrito
    def test_agregar_producto_al_carrito(self):
        producto = self.tienda.buscar_producto("Libro")
        self.assertTrue(self.carrito.agregar_producto(producto))
        self.assertEqual(len(self.carrito.productos), 1)

    # Probar si se agrega un producto sin stock al carrito
    def test_agregar_producto_sin_stock(self):
        producto = self.tienda.buscar_producto("Libro")
        for _ in range(5): 
            self.carrito.agregar_producto(producto)
        self.assertFalse(self.carrito.agregar_producto(producto)) 

    # Probar si se calcula el total del carrito
    def test_calcular_total_carrito(self):
        self.carrito.agregar_producto(self.tienda.buscar_producto("Libro"))
        self.carrito.agregar_producto(self.tienda.buscar_producto("Ebook"))
        self.assertEqual(self.carrito.calcular_total(), 38) 

    # Probar si se calcula el total del carrito vacio
    def test_realizar_compra(self):
        self.carrito.agregar_producto(self.tienda.buscar_producto("Libro"))
        resultado = self.tienda.realizar_compra(self.cliente, self.carrito)
        self.assertIn("Compra de Cliente: Jaime Aquino", resultado)
        self.assertIn("Total: $20", resultado)

    # Probar si se realiza una compra con el carrito vacio
    def test_realizar_compra_carrito_vacio(self):
        resultado = self.tienda.realizar_compra(self.cliente, self.carrito)
        self.assertEqual(resultado, "Compra cancelada: carrito vacío.")

if __name__ == "__main__":
    unittest.main()