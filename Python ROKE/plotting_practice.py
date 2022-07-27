import matplotlib.pyplot as plt
import numpy as np

# LINE GRAPH ....................
years = [1960, 1970, 1980, 1990, 2000, 2010]
gdpMalaysia = [1.92, 3.86, 24.49, 44.02, 93.79, 255.02]
gdpSingapore = [0.7, 1.92, 11.89, 36.15, 95.83, 236.42]
plt.plot(years, gdpMalaysia, color='blue', marker='x', linestyle='solid')
plt.plot(years, gdpSingapore, color='green', marker='x', linestyle='solid')
plt.title("Malaysia & Singapore GDP")
plt.ylabel("$billions")
plt.xlabel("Year")
plt.show()

#BAR
countries = ["China", "India", "USA", "Indonesia","Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico"]
populations = [1401.5, 1359.3, 329.4, 265.0, 208.2, 211.2, 188.5, 168.2, 146.9, 126.6]

plt.bar(countries, populations, color='blue')
plt.show()

#SCATTER
widgets = [5, 7, 9, 13, 86, 103]
gromits = [23, 38, 77, 102, 165, 198]
labels = ["alice", "bob", "jane", "sue", "simon", "steve"]

plt.scatter(widgets, gromits)
plt.xlabel("Widgets")
plt.ylabel("Gromits")
plt.title("Widgets and Gromits")
for label, widget, gromit in zip(labels, widgets, gromits):
    plt.annotate(label, xy=(widget, gromit), xytext=(5, -5), textcoords="offset points")

plt.show()