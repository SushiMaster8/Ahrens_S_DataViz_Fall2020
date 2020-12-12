import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
medals = np.array([9, 12, 20, 13, 0, 0, 20, 17, 20, 21, 7, 20, 1, 3, 2, 4, 6, 37, 40, 49, 75, 68, 91, 90])
medals_us = np.array([13, 14, 45, 16, 0, 0, 16, 30, 26, 27, 8, 7, 25, 11, 30, 9, 7, 14, 21, 34, 84, 53, 98, 65])
years = np.array([1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014])

ax.set_xlabel('Years', fontweight='bold')
ax.set_ylabel('Medal Totals', fontweight='bold')

plt.xticks(np.arange(1924,2014, 4))

plt.plot(years, medals, linestyle = 'solid', marker = 'o', color = 'r', mec = 'r', mfc = 'r')
plt.plot(years, medals_us, linestyle = 'solid', marker = 'o', color = 'b', mec = 'b', mfc = 'b')

#title
fig.suptitle("Winter Olympics medal history: Canada (red) vs United States (blue)", fontsize = 18, fontweight= 'bold')

plt.show()