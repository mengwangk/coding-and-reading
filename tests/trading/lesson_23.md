# Ensemble learners, bagging and boosting

## Ensemble learners

* Assemble several algorithms/models
* KNN, LinReg, Decision Tree, SVM... -> take the mean, etc...
* Why
    * lower error
    * less overfitting
    * tastes great

## How to bu8ld an ensemble

* train several parameterized polynomials of differing degree
* train several KNN models using different subsets of data

## Boostrapping aggregating bagging

* Create a number of subsets of data
* Train -> D1, D2, D3...Dm
* n - number of instances
* n'- number in a bag
* m - number of bags
* n' < n, around 60%
* use each bag to train and get the model
* from the models -> mean -> Y

## Overfitting

* Single 1 NN trained on all data will be overfitting

## Bagging sample

## Boosting: Ada Boost

* Variation of bagging.

* D1->model->D2 use some of not good samples->.....until N

## Overfitting

* Ada boost - really to match all data

## Summary

* Boosting and bagging
    * wrappers for existing methods
    * reduces error
    * reduces overfitage
