# Dyna

## Overview

* Q-Learning is expensive.
* Building models of Transition Matrix or Reward, hallucuinate to update Q table.

## Dyna-Q Big Picture

* Blend of model based and model free model
* Q-Learn
    * init Q table
    * observe s
    * execute a, observe s', r
    * update Q with <s,a,s',r>
    * repeat...
* Dyna-Q - 3 new components
    * Learn model (T R)
    * Hallucinate experience
    * Update Q

* Learn model
    * T'[s,a,s'] update
    * R'[s,a] update
* Hallucinate
    * s = random
    * a = random
    * s' = infer from T[]
    * r = R[s,a]
* Update Q
    * with <s,a,s',r>

## Learning T

* T[s,a,s']   probability s,a -> s'

- init T_c[] = 0.00001
- while executing, observe s,a,s'
- increment T_c[s,a,s']


## How to Evaluate T

Probability of s'

$$ T[s,a,s'] = \frac {T_c[s,a,s']} {\sum_iT[s,a,i]}$$

count of number of times in s' divided by total number of times in [s,a]

## Learning R

* R[s,a] expected reward for s,a - model
* r immediate reward - experience

$$ R'[s,a] = (1-\alpha) R[s,a] + \alpha * r $$

alpha - learning rate, e.g. 0.2

## Dyna Q Recap

## Summary 

The Dyna architecture consists of a combination of:

* direct reinforcement learning from real experience tuples gathered by acting in an environment,
* updating an internal model of the environment, and,
* using the model to simulate experiences.

Dyna learning architecture

Sutton and Barto. Reinforcement Learning: An Introduction. MIT Press, Cambridge, MA, 1998. [web]

## Resources

http://www.incompleteideas.net/
http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html


