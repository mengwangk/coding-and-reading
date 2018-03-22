# Technical Analysis

## Characteristics

What it is

* Histroical price and volume only
* Compute statistics called indicators
* Indicators are heuristics

Why it might work

* there is information in price
* heuristics works

## When is technical analysis valuable?

* Individual indicators weak
* Combinations stronger
* Look for contrasts (stocks vs market)
* Shorter time period

Trading horizon
milliseconds -> days -> years

decision speed
decision complexity

## Momentum

* positive and negative momentum
* steepness - strength of the momentum

Visual or quantitative presentations

momentum[t] = price[t] / price[t-1]

n - day 5, 10

## SMA

n - day window

* strong signal when it crosses with the price
* lagging indicator
* use together with momentum indicator
* proxy for value
* arbitrage opportunity

$$ (price[t]\div price[t-n: t].mean) - 1 $$

## Bollinger Bands

* SMA + 2 * deviation
* SMA - 2 * deviation
* Look for cross outside to inside

$$ BB[t] =  (price[t] - SMA[t]) \div 2 * std[t] $$

## Normalization

* SMA  -0.5 to 0.5
* momentum  -0.5 to 0.5
* BB -.10 to 1.0
* PE ratio 1 to 300

$$ normed = (value - mean) \div values.std() $$

## Wrap up

* heuristics
* Tucker's approach
* don't start trading yet