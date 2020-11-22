import matplotlib.pylab as plt
from collections import Counter
import collections
import os
import matplotlib.pylab as plt
import numpy as np

book = 'text.txt'
file = open(book, 'r')
data = file.read()

dots = data.count('.')
question = data.count('?')
exclamation = data.count('!') 

d1 = {'звичайні речення', "питальні речення", "окличні речення"}
d2 = {dots, question, exclamation}

pos = np.arange(len(d1))
width = 1.0     # gives histogram aspect to the bar diagram

fig, ax = plt.subplots()
ax.set_xticks(pos)
ax.set_xticklabels(d1)

plt.bar(pos, d2, width, color='y')
#plt.show()

fig.savefig('d:/task3.png')