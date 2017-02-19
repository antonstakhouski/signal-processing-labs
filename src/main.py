#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import cmath
import math


class Calculator:
    def __init__(self):
        self.n = 32
        self.start = 0.0
        self.end = 2 * math.pi
        self.step = (self.end - self.start) / self.n
        self.x_array = np.arange(self.start, self.end, self.step)
        self.y_array = self.y(self.x_array)
        self.dft_array = list()

    def y(self, x):
        return np.cos(2 * x) + np.sin(5 * x)

    def dft(self, k):
        m = 0
        c = 0
        w = cmath.exp(cmath.sqrt(-1) * 2 * cmath.pi / self.n)
        while(m < self.n):
            c += self.y_array[m] * w ** (k * m)
            m += 1
        return (1 / self.n) * c

    def idft(self, m):
        k = 0
        x = 0
        w = cmath.exp(cmath.sqrt(-1) * 2 * cmath.pi / self.n)
        while(k < self.n):
            x += self.dft_array[k] * w ** (- (k * m))
            k += 1
        return x

    def draw_signal(self, fignum):
        plt.subplot(fignum)
        plt.title("Default signal")
        plt.plot(self.x_array, self.y_array)

    def draw_dft(self, fignum):
        plt.subplot(fignum)
        plt.title("Discrete Fourier Transform")
        real_array = list()
        self.dft_array.clear()
        for num in self.x_array:
            cnum = self.dft(num)
            real_array.append(cnum.real)
            self.dft_array.append(cnum)
        arr = np.array(real_array)
        plt.plot(self.x_array, arr)

    def draw_idft(self, fignum):
        plt.subplot(fignum)
        plt.title("Inverse Discrete Fourier Transform")
        real_array = list()
        for num in self.x_array:
            cnum = self.idft(num)
            real_array.append(cnum.real)
        arr = np.array(real_array)
        plt.plot(self.x_array, arr)

    def draw(self):
        plt.figure(1)
        self.draw_signal(511)
        self.draw_dft(512)
        self.draw_idft(513)

        plt.show()


if __name__ == '__main__':
    calc = Calculator()
    calc.draw()
