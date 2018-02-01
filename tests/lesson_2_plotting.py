"""Utility functions"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def symbol_to_path(symbol, base_dir="../data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}_history.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'GOOG' not in symbols:  # add GOOG for reference, if absent
        symbols.insert(0, 'GOOG')

    for symbol in symbols:
        # Read and join data for each symbol
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date', parse_dates=True,
                              usecols=['Date', 'Adj Close'],
                              na_values=['nan'])
        # Rename Adj Close to the symbol
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'GOOG':
            df = df.dropna(subset=["GOOG"])
        # df = df.join(df_temp, how='inner')

    return df


def plot_data(df, title="Stock Prices"):
    """Plot stock prices"""
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()  # Show the plot


def plot_selected(df, columns, start_index, end_index):
    """Plot stock prices"""
    plot_data(df.ix[start_index:end_index, columns], title="Selected Data")


def normalized_data(df):
    """Normalize stock prices using the 1st row of the dataframe"""
    return df/df.ix[0,:]


def test_run():
    # Define a date range
    dates = pd.date_range('2017-01-01', '2018-01-10')

    # Choose stock symbols to read
    symbols = ['AAPL', 'DXC', 'IBM']

    # Get stock data
    df = get_data(symbols, dates)

    # Slice by row range (dates) using DateFrame.ix[] selector
    #print(df.ix['2017-01-01':'2017-02-01'])

    # Slice by columns (symbols)
    #print(df['GOOG'])   # a single label selects a single column
    #print(df[['IBM','AAPL']]) # a list of labels select multiple columns

    # Slice by row and column
    # print(df.ix['2017-01-01':'2017-02-01', ['GOOG', 'IBM'] ])

    # Plot
    # plot_data(df)

    # Slice and plot
    # plot_selected(df, ['GOOG', 'IBM'], '2018-01-01', '2018-01-30')

    # print(df)
    # print(df.ix[0,:])
    
    # Plot normalize
    #plot_data(normalized_data(df))


if __name__ == "__main__":
    test_run()
