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

from dataclasses import dataclass
from math import inf, isinf, isnan, nan


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


@dataclass
class TestCase:
    a: float
    b: float
    significand: int
    expected: bool


def fixture_float_is_close() -> list[TestCase]:
    # Arbitrary values used for testing
    n: float = 0.053803  # exclude the number while including the fraction
    m: float = 123456789.123456  # include number and fraction
    o: float = 0.053721  # less than n
    p: float = 0.053951  # greater than n

    return [
        # precision is within a range of 6 digits
        TestCase(0.053803, n, 6, True),  # equal to
        TestCase(n, o, 6, False),  # less than
        TestCase(n, p, 6, False),  # greater than
        # Negative numbers
        TestCase(-0.053803, -n, 6, True),  # equal to
        TestCase(-n, -o, 6, False),  # greater than
        TestCase(-n, -p, 6, False),  # less than
        # Inf and NaN cases
        TestCase(inf, inf, 6, True),  # INF is equal to itself
        TestCase(nan, 0.0, 6, False),  # NaN is not equal to any object
        TestCase(nan, nan, 6, False),  # NaN is not equal to itself
        # Large numbers with significant precision
        TestCase(1e6, 1e6 + 1, 0, True),  # no precision
        TestCase(1e-6, 1e-6 + 1e-9, 6, True),  # Very close but small tolerance
        # Test large significand
        TestCase(123456789.123456, m, 15, True),
        # Test differentiated large significand
        TestCase(m, 123456789.123457, 15, False),
        # Small numbers with large tolerance
        TestCase(1e-15, 2e-15, 15, False),
    ]


def test_float_is_close() -> bool:
    """
    Returns True if tests pass, False if any test fails completion
    """
    pass


if __name__ == "__main__":
    test_float_is_close()
