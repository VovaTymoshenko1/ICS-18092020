import numpy as np
import matplotlib.pylab as plt

def ff(x):
    return -5*np.cos(10*x)*np.sin(3*x)/(x**x)

x = np.arange (0, 5, 0.05)

fig, ax=plt.subplots()
ax.grid()
ax.plot(x, ff(x))

fig.savefig('d:/task1.png')