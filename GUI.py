import customtkinter as ctk
import tkinter
from tkinter import ttk
from PIL import ImageTk, Image


from math_func_3d import main


# Pink Theme  #ff6fff


class Bok_button(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.button_instrucia = ctk.CTkButton(self, text="Инструкция")
        self.button_instrucia.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.button_parametr = ctk.CTkButton(self, text="Параметры")
        self.button_parametr.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.button_funcia = ctk.CTkButton(self, text="Функция")
        self.button_funcia.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("project")
        self.geometry("1600x900")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.bok_button = Bok_button(self)
        self.bok_button.grid(row=0, column=0, padx=5, pady=(10, 0), sticky="nsw", rowspan=4)

        self.slider = ctk.CTkSlider(self, height=30, width=1740)
        self.slider.grid(row=2, column=1, padx=5, pady=10, sticky="ew")

        self.button = ctk.CTkButton(self, text="Построить", width=1740, height=50)
        self.button.grid(row=3, column=1, padx=5, pady=10)

    def button_callback(self):
        print("button pressed")


app = App()
app.mainloop()
