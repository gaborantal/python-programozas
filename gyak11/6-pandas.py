import os

import pandas as pd
import matplotlib.pyplot as plt


def convert_age(age):
    if age < 18:
        return "child"
    if age < 30:
        return "young adult"
    if age < 60:
        return "adult"
    return "elder"


def main():
    print("version", pd.show_versions())
    titanic_df: pd.DataFrame = pd.read_excel(os.path.join("data", "titanic3.xls"))
    # print(titanic_df)
    print(titanic_df.head())
    print(titanic_df.describe())
    titanic_df.drop(['ticket', 'cabin', 'body'], axis=1)
    # titanic_df.drop(columns=['ticket', 'cabin', 'body'])
    print(titanic_df.head())

    survived = pd.value_counts(titanic_df['survived'])
    print(survived)
    print(titanic_df['survived'].mean())
    print(titanic_df['survived'].median())

    survived.plot.bar()
    plt.show()

    print(titanic_df.groupby(['sex']).mean())
    print(titanic_df.groupby(['sex', 'pclass']).mean())
    print(titanic_df.groupby(['age']).mean())

    titanic_df[titanic_df['age'] < 18]['age'].plot.hist()
    plt.show()

    titanic_df2 = titanic_df.copy()
    titanic_df2['age'].fillna(-1, inplace=True)
    # titanic_df2['age'] = titanic_df2['age'].round(0)
    # print(titanic_df2.groupby('age').count())
    # titanic_df2['age'].value_counts().plot.bar()
    # plt.show()

    titanic_df2['age_class'] = titanic_df2['age'].apply(convert_age)
    titanic_df2['age_class'].value_counts().plot.bar()
    plt.show()

    print(titanic_df[titanic_df['age'] < 18].groupby(['sex', 'pclass']).mean())

    # Keressük meg a magyarokat
    titanic_df['home.dest'].fillna("", inplace=True)
    print(titanic_df[titanic_df['home.dest'].str.contains("Hungary")])


if __name__ == '__main__':
    main()
