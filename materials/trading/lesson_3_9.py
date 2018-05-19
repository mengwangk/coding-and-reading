"""Accessing array elements"""

import numpy as np


def test_run():
    a = np.array([(20, 25, 10, 23, 26), (0, 2, 50, 20, 0)])
    print(a)

    # Calculate the mean
    mean = a.mean()
    print(mean)

    # masking
    print(a[a < mean])

    # Replace with mean if < mean
    a[a < mean] = mean
    print(a)


if __name__ == "__main__":
    test_run()
