"""Create NumPy arrays."""

import numpy as np


def test_run():
    # List to 1D array
    print(np.random.normal(size=(2, 3)))  # "standard normal" (mean = 0, s.d. = 1)
    print(np.random.normal(50, 10, size=(2, 3)))  # mean =  50, s.d. = 10


if __name__ == "__main__":
        test_run()
