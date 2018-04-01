# Q-Learning

## Overview

* model free approach.
* build a table of utility values.
* guaranteed to build a optimal policy.

## What is Q

* Named after Q function.

$$ Q[s,a] = immediate reward + discounted reward  $$

s = state
a = action

* How to use Q?

In state s, find which action a is the best

$$ \pi(s) = argmax_a(Q[s,a])$$

Optimal policy

$$ \pi^*(s) = Q^*[s,a]$$

## Learning Procedure

### Big picture

* select training data
* iterate over time <s,a,s',r>
* test policy pi
* repeat until converge

$$ 

s   \pi(s) -> a ->
s', r

<s, a, s',r>
$$

Details

* set start time, init Q[]
* compute s
* select a
* observe r, s'
* update Q

## Update Rule

* How to improve the Q table


$$ Q'[s,a]  = (1-\alpha) Q[s,a] + \alpha * improved estimate $$

* alpha = learning rate 0 to 1.0, usually use 0.2
* gamma = discount rate 0 to 1.0

$$ Q'[s,a]  = (1-\alpha) Q[s,a] + \alpha (r + \gamma * Q[s', argmax_{a'}(Q[s',a'])])$$


The formula for computing Q for any state-action pair <s, a>, given an experience tuple <s, a, s', r>, is:
Q'[s, a] = (1 - α) · Q[s, a] + α · (r + γ · Q[s', argmaxa'(Q[s', a'])])

Here:

r = R[s, a] is the immediate reward for taking action a in state s,
γ ∈ [0, 1] (gamma) is the discount factor used to progressively reduce the value of future rewards,
s' is the resulting next state,
argmaxa'(Q[s', a']) is the action that maximizes the Q-value among all possible actions a' from s', and,
α ∈ [0, 1] (alpha) is the learning rate used to vary the weight given to new experiences compared with past Q-values.

## Two finer points

* success depends on exploration (state and c)
* choose random action with probability c

## The Trading Problem: Actions

### Action

* Buy
* Sell
* Nothing

* Usually nothing and occassional buy and sell

## The Trading Problem: Rewards

Which results in faster convergence?

* r = daily return - YES (immediate rewards)
* r = 0 until exit, then cumulative ret - NO  (delayed rewards)

## The Trading Problem: State

* adjusted closed - NO
* SMA - NO
* adjusted close/SMA - YES
* Bollinger value - YES
* PE ratio - YES
* Holding stock - YES
* return since entry - YES

## Creating the State

* state is an integer
* discretize each factor
* combine

X1  25.6     discretize   0
X2  0.3      discretize   5
X3  2.0      discretize   9
X4  -5.1     discretize   2

## Discretizing

stepsize = size(data) / steps
data.sort()
for i in range(0, steps)
    threshold[i] = data[(i+1) * stepsize]

## Q-Learning Recap

* Build a model
    * define states, actions, rewards
    * choose in sample training period
    * iterate: Q-table update
    * backtest
* Testing a model
    * backtest on later data

## Summary

Advantages
    The main advantage of a model-free approach like Q-Learning over model-based techniques is that it can easily be applied to domains where all states and/or transitions are not fully defined.

    As a result, we do not need additional data structures to store transitions T(s, a, s') or rewards R(s, a).

    Also, the Q-value for any state-action pair takes into account future rewards. Thus, it encodes both the best possible value of a state (maxa Q(s, a)) as well as the best policy in terms of the action that should be taken (argmaxa Q(s, a)).

Issues
    The biggest challenge is that the reward (e.g. for buying a stock) often comes in the future - representing that properly requires look-ahead and careful weighting.

    Another problem is that taking random actions (such as trades) just to learn a good strategy is not really feasible (you'll end up losing a lot of money!).

    In the next lesson, we will discuss an algorithm that tries to address this second problem by simulating the effect of actions based on historical data.

## Resources

* CS7641 Machine Learning, taught by Charles Isbell and Michael Littman

    * Watch for free on Udacity (mini-course 3, lessons RL 1 - 4)
    * Watch for free on YouTube
    * Or take the course as part of the OMSCS program!

* RL course by David Silver (videos, slides)
* A Painless Q-Learning Tutorial