import matplotlib.pyplot as plt
import numpy as np
import tensorflow.keras as keras

# https://www.tensorflow.org/tutorials/keras/classification

data = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data.load_data()
# X_train, y_train, X_test, y_test

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
print(train_images[10])

plt.imshow(train_images[10], cmap=plt.cm.binary)

plt.show()

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

# epoch == hányszor lásson egy képet
model.fit(train_images, train_labels, epochs=2)

test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print("test accuracy", test_accuracy)

prediction = model.predict(test_images)
print("prediction", prediction[0])
print("argmax", np.argmax(prediction[0]))
print(class_names[np.argmax(prediction[0])])

for i in range(5):
    plt.grid(False)
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    plt.xlabel(f"Actual: {class_names[test_labels[i]]}")
    plt.title(f"Prediction: {class_names[np.argmax(prediction[i])]}")
    # plt.show()

for i in range(len(prediction)):
    if test_labels[i] != np.argmax(prediction[i]):
        plt.grid(False)
        plt.imshow(test_images[i], cmap=plt.cm.binary)
        plt.xlabel(f"Actual: {class_names[test_labels[i]]}")
        plt.title(f"Prediction: {class_names[np.argmax(prediction[i])]}")
        plt.show()
