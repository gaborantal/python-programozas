import os

import pandas as pd


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

    print(titanic_df.groupby(['sex']).mean())
    print(titanic_df.groupby(['sex', 'pclass']).mean())
    print(titanic_df.groupby(['age']).mean())
    print(titanic_df[titanic_df['age'] < 18].groupby(['sex', 'pclass']).mean())

    # Keressük meg a magyarokat
    titanic_df['home.dest'].fillna("", inplace=True)
    print(titanic_df[titanic_df['home.dest'].str.contains("Hungary")])


if __name__ == '__main__':
    main()
