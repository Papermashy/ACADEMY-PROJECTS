import matplotlib.pyplot as plt
import numpy as np


x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

plt.scatter(x, y1, color='blue', marker='x')
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y1, 1))(np.unique(x)))
plt.xlabel("X1")
plt.ylabel("Y1")
plt.title("X1 & Y1")
plt.show()

plt.scatter(x, y2, color='green', marker='x')
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y1, 1))(np.unique(x)))
plt.xlabel("X1")
plt.ylabel("Y2")
plt.title("X1 & Y2")
plt.show()

plt.scatter(x, y3, color='pink', marker='x')
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y1, 1))(np.unique(x)))
plt.xlabel("X1")
plt.ylabel("Y3")
plt.title("X1 & Y3")
plt.show()

plt.scatter(x4, y4, color='red', marker='x')
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y1, 1))(np.unique(x)))
plt.xlabel("X4")
plt.ylabel("Y4")
plt.title("X4 & Y4")
plt.show()