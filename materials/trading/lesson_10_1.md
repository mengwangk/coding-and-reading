
ETF - Exchanged traded fund
- Buy/sell like stocks
- Baskets of stocks
- Transparent
- Liquid


Mutual fund
- Buy/sell at end of day
- Quarterly disclouse
- Less transparent

Hedge fund
- Buy/sell by agreement
- No disclosure
- Not transparent

Incentives for fund managers
----------------------------
Assets under mgmt - total amount of money managed by the fund

ETF - expense ratio
Mutual fund - expense ratio - higher ratio
Hedge fund - two and twenty
  -> 2 percent of AUM and 20% of the profits


Hedge fund goals and metrics

Goals
- Beat a benchmark - SP500
- Absolute return - Long/short

Metrics
- Cumulative return - (val[-1] / val[0]) -1
- Volatility - daily_rturns.std()
- Risk/Reward - Sharpe Ratio (risk adjusted return)

k * mean(_daily_rets_ - _daily_rf_) / std(_daily_rets_)

where k = sqrt(252) for daily sampling.

### Trading algorithm
- OHLCV
- Live Portfolio
- Orders
- Target portfolio
    - Portfolio optimizer
    - N-day forecast (machine learning)
        - Information feed
        - OHLCV
    - Current portfolio
    - Historical price data - OHLCV
- Market

