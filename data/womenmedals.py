import matplotlib.pyplot as plt

#generate a pie chart with our Olympic data

values = [239, 242]
colors = ['#f74a41', '#4c61fa']
labels = ["Canadian Women", "American Women"]

explode = (0, 0.1)


plt.pie(values, labels=labels, colors=colors, explode=explode, autopct='%.1f%%', shadow = True)

plt.title("United States and Canada's women's medal totals compared", fontsize = 24, fontweight = 'bold')

plt.show()