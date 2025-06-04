import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.transform import resize
from skimage import color
from tensorflow.keras import models
import numpy as np

filename = 'test.png'

# Ucitaj sliku
img_original = mpimg.imread('C:\\Users\\Nino\\Desktop\\LV8\\test.png')  # Zamijeni 'test.png' s putanjom do svoje slike

# Ako slika ima 4 kanala (RGBA), uzmi samo prva 3 (RGB)
if img_original.shape[-1] == 4:
    img_original = img_original[:, :, :3]

img = color.rgb2gray(img_original)
img = resize(img, (28, 28))


# Prikazi sliku
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.axis('off')  
plt.show()

# Pripremi sliku - ulaz u mrezu
img = img.reshape(1, 28, 28, 1)
img = img.astype('float32')

# TODO: ucitaj izgradenu mrezu
model = models.load_model('model.h5')


# TODO: napravi predikciju za ucitanu sliku pomocu mreze
predictions = model.predict(img)
predicted_digit = np.argmax(predictions)


# TODO: ispis rezultat u terminal
print(f'Predikcija modela: {predicted_digit}')

#Ako je znamenka nagnuta, pomaknuta ili okružena šumom, model je teže prepozna 
#točnost opada, a model najbolje radi kad je znamenka ravna i na sredini slike