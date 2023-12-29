import numpy as np
import matplotlib.pyplot as plt

plt.ion()  # Turn on interactive mode

x_values = []
y_values = []

for time in np.arange(0, 100, 2):  # Generate time values with 0.1-second steps
    x = time
    y = 1.0128 * x / (1 + 0.0128 * x)  # Adjust formula if needed to incorporate time

    x_values.append(x)
    y_values.append(y)
    plt.clf()
    # Clear the previous plot
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.plot(x_values, y_values, color='blue')  # Use plot() for a line plot
    plt.xlabel("$\\tilde{e}_w$")
    plt.ylabel("$\\tilde{e}_a$")
    plt.pause(1)

plt.show()
