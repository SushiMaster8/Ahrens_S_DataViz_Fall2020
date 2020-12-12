import matplotlib.pyplot as plt

#generate a pie chart with our Olympic data

values = [386, 411]
colors = ['red', 'blue']
labels = ["Canadian Men", "American Men"]

explode = (0, 0.1)


plt.pie(values, labels=labels, colors=colors, explode=explode, autopct='%.1f%%', shadow = True)

plt.title("United States and Canada's men's medal totals compared", fontsize = 24, fontweight = 'bold')

plt.show()
