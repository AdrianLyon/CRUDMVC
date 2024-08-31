# controllers/producto_controller.py

from views.producto_view import ProductoView

class ProductoController:
    def __init__(self, master, modelo):
        self.master = master
        self.modelo = modelo
        self.view = ProductoView(master, self)

    def obtener_productos(self):
        return self.modelo.obtener_productos()

    def agregar_producto(self, nombre, descripcion, precio):
        self.modelo.agregar_producto(nombre, descripcion, precio)
        self.view.actualizar_lista()

    def actualizar_producto(self, producto_id, nombre, descripcion, precio):
        if self.modelo.actualizar_producto(producto_id, nombre, descripcion, precio):
            self.view.actualizar_lista()
        else:
            from tkinter import messagebox
            messagebox.showerror("Error", "No se pudo actualizar el producto.")

    def eliminar_producto(self, producto_id):
        if self.modelo.eliminar_producto(producto_id):
            self.view.actualizar_lista()
        else:
            from tkinter import messagebox
            messagebox.showerror("Error", "No se pudo eliminar el producto.")
