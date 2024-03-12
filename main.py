import customtkinter as ctk
import tkinter
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class Grafic_output:
    def __init__(self, function, tochnost):
        self.function = function
        self.symbol_x = sp.Symbol("x")
        self.symbol_y = sp.Symbol("y")
        self.a_value = -10
        self.b_value = 10
        self.toch = tochnost

    def main(self):
        if "x" and not "y" in self.function:
            self.plot_2d_function(self.function, self.a_value, self.b_value)
        elif "x" and "y" in self.function:
            self.plot_3d_function(self.function, self.a_value, self.b_value)
        else:
            print("You must enter a function in terms of x and/or y")

    def get_vector(self, a, b):
        return np.arange(a, b + 1, self.toch)

    def plot_2d_function(self, function, a, b):
        # Create the sympy function f(x)
        f_x = sp.sympify(function)
        # Create domain and image
        domain_x = self.get_vector(a, b)
        image = [f_x.subs(self.symbol_x, value) for value in domain_x]

        # Plot the 2D function graph
        # fig = plt.figure(figsize=(10, 10))
        plt.plot(domain_x, image)
        # plt.show()

    def plot_3d_function(self, function, a, b):
        # Create sympy function f(x, y)
        f_xy = sp.lambdify((self.symbol_x, self.symbol_y), sp.sympify(function))

        # Create domains and image
        domain_x = self.get_vector(a, b)
        domain_y = self.get_vector(a, b)
        domain_x, domain_y = np.meshgrid(domain_x, domain_y)
        image = f_xy(domain_x, domain_y)

        # Plot the 3D function graph
        # fig = plt.figure(figsize=(10, 10))
        ax = plt.axes(projection="3d")
        ax.plot_surface(domain_x, domain_y, image, rstride=1, cstride=1, cmap="viridis")
        # plt.show()


class Bok_button(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.button_instrucia = ctk.CTkButton(self, text="Инструкция")
        self.button_instrucia.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.button_parametr = ctk.CTkButton(self, text="Параметр")
        self.button_parametr.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.button_funcia = ctk.CTkButton(self, text="Функции")
        self.button_funcia.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("project")
        self.geometry("600x900")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # setting button
        self.bok_button = Bok_button(self)
        self.bok_button.grid(
            row=0, column=0, padx=5, pady=(10, 0), sticky="nsw", rowspan=4
        )

        # entery
        self.pole_vvoda = ctk.CTkEntry(
            self,
            height=50,
            width=1740,
            placeholder_text="Введите текст",
        )
        self.pole_vvoda.grid(
            row=1, column=1, padx=5, pady=10, sticky="ew", columnspan=2
        )

        # slider
        self.slider = ctk.CTkSlider(self, height=30, width=1740)
        self.slider.grid(row=2, column=1, padx=5, pady=10, sticky="ew", columnspan=2)

        # enter button
        self.button = ctk.CTkButton(
            self,
            text="Построить",
            command=self.button_callback,
            width=850,
            height=50,
        )
        self.button.grid(row=3, column=1, padx=5, pady=10)

        self.clear_button = ctk.CTkButton(
            self, text="Отчистить", command=plt.clf, width=850, height=50
        )
        self.clear_button.grid(row=3, column=2, padx=5, pady=10)

    def button_callback(self):
        Grafic_output(self.pole_vvoda.get(), 0.2).main()
        plt.show()


app = App()
app.mainloop()
