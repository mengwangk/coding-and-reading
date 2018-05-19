"""Arithmetic operations"""

import numpy as np


def test_run():
    a = np.array([(1, 2, 3, 4, 5), (10, 20, 30, 40, 50)])
    print("Original array a \n:", a)

    # Multiply a by 2
    print("\nMultiply a by 2:\n", 2 * a)

    # Divide a by 2
    print("\nDivide a by 2:\n", a / 2.0)

    b = np.array([(100, 200, 300, 400, 500), (10, 20, 30, 40, 50)])
    print("Original array b \n:", b)

    # Add the 2 arrays
    print("\nAdd a + b \n", a + b)

    # Multiply the 2 arrays
    print("\nMultiply a * b \n", a * b)

    # Divide the 2 arrays
    print("\nDivide a / b \n", a / b)



if __name__ == "__main__":
    test_run()
