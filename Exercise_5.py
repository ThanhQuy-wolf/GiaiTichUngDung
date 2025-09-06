import matplotlib.pyplot as plt
import numpy as np

fx_1 = lambda x: np.sqrt(1 - np.pow(abs(x) - 1, 2))
fx_2 = lambda x: -3 * np.sqrt(1 - np.sqrt(abs(x) / 2))

def draw(fx, start, stop, step, color, label):
    x_array = np.arange(start, (stop + step), step)
    y_array = list( map(fx, x_array))

    plt.plot(x_array, y_array, color=color, label = label)
    plt.legend()