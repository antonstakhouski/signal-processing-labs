#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import cmath
import math
import matplotlib.gridspec as gridspec
#  import ipdb


class Calculator:
    def __init__(self):
        self.n = 32
        self.start = 0.0
        self.end = 2 * math.pi
        self.step = (self.end - self.start) / self.n
        self.x_array = np.arange(self.start, self.end, self.step)
        self.y_array = self.y(self.x_array)
        self.dft_array = list()
        self.count = 0

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

    def fft_dit(self, a, direct):
        if len(a) == 1:
            return a
        a_even = list()
        a_odd = list()
        i = 0
        while (i < len(a)):
            if i % 2 == 0:
                a_even.append(a[i])  # четный
            else:
                a_odd.append(a[i])
            i += 1
        b_even = self.fft_dit(a_even, direct)
        b_odd = self.fft_dit(a_odd, direct)

        #  print(self.count)
        self.count += 1

        #  print(b_even)
        #  print(b_odd)
        argument = 2 * cmath.pi / len(a)
        wn = cmath.cos(argument) + direct * cmath.sqrt(-1) * cmath.sin(argument)

        w = np.complex(1)
        #  print(w)

        y = [np.complex(0)] * len(a)
        j = 0
        while(j < len(a) // 2):
            y[j] = b_even[j] + w * b_odd[j]
            #  print(y[j])
            #  self.t(y[j])
            y[j + len(a) // 2] = b_even[j] - w * b_odd[j]
            #  print(y[j] + len(a) // 2)
            #  self.t(y[j] + len(a) // 2)
            w *= wn
            j += 1
        #  print(y)
        return y

    def t(self, x):
        print(type(x))

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
        abs_y = np.absolute(self.y_array)
        plt.vlines(self.x_array, 0, abs_y)

    def draw_dft(self, fignum):
        plt.subplot(fignum)
        plt.title("Discrete Fourier Transform")
        self.dft_array.clear()
        i = 0
        while i < self.n:
            cnum = self.dft(i)
            self.dft_array.append(cnum)
            i += 1
        arr = np.array(self.dft_array)
        abs_y = np.absolute(arr)
        plt.vlines(self.x_array, 0, abs_y)

    def draw_idft(self, fignum):
        plt.subplot(fignum)
        plt.title("Inverse Discrete Fourier Transform")
        idft_array = list()
        i = 0
        while i < self.n:
            idft_array.append(self.idft(i))
            i += 1
        arr = np.array(idft_array)
        abs_y = np.absolute(arr)
        plt.vlines(self.x_array, 0, abs_y)

    def draw_fft(self, fignum):
        plt.subplot(fignum)
        plt.title("Fast Fourier Transform")
        fft_array = self.fft_dit(self.y_array, -1)
        self.dft_array = fft_array
        #  print(type(fft_array[0]))
        print(fft_array)

        abs_y = list()
        for num in fft_array:
            abs_y.append(np.absolute(num.real))
        plt.vlines(self.x_array, 0, abs_y)

    def draw_fft_inv(self, fignum):
        plt.subplot(fignum)
        plt.title("Inverse Fast Fourier Transform")
        fft_array = self.fft_dit(self.dft_array, 1)
        arr = np.array(fft_array)

        fft_real = list()
        abs_y = list()
        for num in arr:
            fft_real.append(num)
            abs_y.append(np.absolute(num))
        plt.vlines(self.x_array, 0, abs_y)

    def draw(self):
        gs = gridspec.GridSpec(2, 3)
        self.draw_signal(gs[0, 0])
        self.draw_dft(gs[0, 1])
        self.draw_idft(gs[1, 1])

        self.draw_fft(gs[0, 2])
        self.draw_fft_inv(gs[1, 2])
        plt.show()


if __name__ == '__main__':
    calc = Calculator()
    #  ipdb.set_trace()
    #  calc.fft_dit(calc.x_array, calc.n, 1)
    calc.draw()
