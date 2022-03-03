import matplotlib.pyplot as plt
import numpy as np
import io

x = np.arange(0, 100, 0.00001)
y = x * np.sin(2 * np.pi * x)
plt.plot(y)
f = io.StringIO()
plt.savefig(f, format="svg")
