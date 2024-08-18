#!/usr/bin/env python

"""
Copyright © 2024 Austin Berrio

float_is_close.py

Proof of concept for float_is_close.c in pure Python.

Requires Python 3.7 or greater.

This script is minimalistic with no dependencies beyond the standard library.

IMPORTANT: The 53-bit significand precision gives 15 to 17 significant decimal
           digits of precision (2e-53 ≈ 1.11 x 10e-16).
"""

from math import isinf, isnan


def float_is_close(
    a: float, b: float, significand: int, relative_tolerance: float = 1e-15
) -> bool:
    if a == b:
        return True

    if isinf(a) or isinf(b) or isnan(a) or isnan(b):
        return False

    # Ensure significand is positive and non-zero
    significand = max(1, abs(significand))

    # Calculate the absolute tolerance as a power of 10
    absolute_tolerance = 10**-significand

    # Compute the tolerance considering both relative and absolute tolerance
    tolerance = max(
        relative_tolerance * max(abs(a), abs(b)), absolute_tolerance
    )

    # Calculate the absolute difference between the input values
    difference = abs(a - b)

    return difference <= tolerance


if __name__ == "__main__":
    result = float_is_close(1e-15, 2e-15, 15)
    print(
        result is False
    )  # Expected output: True (since the values are not close)
