import  pandas as pd

def test_run():

    # define date ranges
    start_date = '2018-01-01'
    end_date = '2018-01-10'
    dates = pd.date_range(start_date, end_date)

    #print(dates)
    #print(dates[0])

    # Create empty data frame
    df1 = pd.DataFrame(index=dates)
    print(df1)

    # Read AAPL data into temporary dataframe
    dfGOOG = pd.read_csv('../data/GOOG_history.csv', index_col='Date', parse_dates=True, usecols=['Date','Adj Close'],
                         na_values=['nan'])
    #print(dfGOOG)

    # Rename Adj Close to GOOG
    dfGOOG = dfGOOG.rename(columns={'Adj Close': 'GOOG'})

    # Join the 2 dataframes using DataFrame.join() and drop NaN
    df1 = df1.join(dfGOOG, how='inner')

    # Drop NaN
    # df1 = df1.dropna()
    # print(df1)

    # Read in more stocks
    symbols = ['AAPL', 'DXC', 'IBM']
    for symbol in symbols:
        df_temp = pd.read_csv('../data/{}_history.csv'.format(symbol), index_col='Date', parse_dates=True, usecols=['Date','Adj Close'],
                         na_values=['nan'])
        # Rename Adj Close to the symbol
        df_temp = df_temp.rename(columns={'Adj Close': symbol})

        df1 = df1.join(df_temp)     #use default left join

    print(df1)



if __name__ == "__main__":
    test_run()