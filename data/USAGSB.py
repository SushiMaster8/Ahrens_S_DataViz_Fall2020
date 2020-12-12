import matplotlib.pyplot as plt

values = [167, 319, 167]
colors = ['#fcbf1e', '#a0a09e', '#a2440b']
labels = ["Gold Medals", "Silver Medals", "Bronze Medals"]

#explode = (0, 0.1, 0.1)

plt.pie(values, labels=labels, colors=colors, autopct='%.1f%%')

plt.title("America's Winter Olympic medal totals divided\n between gold, silver, and bronze", fontsize = 24)

plt.show()