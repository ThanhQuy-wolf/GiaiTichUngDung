import matplotlib.pyplot as plt
import numpy as np

fx_1 = lambda x: np.sqrt(1 - np.pow(abs(x) - 1, 2))
fx_2 = lambda x: -3 * np.sqrt(1 - np.sqrt(abs(x) / 2))

def draw(fx, start, stop, step, color, label):
    x_array = np.arange(start, (stop + step), step)
    y_array = list( map(fx, x_array))

    plt.plot(x_array, y_array, color=color, label = label)
    plt.legend()

# Main
draw(fx_1, -5, 5, 0.0001, "magenta", "y = fx(1)")
draw(fx_2, -5, 5, 0.0001, "red", "y = fx(2)")
plt.grid()
plt.show()
