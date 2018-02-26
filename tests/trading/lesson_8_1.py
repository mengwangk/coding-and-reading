""" Optimizer
- Find min values of functions
- Build parameterized models based on data
- Refine allocations to stock in portfolio

How to use
1. Provide a function to minimize
2. Provide an initial guess
3. Call the optimizer

"""

""" 
Minimize an objective function, using SciPy. 
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def f(X):
    """Given a salar X, return some value (a real number)."""
    Y = (X - 1.5) **2 + 0.5
    print("X = {}, Y = {}".format(X, Y))   # for tracing
    return Y


def test_run():

if __name__ == "__main__":
    test_run()
