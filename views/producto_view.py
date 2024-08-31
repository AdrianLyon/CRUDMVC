# views/producto_view.py

import tkinter as tk
from tkinter import messagebox, simpledialog

class ProductoView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.pack()
        self.create_widgets()
        self.actualizar_lista()

    def create_widgets(self):
        tk.Label(self, text="Gestión de Productos", font=("Arial", 16)).pack(pady=10)

        self.listbox_productos = tk.Listbox(self, width=50)
        self.listbox_productos.pack(padx=10, pady=10)

        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=5)

        self.btn_agregar = tk.Button(frame_botones, text="Agregar", width=10, command=self.on_agregar)
        self.btn_agregar.grid(row=0, column=0, padx=5)

        self.btn_actualizar = tk.Button(frame_botones, text="Actualizar", width=10, command=self.on_actualizar)
        self.btn_actualizar.grid(row=0, column=1, padx=5)

        self.btn_eliminar = tk.Button(frame_botones, text="Eliminar", width=10, command=self.on_eliminar)
        self.btn_eliminar.grid(row=0, column=2, padx=5)

    def actualizar_lista(self):
        self.listbox_productos.delete(0, tk.END)
        productos = self.controller.obtener_productos()
        for producto in productos:
            self.listbox_productos.insert(tk.END, f"{producto.id}: {producto.nombre} - {producto.descripcion} - ${producto.precio}")

    def on_agregar(self):
        datos = self.obtener_datos_producto()
        if datos:
            nombre, descripcion, precio = datos
            self.controller.agregar_producto(nombre, descripcion, precio)

    def on_actualizar(self):
        seleccion = self.listbox_productos.curselection()
        if seleccion:
            index = seleccion[0]
            producto = self.controller.obtener_productos()[index]
            datos = self.obtener_datos_producto(producto)
            if datos:
                nombre, descripcion, precio = datos
                self.controller.actualizar_producto(producto.id, nombre, descripcion, precio)
        else:
            messagebox.showwarning("Seleccionar Producto", "Por favor, selecciona un producto para actualizar.")

    def on_eliminar(self):
        seleccion = self.listbox_productos.curselection()
        if seleccion:
            index = seleccion[0]
            producto = self.controller.obtener_productos()[index]
            confirm = messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de eliminar '{producto.nombre}'?")
            if confirm:
                self.controller.eliminar_producto(producto.id)
        else:
            messagebox.showwarning("Seleccionar Producto", "Por favor, selecciona un producto para eliminar.")

    def obtener_datos_producto(self, producto=None):
        nombre = simpledialog.askstring("Nombre", "Ingrese el nombre del producto:", initialvalue=producto.nombre if producto else "")
        if not nombre:
            messagebox.showerror("Datos Incompletos", "El nombre es obligatorio.")
            return None

        descripcion = simpledialog.askstring("Descripción", "Ingrese la descripción del producto:", initialvalue=producto.descripcion if producto else "")
        if not descripcion:
            messagebox.showerror("Datos Incompletos", "La descripción es obligatoria.")
            return None

        try:
            precio = float(simpledialog.askstring("Precio", "Ingrese el precio del producto:", initialvalue=str(producto.precio) if producto else ""))
        except (TypeError, ValueError):
            messagebox.showerror("Datos Inválidos", "El precio debe ser un número.")
            return None

        return nombre, descripcion, precio
