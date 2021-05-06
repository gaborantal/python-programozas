import os

import pandas as pd
from sklearn.model_selection import train_test_split  # !!
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

music_df = pd.read_csv(os.path.join("data", "music.csv"))

X = music_df.drop(columns="genre")
y = music_df["genre"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
# model.fit(X_train, y_train)
# score = model.score(X_test, y_test)
# print(score)

scores = cross_val_score(model, X_train, y_train, cv=4)
print(scores)
print(f"Accuracy: {scores.mean()}")
