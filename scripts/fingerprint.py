#/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

data = np.random.random([2, 50])

colors = np.array([[1, 0, 0], [0, 1, 0]])

plt.xticks([0, 1], ['perfect', 'judged'])
plt.eventplot(data, orientation='vertical', colors=colors)
plt.show()
