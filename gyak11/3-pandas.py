import os

import numpy as np
import pandas as pd


def main():

    charts_df: pd.DataFrame = pd.read_csv(os.path.join("data", "charts.csv"))

    print(charts_df.head())
    print(charts_df.describe())
    print(charts_df.info())
    print(charts_df.sort_values(by="weeks-on-board").tail(1))


if __name__ == '__main__':
    main()
