# Asessing a learning algorithm

## Closer look at KNN solutions

* N increase, less likely to overfit

## What happens as D varies

* D increases, more likely to overfit

$$ y = m_1x_1 + m_2x^2_2 + m_3x^3_3 + b $$

## Metric 1 RMS Error

Root mean square error

$$ RMSE = \sqrt{ \dfrac {\sum(y_{test} - y_{predict})^2} {N}} $$

## In Sample vs out of sample

Use the test data to calculate RMSE

## Which is worse?

Out of sample error to be larger

## Cross validation

* train - 60%, test - 40%
* slice data in different chunks
* train, train, train, train, test, and swap them and train

## Roll forward cross validation

* Training data is always before testing data

## Metric 2 - correlation

$$ X_{test} to Y_{test} and Y_{predict} $$

* use np.corrcoef, +1 strong corrleated, -1 inversely correlated, 0 no correlation.
* RMS error increases, correlation decreases, or we can't be sure either way

## Overfitting

* In sample error decreasing
* Out of sample error increasing

## KNN overfitting

## A few other considerations

### LinReg

* space for savig model
* computer time to query

### KNN

* Compute time to training
* ease to add new data