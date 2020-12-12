import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
x1 = np.array(["USA first places", "USA top fives"])
x2 = np.array(["Canada first places", "Canada top fives"])
y1 = np.array([4, 14])
y2 = np.array([3, 15])

plt.bar(x1, y1, color = 'blue', width = 0.6)
plt.bar(x2, y2, color = 'red', width = 0.6)

ax.yaxis.set_minor_locator(plt.MultipleLocator(1))

plt.title("United States and Canada's medal winning totals compared", fontsize = 18, fontweight='bold')

plt.show()