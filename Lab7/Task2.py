import matplotlib.pylab as plt
from collections import Counter
import collections
import os
import matplotlib.pylab as plt
import numpy as np

book = 'text.txt'
file = open(book, 'r')
data = file.read().lower()
d1 = dict()

for c in data:
    if c in d1:
        d1[c] = d1[c]+1
    else:
        d1[c] = 1


pos = np.arange(len(d1.keys()))
width = 1.0     # gives histogram aspect to the bar diagram

fig, ax = plt.subplots()
ax.set_xticks(pos)
ax.set_xticklabels(d1.keys())

plt.bar(pos, d1.values(), width, color='r')
#plt.show()

fig.savefig('d:/task2.png')
