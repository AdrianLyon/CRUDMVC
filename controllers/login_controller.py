# controllers/login_controller.py

import tkinter as tk
from controllers.producto_controller import ProductoController
from views.login_view import LoginView
from views.producto_view import ProductoView

class LoginController:
    def __init__(self, master, modelo):
        self.master = master
        self.modelo = modelo
        self.view = LoginView(master, self)

    def autenticar_usuario(self, username, password):
        if self.modelo.autenticar_usuario(username, password):
            self.mostrar_crud_productos()
        else:
            self.view.mostrar_error("Usuario o contraseña incorrectos.")

    def mostrar_crud_productos(self):
        self.view.destroy()
        self.view = ProductoView(self.master, ProductoController(self.master, self.modelo))
