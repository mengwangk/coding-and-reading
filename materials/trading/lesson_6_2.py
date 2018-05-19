"""Plot a histogram."""

import pandas as pd
import matplotlib.pyplot as plt

from utils import get_data, plot_data, compute_daily_returns


def test_run():
    # Define a date range
    dates = pd.date_range('2017-01-01', '2018-01-10')

    # Choose stock symbols to read
    symbols = ['SPY', 'AAPL']

    # Get stock data
    df = get_data(symbols, dates)
    # plot_data(df)

    # Computer daily returns
    daily_returns = compute_daily_returns(df)
    # plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

    # Plot a histogram
    daily_returns['AAPL'].hist(bins=20, label='AAPL')
    daily_returns['SPY'].hist(bins=20, label='SPY')
    plt.legend(loc='upper right')
    plt.show()



if __name__ == "__main__":
    test_run()
