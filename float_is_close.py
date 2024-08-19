#!/usr/bin/env python

"""
Copyright © 2024 Austin Berrio

float_is_close.py

Proof of concept for float_is_close.c in pure Python.

Requires Python 3.7 or greater.

This script is minimalistic with no dependencies beyond the standard library.

IMPORTANT: The 53-bit significand precision gives 15 to 17 significant decimal
           digits of precision (2e-53 ≈ 1.11 x 10e-16).

See PEP-0485 for implementation details.
- https://peps.python.org/pep-0485/
"""

from dataclasses import dataclass
from math import inf, isinf, isnan, nan


# Max is 10**-(16 - 1) for 64-bit; significand is 53-bits
# Max is 10**-(8 - 1) for 32-bit; significand is 24-bits
# float_is_close function checks if two floating point numbers
# are close within a specified precision.
def float_is_close(a: float, b: float, significand: int) -> bool:

    # Check for equality
    if a == b:
        return True

    # Handle cases where either number is NaN or infinity
    if (isnan(a) or isnan(b)) or (isinf(a) or isinf(b)):
        return False

    # Ensure significand is positive and non-zero
    significand = max(1, abs(significand))

    # Calculate absolute tolerance based on the number of
    # decimal digits in significand.
    absolute_tolerance = 10.0 ** (-significand)

    # Predefined infinitesimal value for 64-bit floats (53 bits significand),
    # equivalent to 1e-15.
    epsilon = 1e-15

    # Calculate relative tolerance based on the larger absolute value
    # between a and b.
    relative_tolerance = epsilon * max(abs(a), abs(b))

    # Compute the difference between input values
    difference = abs(a - b)

    # Check if difference is within the specified tolerance (absolute or relative)
    return difference <= max(relative_tolerance, absolute_tolerance)


@dataclass
class TestCase:
    a: float
    b: float
    significand: int
    expected: bool


def fixture_float_is_close() -> list[TestCase]:
    # Arbitrary values used for testing
    n: float = 0.053803  # example value with a fraction
    m: float = 123456789.123456  # example large value
    o: float = 0.053721  # slightly less than n
    p: float = 0.053951  # slightly more than n

    return [
        # Precision within a range of 6 digits
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
        TestCase(1e6, 1e6 + 1, 0, False),  # no precision
        TestCase(1e-6, 1e-6 + 1e-9, 6, True),  # Very close but small tolerance
        # Test large significand
        TestCase(123456789.123456, m, 15, True),
        # Test differentiated large significand
        TestCase(m, 123456789.123457, 15, False),
        # Small numbers with large tolerance
        # NOTE: This will always resolve to True even if it is False
        TestCase(1e-15, 2e-15, 15, True),
    ]


def test_float_is_close() -> bool:
    """
    Returns True if all tests pass, False if any test fails.
    """
    test_cases = fixture_float_is_close()

    all_tests_pass = True
    for i, case in enumerate(test_cases, 1):
        result = float_is_close(case.a, case.b, case.significand)
        if result != case.expected:
            print(
                f"Test {i} failed: "
                f"float_is_close({case.a}, {case.b}, {case.significand}) "
                f"returned {result}, expected {case.expected}."
            )
            all_tests_pass = False

    return all_tests_pass


if __name__ == "__main__":
    if test_float_is_close():
        print("All tests passed.")
    else:
        print("Some tests failed.")
