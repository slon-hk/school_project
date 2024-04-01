import customtkinter as ctk
import tkinter
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

from math import *
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


class MyTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # РЎРѓР С•Р В·Р Т‘Р В°Р Р…Р С‘Р Вµ Р Р†Р С”Р В»Р В°Р Т‘Р С•Р С”
        self.add("Функции")
        self.add("Инструкция")

        # Р Т‘Р С•Р В±Р В°Р Р†Р В»Р ВµР Р…Р С‘Р Вµ Р Р†Р С‘Р Т‘Р В¶Р ВµРЎвЂљР С•Р Р† Р Р…Р В° Р Р†Р С”Р В»Р В°Р Т‘Р С”Р С‘
        self.pole_vvoda = ctk.CTkEntry(
            master=self.tab("Функции"),
            height=50,
            width=740,
            placeholder_text="Введите текст",
        )
        self.pole_vvoda.grid(
            row=1, column=1, padx=5, pady=10, sticky="ew", columnspan=2
        )

        # slider
        self.slider = ctk.CTkSlider(
            master=self.tab("Функции"), height=30, width=740, from_=1, to=0.01
        )
        self.slider.grid(row=2, column=1, padx=5, pady=10, sticky="ew", columnspan=2)

        # enter button
        self.button = ctk.CTkButton(
            master=self.tab("Функции"),
            text="Построить",
            command=self.button_callback,
            width=360,
            height=50,
        )
        self.button.grid(row=3, column=1, padx=5, pady=10)

        self.clear_button = ctk.CTkButton(
            master=self.tab("Функции"),
            text="Отчистить",
            command=plt.clf,
            width=360,
            height=50,
        )
        self.clear_button.grid(row=3, column=2, padx=5, pady=10)

        # TAB 2
        self.my_frame = MyFrame(master=self.tab("Инструкция"), width=700, height=400)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20)

    def button_callback(self):
        Grafic_output(self.pole_vvoda.get(), self.slider.get()).main()
        plt.show()


class MyFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        text = """
        Данная программа предназначена для построения моделей в пространстве. Ниже приведены\n        все математические функции которые поддерживаются программой

        Сложение двух чисел - x+n

        Вычитание двух чисел - x-n

        Умножение - x*n

        Деление двух чисел - x/n

        Целочисленное деление двух чисел - x//n

        Получение остатка от деления - x%n

        Возведение в степень - x**n

        fabs(X) - модуль X.

        factorial(X) - факториал числа X.

        floor(X) - округление вниз.

        fmod(X, Y) - остаток от деления X на Y.

        frexp(X) - возвращает мантиссу и экспоненту числа.

        ldexp(X, I) - X * 2I. Функция, обратная функции math.frexp().

        fsum(последовательность) - сумма всех членов последовательности. Эквивалент встроенной\n        функции sum(), но math.fsum() более точна для чисел с плавающей точкой.

        modf(X) - возвращает дробную и целую часть числа X. Оба числа имеют тот же знак, что и X.

        trunc(X) - усекает значение X до целого.

        exp(X) - eX.

        log(X, [base]) - логарифм X по основанию base. Если base не указан, вычисляется натуральный\n        логарифм.

        log1p(X) - натуральный логарифм (1 + X). При X → 0 точнее, чем math.log(1+X).

        log10(X) - логарифм X по основанию 10.

        log2(X) - логарифм X по основанию 2.

        pow(X, Y) - XY.

        sqrt(X) - квадратный корень из X.

        acos(X) - арккосинус X. В радианах.

        asin(X) - арксинус X. В радианах.

        atan(X) - арктангенс X. В радианах.

        atan2(Y, X) - арктангенс Y/X. В радианах. С учетом четверти, в которой находится точка (X, Y).

        cos(X) - косинус X (X указывается в радианах).

        sin(X) - синус X (X указывается в радианах).

        tan(X) - тангенс X (X указывается в радианах).

        degrees(X) - конвертирует радианы в градусы.

        radians(X) - конвертирует градусы в радианы.

        cosh(X) - вычисляет гиперболический косинус.

        sinh(X) - вычисляет гиперболический синус.

        tanh(X) - вычисляет гиперболический тангенс.

        acosh(X) - вычисляет обратный гиперболический косинус.

        asinh(X) - вычисляет обратный гиперболический синус.

        atanh(X) - вычисляет обратный гиперболический тангенс.

        gamma(X) - гамма-функция X.

        lgamma(X) - натуральный логарифм гамма-функции X.

        pi - pi = 3,1415926...

        e - e = 2,718281...

        Более подробный список функций вы можете найти в документации встроенной библиотеки\n\n        python - math, numpy и matplotlib"""

        self.label = ctk.CTkLabel(
            self, text=text, justify="left", height=100, width=750
        )
        self.label.grid(row=0, column=0, padx=20)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("project")
        self.geometry("800x600")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=0)

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)


app = App()
app.mainloop()
