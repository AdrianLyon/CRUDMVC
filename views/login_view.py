# views/login_view.py

import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Inicio de Sesión", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self, text="Usuario:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.entry_username = tk.Entry(self)
        self.entry_username.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self, text="Contraseña:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.grid(row=2, column=1, padx=5, pady=5)

        self.btn_login = tk.Button(self, text="Ingresar", command=self.on_login)
        self.btn_login.grid(row=3, column=0, columnspan=2, pady=10)

    def on_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.controller.autenticar_usuario(username, password)

    def mostrar_error(self, mensaje):
        messagebox.showerror("Error de Inicio de Sesión", mensaje)
