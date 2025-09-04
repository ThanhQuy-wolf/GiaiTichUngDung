import math as m;

def f_1a(x): 
    return m.sqrt(x)

def f_1b(x):
    return m.sqrt(m.sqrt(x))

def f_1c(x):
    return m.pow(x, (2 / 3))

def f_1d(x):
    return (m.pow(x, 3) / 3) - (m.pow(x,2) / 2) - (2*x) + (1/3)

def f_1e(x):
    return (2 * m.pow(x,2) - 3) / (7 * x + 4)

def f_1f(x):
    return (5 * m.pow(x,2) + 8 * x - 3) / (3 * m.pow(x,2) + 2)

def f_1g(x):
    return m.sin(x)

def f_1h(x):
    return m.cos(x)

def f_1i(x):
    return m.pow(3, x)

def f_1j(x):
    return m.pow(10, -x)

def f_1k(x):
    return m.pow(m.e, x)

def f_1l(x):
    return m.log2(x)

def f_1m(x):
    return m.log10(x)

def f_1n(x):
    return m.log(x)
