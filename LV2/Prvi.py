import numpy as np
import matplotlib.pyplot as plt

#Koordinate

x = np.array([1, 2, 3, 3, 1])
y = np.array([1, 2, 2, 1, 1])

#Crtanje

plt.plot(x, y, color='b', marker = 'o')
plt.title("Primjer")
plt.xlabel("x-os")
plt.ylabel("y-os")

#Ispis/crtanje

plt.grid(True)
plt.show()
