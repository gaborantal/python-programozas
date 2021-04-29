import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 10])  # ezek lehetnének akár sima python listák is, ugyan úgy működik
y = np.array([0, 40])
plt.plot(x, y)  # a pontok megjelenítése
# egy pont az (x[i], y[i]) koordináta-párból jön létre,
# így jelen esetben egy (0,0) és egy (10,40) pontból áll az egyenes
plt.show()  # a grafikon megjelenítse
# ---------------------------------------------
plt.title("Kiscica")
plt.plot(x, y, 'x--r')
plt.show()
# ---------------------------------------------

plt.plot(x, y)
plt.title("Title")  # A diagram címe
plt.xlabel("x")  # Tengelyfeliratok
plt.ylabel("y")
plt.show()
# ---------------------------------------------

x = np.array([0, 10, 20, 30])
y = np.array([0, 40, 70, 10])
plt.subplot(1, 2, 1)
plt.plot(x, y, 'r')

x = np.array([0, 1, 2, 3])
y = np.array([0, 10, -20, 30])
plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.show()
# ---------------------------------------------

x = np.array([11, 1, 0, 3, 13, 13, 2, 5, 10, 4])
y = np.array([23, 25, 37, 21, 20, 23, 22, 33, 32, 28])
plt.scatter(x, y)
plt.show()

# ---------------------------------------------
x = np.array([14, 6, 10, 2, 0, 11, 10, 12, 0, 12])
y = np.array([28, 35, 7, 21, 12, 0, 17, 27, 18, 27])
colors = np.array(["red", "green", "blue", "yellow", "pink", "black", "orange", "purple", "beige", "brown"])
plt.scatter(x, y, color=colors)
plt.show()

# ---------------------------------------------
x = np.array(["A", "B", "C", "D", "E"])  # Címkék
y = np.array([3, 2, 4, 5, 1])  # Oszlopok értékei

plt.bar(x, y, color="red")  # A color paraméteren keresztül ugyan úgy színezhető
plt.show()
# ---------------------------------------------

x = np.random.normal(200, 20, 300)  # 300 normál eloszlású szám generálása 200-as átlaggal, 10-es szórással
plt.hist(x)
plt.show()
# ---------------------------------------------

x = np.array([39, 21, 13, 27])
labels = ["Kutya", "Cica", "T-Rex", "lorem ipsum"]
colors = ["red", "blue", "green", "orange"]
plt.pie(x, labels=labels, colors=colors)
plt.show()
# ---------------------------------------------

x = np.array([39, 21, 13, 27])
labels = ["Kutya", "Cica", "T-Rex", "lorem ipsum"]
colors = ["red", "blue", "green", "orange"]
explode = [0, 0.2, 0, 0]  # a 0-nál nagyobb értékkel rendelkező körcikkek lesznek kiemelve
# jelen esetben mivel ez a második indexű, így a
# 21 értékű, "Cica" felírat kék körcikk lesz ez

plt.pie(x, labels=labels, colors=colors, explode=explode)
plt.show()
# ---------------------------------------------
