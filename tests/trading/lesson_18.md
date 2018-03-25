# The Fundamental Law of active portfolio mgmt

## Grinold's Fundamental Law

* Performance
* Skill
* Breadth

$$ performance = skill * \sqrt{breadth} $$

$$ IR = IC \sqrt{BR} $$

IR = information ratio
IC = information coefficient
BR = breadth - trading opportunity

## Thd coin flipping casino

* Flip coin instead of stocks
* the coin is biased - like alpha 0.51 heads
* Uncertainty is like beta

### Betting

Bet N coins

* Win: now have 2xN
* Lose: now have 0

### Casion

* 1000 tables
* 1000 tokens
* game runs in parallel

## Coin flip casino: Reward

* Expected return
* Single bet = 0.51 x  1000 + 0.49 x -10000 = $20
* Multi bet = (0.51 x 1 + 0.49 x -1) * 1000 = $20

## Coin flip casino: Risk 1

* Lose it all
* Single bet - 49%
* Multi bet - 0.49 x 0.49 x 0.49....... = 0.49^1000 = NaN

## Coin flip casino: Risk 2

* Standard deviation of individual bets
* One token per table

stdev(-1, 1, -1, 1, 1.....) = 1.0

* One 1000 token bet, 9999 0 token bets

stdev(1000, 0, 0....) = 31.6
stdev(-1000, 0, 0...) = 31.6

## Coin flip casino - Reward/Risk

* Just like sharpe ratio
* Single bet case - $20 / 31.62 = 0.63
* Multi bet case - $20 / 1 = 20

## Coin flip casino observation

$$ SR_s = 0.63 $$

$$ SR_m = 20 $$

$$ SR_m = SR_s * \sqrt{bets}$$

$$ 20 = 0.63 * \sqrt{1000}$$

$$ performance = skill * \sqrt{breadth}$$

## Coin Flip Casino: Lessons

## Back to real world

* RenTec trades 100k/day
* Warren Buffet holds 120 stocks

Similiar performance - can a single theory relates these 2?

## IR, IC and breadth

* IR - information ratio

$$ r_p(t) = \beta_pr_m(t) + \alpha_p(t)$$
             market       +   skill

Sharpe ratio (reward/risk)

$$ IR = mean(\alpha_p(t)) \div stdev(\alpha_p(t)) $$

IR is like Sharpe of excess return

* IC - information coefficient

correlation of forecasts to returns

* BR - breadth

number of trading opportunities per year

## The fundamental law

$$ IR = IC * \sqrt{BR} $$

$$ performance = skill * \sqrt{breadth} $$

## Simons vs Buffet

* Both have same IR

$$ IC_B * \sqrt{120} = IC_S * \sqrt{x}$$
$$ IC_B * \sqrt{120} = IC_B\div 1000 * \sqrt{x}$$