import math as m
import numpy as np

def Find_fmin(f, start, stop):
    fmin = f(start)
    for x in np.arange(start, stop + 0.1, 0.1):
        fnext = f(x)
        if fnext < fmin:
            fmin = fnext
    return fmin

def Find_fmax(f, start, stop):
    fmax = f(start)
    for x in np.arange(start, stop + 0.1, 0.1):
        fnext = f(x)
        if fnext > fmax:
            fmax = fnext
    return fmax

def f_2a(x):
    return 2 + (m.pow(x, 2) / (m.pow(x, 2) + 4))

def f_2b(x):
    return m.sqrt(5 * x + 10)

def f_2c(x):
    return 2 / (m.pow(x, 2) - 16)

def f_2d(x):
    return m.pow(x, 4) + (3 * m.pow(x, 2)) - 1

def f_2e(x):
    if x >= 0:
        return x
    else:
        return -x
    
def Cau_2a():
    print("Max: ", Find_fmax(f_2a, -2, 2))
    print("Min: ", Find_fmin(f_2a, -2, 2))

def Cau_2b():
    print("Max: ", Find_fmax(f_2b, 0, 5))
    print("Min: ", Find_fmin(f_2b, 0, 5))

Cau_2a()
Cau_2b()