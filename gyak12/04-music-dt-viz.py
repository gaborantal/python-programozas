import os

import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split  # !!
from sklearn.tree import DecisionTreeClassifier

music_df = pd.read_csv(os.path.join("data", "music.csv"))

X = music_df.drop(columns="genre")
y = music_df["genre"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

tree.export_graphviz(model, out_file="alma.dot",
                     feature_names=["Kor", "Nem"],
                     class_names=sorted(y.unique()),
                     label="all",
                     rounded=True,
                     filled=True)
