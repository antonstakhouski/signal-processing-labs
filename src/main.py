#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import cmath


class Calculator:
    def __init__(self):
        self.n = 32
        self.start = 0.0
        self.end = 2000.0
        self.step = (self.end - self.start) / self.n
        self.x_array = np.arange(self.start, self.end, self.step)

    def y(self, x):
        return np.cos(2 * x) + np.sin(5 * x)

    def dft(self, k):
        m = 0
        c = 0
        w = cmath.exp(cmath.sqrt(-1) * 2 * cmath.pi / self.n)
        while(m < self.n):
            c += self.y(m) * w ** (k * m)
        return (1 / self.n) * c

    def draw(self):
        plt.figure(1)

        plt.subplot(111)
        plt.title("Default signal")
        plt.plot(self.x_array, self.y(self.x_array))

        # plt.subplot(222)
        # plt.title("Discrete Fourier Transform")
        # plt.plot(self.x_array, self.dft(self.x_array))

        plt.show()


if __name__ == '__main__':
    calc = Calculator()
    calc.draw()
