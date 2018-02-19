"""Plot a histogram."""

import pandas as pd
import matplotlib.pyplot as plt

from util import get_data

def test_run():
    # Define a date range
    dates = pd.date_range('2017-01-01', '2018-01-10')

    # Choose stock symbols to read
    symbols = ['AAPL', 'DXC', 'IBM']

    # Get stock data
    df = get_data(symbols, dates)

    print(df)


if __name__ == "__main__":
    test_run()
