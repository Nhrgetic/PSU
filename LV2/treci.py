import numpy as np
import matplotlib.pyplot as plt

#Učitavanje slike
tiger = plt.imread("tiger.png")

#Pretvaranje u grayscale ako je slika u boji
if len(tiger.shape) == 3:
    tiger = tiger[:, :, 0].copy()

#Povećanje svjetline
bright_tiger = np.clip(tiger + 50, 0, 255)  #50 na svaku vrijednost piksela

#Rotacija 90 stupnjeva
rotated_tiger = np.rot90(tiger, k=-1)

# Zrcaljenje slike
mirrored_tiger = np.fliplr(tiger)

#Smanjenje rezolucije slike 10 puta
factor = 10
small_tiger = tiger[::factor, ::factor]

#Prikaz druge četvrtine slike po širini
masked_tiger = np.zeros_like(tiger)
width = tiger.shape[1]
masked_tiger[:, width // 4: width // 2] = tiger[:, width // 4: width // 2]

#Rezultat
titles = ["Original", "Povećana svjetlina", "Rotacija 90°", "Zrcaljena slika", "Smanjena rezolucija", "Druga četvrtina"]
images = [tiger, bright_tiger, rotated_tiger, mirrored_tiger, small_tiger, masked_tiger]

fig, axes = plt.subplots(2, 3, figsize=(12, 8))

for ax, img, title in zip(axes.ravel(), images, titles):
    ax.imshow(img, cmap="gray")
    ax.set_title(title)
    

plt.tight_layout()
plt.show()
