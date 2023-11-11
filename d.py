import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


class ploskey_graf:
    def __init__(self, x, y):
        self.t = sp.Symbol("t")

        self.function_x = sp.sympify(x)
        self.function_y = sp.sympify(y)
        self.interval = np.arange(1.5, 20.5, 0.01)

        self.x_values = [self.function_x.subs(self.t, value) for value in self.interval]
        self.y_values = [self.function_y.subs(self.t, value) for value in self.interval]

    def show(self):
        plt.figure(figsize=(10, 10))
        plt.plot(self.x_values, self.y_values)
        plt.show()


if __name__ == "__main__":
    app = ploskey_graf("t - 1.6*cos(24*t)", "t - 1.6*sin(25*t)")
    app.show()
