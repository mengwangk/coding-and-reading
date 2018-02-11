"""Create NumPy arrays."""

import numpy as np


def test_run():
    # List to 1D array
    print(np.array([2,3,4]))

    # List of tuples to 2D array
    print(np.array([(2,3,4), (5,6,7)]))

    # Empty array
    print(np.empty(5))        # 1 dimension
    print(np.empty((5,4)))    # 2 dimensions
    print(np.empty((5,4,3)))  # 3 dimensions

    # Array of 1s
    print(np.ones((5, 4)))
    print(np.ones((5, 4), dtype=int))

    # Array of 0s
    print(np.zeros((3, 2)))

    # Generate an array full of random number, uniformly sample from [0.0, 1.0]
    print(np.random.random((5, 4)))  # pass in a size array
    print(np.random.rand(5, 4))      # function arguments not a tuple

    # Sample numbers from a Gaussian (normal) distribution
    print(np.random.normal(size=(2,3)))  # "standard normal" (mean = 0, s.d. = 1)
    print(np.random.normal(50, 10, size=(2, 3)))  # mean =  50, s.d. = 10

    # Random integer
    print(np.random.randint(10))     # a single integer i [0,10)
    print(np.random.randint(0, 10))  # same as above, specifying [low, high] explicit
    print(np.random.randint(0, 10, size=5))  # 5 random integer as a 1D array
    print(np.random.randint(0, 10, size=(2, 3)))  # 2x3 array of random integer

    # Shape
    a = np.random.random((5, 4))
    print(a)
    print(a.shape)
    print(len(a.shape)) # 2 dimensions
    print(a.shape[0])   # number of rows
    print(a.shape[1])   # number of columns
    print(a.size)       # number of elements
    print(a.dtype)      # data type

    # Operations on ndarrays
    np.random.seed(693)
    a = np.random.randint(0, 10, size=(5, 4))  # 5x4 random integers in [0.10)
    print("Array:\n", a)

    # Sum of all elements
    print("Sum of all elements:", a.sum())



if __name__ == "__main__":
    test_run()
