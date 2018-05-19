"""Accessing array elements"""

import numpy as np


def test_run():
    a = np.random.rand(5, 4)
    print("Array:\n", a)

    # Assigning a value to a particular location
    a[0, 0] = 1
    print("\nModfied array\n", a)

    # Assigning a single value to an entire row
    a[0, :] = 2
    print("\nModfied array\n", a)

    # Assigning a list to a column in an array
    a[:, 3] = [1, 2, 3, 4, 5]
    print("\nModfied array\n", a)

    # Access using list of indices
    a = np.random.rand(5)

    # accessing using list of indices
    indices = np.array([1,1,2,3])

    print(a[indices])


if __name__ == "__main__":
    test_run()
