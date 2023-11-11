import customtkinter as ctk
import tkinter
from tkinter import ttk
from PIL import ImageTk, Image


import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D

toch = 0
symbol_x = sp.Symbol("x")
symbol_y = sp.Symbol("y")


class Postroen_graf(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.a_value = -10
        self.b_value = 10
        global toch
        # self.tochnost = toch

    def main(self, function):
        if "x" and not "y" in function:
            self.plot_2d_function(function, self.a_value, self.b_value)
        elif "x" and "y" in function:
            self.plot_3d_function(function, self.a_value, self.b_value)
        else:
            print("You must enter a function in terms of x and/or y")

    def get_vector(self, a, b):
        return np.arange(a, b + 1, 0.5)

    def plot_2d_function(self, function, a, b):
        fig, ax = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10)

        # Create the sympy function f(x)
        f_x = sp.sympify(function)

        # Create domain and image
        domain_x = self.get_vector(a, b)
        image = [f_x.subs(symbol_x, value) for value in domain_x]

        # Plot the 2D function graph
        fig = plt.figure(figsize=(10, 10))
        plt.plot(domain_x, image)
        canvas.draw()

    def plot_3d_function(self, function, a, b):
        fig, ax = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10)
        # Create sympy function f(x, y)
        f_xy = sp.lambdify((symbol_x, symbol_y), sp.sympify(function))

        # Create domains and image
        domain_x = self.get_vector(a, b)
        domain_y = self.get_vector(a, b)
        domain_x, domain_y = np.meshgrid(domain_x, domain_y)
        image = f_xy(domain_x, domain_y)

        # Plot the 3D function graph
        fig = plt.figure(figsize=(10, 10))
        ax = plt.axes(projection="3d")
        ax.plot_surface(domain_x, domain_y, image, rstride=1, cstride=1, cmap="viridis")
        canvas.draw()


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

        self.graf = Postroen_graf(self)
        self.graf.grid(row=0, column=1, padx=10, pady=10)
        self.graf.main("x**2")

        self.pole_vvoda = ctk.CTkEntry(self, height=50, width=1740, placeholder_text="Введите функцию")
        self.pole_vvoda.grid(row=1, column=1, padx=5, pady=10, sticky="ew")

        self.slider = ctk.CTkSlider(self, height=30, width=1740)
        self.slider.grid(row=2, column=1, padx=5, pady=10, sticky="ew")

        self.button = ctk.CTkButton(self, text="Построить", command=self.button_callback, width=1740, height=50)
        self.button.grid(row=3, column=1, padx=5, pady=10)

    def button_callback(self):
        print("button pressed")


app = App()
app.mainloop()
