# Regression

* Numerical model

## Parametric regression

* Linear  y = mx + b
* Polynomial y = ax^2 + bx + c
* Space efficient
* Training slow, query is fast

## K nearest neighbor (KNN)

* k = 3, find nearest 3 historical data points
* Hard to apply for huge datasets, new parameters can be added fast
* Training fast, query is slow
* Suitable for complex pattern

## Kernel regression

* weight the contributions for each of the nearest the data points

## Training and testing

## Learning APIs

* For linear regression

learner = 

## Example for linear regression

```python

class LinRegLearner::
    def __iniit__():
        pass

    def train(x,y):
        self.m, self.b = favorite_linreg(x,y)
    
    def query(x):
        y = self.m * x + self.b
        return y
```