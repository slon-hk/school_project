import customtkinter as ctk
import tkinter
from tkinter import ttk
from PIL import ImageTk, Image


import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from mpl_toolkits.mplot3d import Axes3D


symbol_x = sp.Symbol("x")
symbol_y = sp.Symbol("y")

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
        self.bok_button.grid(
            row=0, column=0, padx=5, pady=(10, 0), sticky="nsw", rowspan=4
        )

        # self.graf = pass
        # self.graf.grid(row=0, column=1, padx=10, pady=10)

        self.pole_vvoda = ctk.CTkEntry(
            self, height=50, width=1740, placeholder_text="Введите функцию"
        )
        self.pole_vvoda.grid(row=1, column=1, padx=5, pady=10, sticky="ew")

        self.slider = ctk.CTkSlider(self, height=30, width=1740)
        self.slider.grid(row=2, column=1, padx=5, pady=10, sticky="ew")

        self.button = ctk.CTkButton(
            self, text="Построить", command=self.button_callback, width=1740, height=50
        )
        self.button.grid(row=3, column=1, padx=5, pady=10)

    def button_callback(self):
        print(999)


app = App()
app.mainloop()
