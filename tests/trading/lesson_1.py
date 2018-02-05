import  pandas as pd
import  matplotlib.pyplot as plt

def get_max_close(symbol):
    """
    Get the max close for the symbol.
    :param symbol: Symbol to search
    :return: Max close p[rice
    """
    df = pd.read_csv("data/{}_history.csv".format(symbol))
    # return df['Close'].max() # compute and return max
    # return df['Close'].min() # compute and return min
    return df['Volume'].mean() # compute and return mean


def test_run():
    """
    Test run.
    :return: None.
    """

    # PRINT OUT DATA
    # df = pd.read_csv("../data/AAPL_history.csv"
    # print(df) # print all
    # print(df.tail(5)) # print last 5
    # print(df.head(5)) # print first 5
    # print(df[10:21]) # between 10 and 20

    # GET MIN, MAX AND MEAN
    # for symbol in ['AAPL']:
    #    print("Max Close")
    #    print(symbol, get_max_close(symbol))

    # PLOT THE DATA
    # df = pd.read_csv("../data/GOOG_HISTORY.csv")
    # print(df['Adj Close'])
    # df['Adj Close'].plot()
    # plt.show() # Show the plot

    # PLOT THE DATA
    # df = pd.read_csv("../data/GOOG_HISTORY.csv")
    # print(df['High'])
    # df['High'].plot()
    # plt.show() # Show the plot

    # PLOT THE DATA
    # df = pd.read_csv("../data/GOOG_HISTORY.csv")
    # print(df['High'])
    # df['High'].plot()
    # plt.xlabel("Day")
    # plt.ylabel(("Volume"))
    # plt.title("Google")
    # plt.show() # Show the plot

    df = pd.read_csv("data/AAPL_HISTORY.csv")
    df[['Close', 'Adj Close']].plot()
    plt.show() # Show the plot



if __name__ == "__main__":
    test_run()

