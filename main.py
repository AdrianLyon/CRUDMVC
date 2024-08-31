# main.py

import tkinter as tk
from models.modelo import Modelo
from controllers.login_controller import LoginController

def main():
    root = tk.Tk()
    root.title("Aplicación MVC con Tkinter")
    root.geometry("400x300")
    modelo = Modelo()
    app = LoginController(root, modelo)
    root.mainloop()

if __name__ == "__main__":
    main()
