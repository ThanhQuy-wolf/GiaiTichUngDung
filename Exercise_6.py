import numpy as np
import matplotlib.pyplot as plt

fx_6a = lambda x, k: np.pow(x, 2) + k
fx_6b = lambda x, k: np.pow((x + k), 2)
fx_6c = lambda x, k: k * np.sqrt(x)
fx_6d = lambda x, left, down: np.pow(np.cbrt(x - left), 3) - down;
fx_6e = lambda x, right, down: np.pow(x + right, (2 / 3)) - down
fx_6f = lambda x, right, down: (0.5 * (x + 1 + right) + 5) - down
fx_6g = lambda x, left, down: (1 / np.pow(np.cbrt(x - left), 2)) - down
fx_6h = lambda x: 1 - np.pow(x, 3)
gx_6h = lambda x: fx_6h(x / 2)
fx_6i = lambda x: np.sqrt(x + 1)
gx_6i = lambda x: fx_6i(4 * x)
fx_6j = lambda x: np.sqrt(x + 1)
gx_6j = lambda x: 3 * fx_6j(x)



def draw(fx, k, start, stop, step, color):
    x = np.arange(start, stop + step, step)
    y = np.arange(fx, x, k)
        
    plt.plot(x, y, label="k=" + str(k), color = color)
    plt.legend()
        
        