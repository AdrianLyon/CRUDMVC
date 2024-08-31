# models/modelo.py

class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Producto:
    _id = 1

    def __init__(self, nombre, descripcion, precio):
        self.id = Producto._id
        Producto._id += 1
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

class Modelo:
    def __init__(self):
        # Usuarios de ejemplo
        self.usuarios = [
            Usuario("admin", "admin123"),
            Usuario("user", "user123")
        ]

        # Productos de ejemplo
        self.productos = [
            Producto("Laptop", "Portátil de 15 pulgadas", 1500.00),
            Producto("Smartphone", "Teléfono inteligente", 800.00)
        ]

    # Métodos para autenticación
    def autenticar_usuario(self, username, password):
        for usuario in self.usuarios:
            if usuario.username == username and usuario.password == password:
                return True
        return False

    # Métodos CRUD para productos
    def obtener_productos(self):
        return self.productos

    def agregar_producto(self, nombre, descripcion, precio):
        producto = Producto(nombre, descripcion, precio)
        self.productos.append(producto)

    def actualizar_producto(self, producto_id, nombre, descripcion, precio):
        for producto in self.productos:
            if producto.id == producto_id:
                producto.nombre = nombre
                producto.descripcion = descripcion
                producto.precio = precio
                return True
        return False

    def eliminar_producto(self, producto_id):
        for producto in self.productos:
            if producto.id == producto_id:
                self.productos.remove(producto)
                return True
        return False
