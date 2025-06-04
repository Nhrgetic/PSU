import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix


# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# TODO: prikazi nekoliko slika iz train skupa

for i in range(5):
    plt.imshow(x_train[i], cmap='gray')
    plt.title(f"Broj: {y_train[i]}")
    plt.show()

# Skaliranje vrijednosti piksela na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# Slike 28x28 piksela se predstavljaju vektorom od 784 elementa
x_train_s = x_train_s.reshape(60000, 784)
x_test_s = x_test_s.reshape(10000, 784)

# Kodiraj labele (0, 1, ... 9) one hot encoding-om
y_train_s = keras.utils.to_categorical(y_train, 10)
y_test_s = keras.utils.to_categorical(y_test, 10)


# TODO: kreiraj mrezu pomocu keras.Sequential(); prikazi njenu strukturu pomocu .summary()

model = keras.Sequential(
    [
        keras.Input(shape=(784,)),
        layers.Dense(128, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax'),
    ]
)
model.summary()

# TODO: definiraj karakteristike procesa ucenja pomocu .compile()

model.compile(optimizer=keras.optimizers.Adam(),
              loss=keras.losses.CategoricalCrossentropy(),
               metrics=[keras.metrics.Accuracy()])

# TODO: provedi treniranje mreze pomocu .fit()

hist = model.fit(x_train_s, y_train_s, epochs=10, batch_size=500, validation_split=0.2)

# TODO: Izracunajte tocnost mreze na skupu podataka za ucenje i skupu podataka za testiranje

train_loss, train_acc = model.evaluate(x_train_s, y_train_s)
test_loss, test_acc = model.evaluate(x_test_s, y_test_s)

print(f"Tocnost train-a: {train_acc:.2f}")
print(f"Tocnost testa: {test_acc:.2f}")


# TODO: Prikazite matricu zabune na skupu podataka za testiranje

predvidjanje_y = model.predict(x_test_s)
predvidjanje_y_klasa = np.argmax(predvidjanje_y, axis=1)
y_istinito = np.argmax(y_test_s, axis=1)
matrica_zabune = confusion_matrix(y_istinito, predvidjanje_y_klasa)
print("Matrica zabune:")
print(matrica_zabune)
# TODO: Prikazi nekoliko primjera iz testnog skupa podataka koje je izgrađena mreza pogresno klasificirala

pogreske = np.where(predvidjanje_y_klasa != y_istinito)[0]

for i in pogreske[:5]:
    tocno = y_istinito[i]
    pred_klasa = predvidjanje_y_klasa[i]
    
    plt.imshow(x_test[i], cmap='gray')
    plt.title(f"Tocno: {tocno}, Predvidjeno: {pred_klasa}")
    plt.axis('off')
    plt.show()


    #Ukupna točnost iznosi otprilike 97–98%, što je i očekivano za ovu arhitekturu i MNIST