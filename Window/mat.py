import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle



ax = plt.subplot(111)
x = np.linspace(0, 10)
y = np.exp(x)
plt.plot(x, y)
pickle.dump(ax, open('myplot.pickle', 'wb'))