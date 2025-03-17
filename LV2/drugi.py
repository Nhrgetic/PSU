import numpy as np
import matplotlib.pyplot as plt

# Učitavanje podataka iz mtcars.csv
data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), 
                  delimiter=",", skiprows=1)

# Izdvajanje pojedinih varijabli
mpg = data[:, 0]  # Potrošnja goriva
hp = data[:, 2]   # Konjske snage
wt = data[:, 4]   # Težina automobila
cyl = data[:, 1]  # Broj cilindara

# (b) Scatter plot: mpg vs hp (veličina točkica u skladu s težinom)
plt.figure(figsize=(8,6))
plt.scatter(hp, mpg, s=wt*50, alpha=0.6, edgecolors="k")
plt.xlabel("Konjske snage (hp)")
plt.ylabel("Potrošnja goriva (mpg)")
plt.title("Ovisnost potrošnje goriva o konjskim snagama")
plt.grid()
plt.show()

# (d) Izračun minimalne, maksimalne i srednje vrijednosti mpg
mpg_min = np.min(mpg)
mpg_max = np.max(mpg)
mpg_mean = np.mean(mpg)
print(f"Min MPG: {mpg_min}, Max MPG: {mpg_max}, Mean MPG: {mpg_mean:.2f}")

# (e) Izdvajanje podataka samo za automobile sa 6 cilindara
mpg_6cyl = mpg[cyl == 6]
mpg_6cyl_min = np.min(mpg_6cyl)
mpg_6cyl_max = np.max(mpg_6cyl)
mpg_6cyl_mean = np.mean(mpg_6cyl)
print(f"6-cyl Min MPG: {mpg_6cyl_min}, Max MPG: {mpg_6cyl_max}, Mean MPG: {mpg_6cyl_mean:.2f}")
