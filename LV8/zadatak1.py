from tensorflow import keras
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np
import os
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Učitavanje i priprema MNIST podatkovnog skupa
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train_s = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test_s = x_test.reshape(-1, 28, 28, 1) / 255.0

y_train_s = to_categorical(y_train, num_classes=10)
y_test_s = to_categorical(y_test, num_classes=10)

# 2. Struktura konvolucijske neuronske mreže (slika 8.1 pretpostavljena kao tipična CNN)
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# 3. Kompilacija modela
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 4. Callback za TensorBoard
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_cb = callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

# Callback za spremanje najboljeg modela
checkpoint_path = "best_model.h5"
model_checkpoint_cb = callbacks.ModelCheckpoint(
    filepath=checkpoint_path,
    monitor='val_accuracy',
    save_best_only=True,
    mode='max',
    verbose=1
)

# 5. Treniranje modela (10% validacija)
history = model.fit(
    x_train_s, y_train_s,
    epochs=10,
    batch_size=64,
    validation_split=0.1,
    callbacks=[tensorboard_cb, model_checkpoint_cb]
)

# 6. Učitavanje najboljeg modela
best_model = keras.models.load_model("best_model.h5")

# 7. Evaluacija
train_preds = best_model.predict(x_train_s)
test_preds = best_model.predict(x_test_s)

train_acc = accuracy_score(np.argmax(y_train_s, axis=1), np.argmax(train_preds, axis=1))
test_acc = accuracy_score(np.argmax(y_test_s, axis=1), np.argmax(test_preds, axis=1))

print(f"Tocnost na skupu za ucenje: {train_acc:.4f}")
print(f"Tocnost na skupu za testiranje: {test_acc:.4f}")

# 8. Matrica zabune za test skup
conf_matrix = confusion_matrix(np.argmax(y_test_s, axis=1), np.argmax(test_preds, axis=1))
plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predvidjeno")
plt.ylabel("Istinito")
plt.title("Matrica zabune (test skup)")
plt.show()