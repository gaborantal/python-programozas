import matplotlib.pyplot as plt
import numpy as np
import tensorflow.keras as keras

# https://www.tensorflow.org/tutorials/keras/classification

data = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# 0-1 közé kerüljön (numpy tömb)
train_images = train_images / 255.0
test_images = test_images / 255.0
# print(train_images[10])

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(units=128, activation="relu"),  # teljesen összekötött
    keras.layers.Dense(units=10, activation="softmax")  # összegük 1
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(train_images, train_labels, epochs=2)

model.save("fashion_mnist_model")

del model

model2 = keras.models.load_model("fashion_mnist_model")
model2.summary()

prediction = model2.predict(test_images)

for i in range(5):
    print(f"Actual: {class_names[test_labels[i]]}, Prediction: {class_names[np.argmax(prediction[i])]}")

