import os

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split  # !!
from sklearn.tree import DecisionTreeClassifier

music_df = pd.read_csv(os.path.join("data", "music.csv"))

X = music_df.drop(columns="genre")
y = music_df["genre"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Mentés
joblib.dump(model, "model.joblib")

del model
model2 = joblib.load("model.joblib")
predictions = model2.predict(X_test)
# print(predictions)

resulting_score = accuracy_score(y_test, predictions)
print("A model pontossága", resulting_score)
