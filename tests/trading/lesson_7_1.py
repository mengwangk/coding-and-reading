"""
Sharpe ratio - Risk adjusted return

- daly returns
- cumulative returns
- average returns
- sharpe ratio

k * mean(_daily_rets_ - _daily_rf_) / std(_daily_rets_)

where k = sqrt(252) for daily sampling.


"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from utils import get_data, plot_data, compute_daily_returns


def test_run():
    # Define a date range
    dates = pd.date_range('2017-01-01', '2018-01-10')

    # Choose stock symbols to read
    symbols = ['SPY', 'AAPL', 'DXC']

    # Get stock data
    df = get_data(symbols, dates)
    # plot_data(df)

    # Computer daily returns
    daily_returns = compute_daily_returns(df)

    # Scatterplot SPY vs DXC
    daily_returns.plot(kind='scatter', x='SPY', y='DXC')
    beta_DXC, alpha_DXC = np.polyfit(daily_returns['SPY'], daily_returns['DXC'], 1)
    print('beta_DXC', beta_DXC)
    print('alpha_DXC', alpha_DXC)
    plt.plot(daily_returns['SPY'], beta_DXC * daily_returns['SPY'] + alpha_DXC, '-', color='r')
    plt.show()

    # Scatterplot SPY vs AAPL
    daily_returns.plot(kind='scatter', x='SPY', y='AAPL')
    beta_AAPL, alpha_AAPL = np.polyfit(daily_returns['SPY'], daily_returns['AAPL'], 1)
    print('beta_AAPL', beta_AAPL)
    print('alpha_AAPL', alpha_AAPL)
    plt.plot(daily_returns['SPY'], beta_AAPL * daily_returns['SPY'] + alpha_AAPL, '-', color='r')

    plt.show()

    # Calculate correlation coefficient
    print(daily_returns.corr(method='pearson'))


if __name__ == "__main__":
    test_run()
