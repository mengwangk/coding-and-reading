# Reinforcement learning

## The RL problem

* Robot - sense, think, act
* State -> pi (S) -> Action -> Transition -> State->....
* Reward for the action taking the state
* Algorithm to figure out pi

## Trading as an RL problem

* Buy - action
* Sell - action
* Holding Long - state
* Bollinger Value - state
* Return from trade - reward
* daily return - state, return

## Mapping trade as RL

* State - Features, Holding
* Action - Buy, Sell, Do Nothing

## Markov decision problems

* Set of states S
* Set of actions A
* Transition function T[s,a,s']
* Reward function R[s,a]
* Find policy

$$ \pi^*(s) $$

that will maximize reward

* Policy iteration, value iteration

## Unknown transitions and rewards

* Work with data to build a policy
* <s1 a1 s1' r1>  - Experience tuple
* <s2=s1' s2' r2>.....

* Model based RL 
    * build model of T[s,a,s']
    * build model of R[s,a]
    * value/policy iteration
* Model-free
    * Q-Learning


## What to optimize

* infinite horizon

$$ \sum_{i=1}^\infty r_i	$$

* finite horizon

$$ \sum_{i=1}^n r_i	$$

* discounted reward

$$ \sum_{i=1}^\infty \gamma^{i-1} r_i	$$ 

0 < gamma <= 1.0 

* Used in Q-Learning


## Which approach gets $1M

* 6 RL algos solve MDPs
* S, A, T[s,a,s'], R[s,a]
* Find pi(s) -> a
* Map trading to RL
