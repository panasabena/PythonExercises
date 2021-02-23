import numpy as np
import matplotlib.pyplot as plt

ys = 200 + np.random.randn(100)
x = np.arange(100)

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()
