import matplotlib.pyplot as plt
import numpy as np

fx_4i = lambda x: np.pow(-x, 3)
fx_4j = lambda x: -1 / np.pow(x, 2)
fx_4k = lambda x: -1 / x
fx_4l = lambda x: 1 / np.fabs(x)
fx_4m = lambda x: np.sqrt(np.fabs(x))
fx_4n = lambda x: np.sqrt(np.fabs(-x))

def draw(fx, start, stop, step, color, label):
    x_array = np.arange(start, (stop + step), step)
    y_array = list( map(fx, x_array))

    plt.plot(x_array, y_array, color=color, label = label)
    plt.grid()
    plt.legend()
    plt.show()
