import math as m
import numpy as np

f1 = lambda x: x + 5
f2 = lambda x: m.pow(x, 2) -3

def f_3a():
    return f1(f2(0))

def f_3b():
    return f2(f1(0))

def f_3c():
    return f1(f1(-5))

def f_3d():
    return f2(f2(2))

print("Cau 3a: ", f_3a())
print("Cau 3b: ", f_3b())
print("Cau 3c: ", f_3c())
print("Cau 3d: ", f_3d())