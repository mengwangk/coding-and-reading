"""
Convex problem - a real-valued function f(x) defined on an interval is called convex
if the line segment between any two points on the graph of the function lies above the graph ..

Parameterized model - f(x) = c0x + c1

Fit polynomial

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def error_poly(C, data):
    """
    Compute errror between given polynomial and observed data

    :param C: numpy.poly1d object or equivalent array representing polynomial coefficients
    :param data: 2D array where each row is a point (x,y)
    :return: Returns error as a single real value

    """

    # Metric: Sum of squared Y-axis differences
    err = np.sum((data[:, 1] - np.polyval(C, data[:, 0])) ** 2)
    return err


def fit_poly(data, error_func, degree=3):
    """
    Fit a polynomial to given data, using supplied error function.

    :param data: 2D array where each row is a point(x,y)
    :param error_func: function that computes the error between a polynomial and observed data
    :param degree:
    :return: Returns polynomial that minimizes the error function.
    """

    # Generate initial guess for polynomial model (all coeffs = 1)
    Cguess = np.poly1d(np.ones(degree + 1, dtype=np.float32))

    print("Cguess", Cguess)

    # Plot initial guess (optional)
    x = np.linspace(-5, 5, 21)
    plt.plot(x, np.polyval(Cguess, x), 'm--', linewidth=2.0, label='Initial guess')

    # Call optimizer to minimize error function
    result = spo.minimize(error_func, Cguess, args=(data,), method='SLSQP', options={'disp': True})
    return np.poly1d(result.x) # convert optimal result into a poly1d object and return


def test_run():
    print("run")


if __name__ == "__main__":
    test_run()
