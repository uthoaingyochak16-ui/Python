import numpy as np
import matplotlib.pyplot as plt

# 1. Create data using NumPy
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 2. Plot the data
plt.plot(x, y, label='Sine Wave', color='blue', linestyle='--')

# 3. Add documentation/labels
plt.title("NumPy Plot in VS Code")
plt.xlabel("X Axis (Time)")
plt.ylabel("Y Axis (Amplitude)")
plt.legend()

# 4. Show the result
plt.show()
