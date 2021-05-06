import os

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

music_df = pd.read_csv(os.path.join("data", "music.csv"))

# print(music_df)

# Adatok szétszedése input és output halmazokra (mit akarunk prediktálni)
X = music_df.drop(columns="genre")
y = music_df["genre"]

# print(X)
# print(y)

model = DecisionTreeClassifier()
model.fit(X, y)

predictions = model.predict([[21, 1], [20, 2], [60, 1], [60, 2]])
print(predictions)

kor = input("Hány éves emberre vagy kíváncsi?\n")
nem = input("Az ember neme (0 - nő, 1 - férfi)?\n")

predictions = model.predict([[kor, nem]])
