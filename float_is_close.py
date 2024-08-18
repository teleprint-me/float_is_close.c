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
# This means we can treat the 64-bit as an infinitesimal value
# and declare it as epsilon which gives us a valid range of
# potential input values.
def float_is_close(a: float, b: float, significand: int) -> bool:
    # Has equality
    if a == b:
        return True

    # Not a number
    if isinf(a) or isinf(b) or isnan(a) or isnan(b):
        return False

    # Ensure significand is positive and non-zero
    significand = max(1, abs(significand))

    # Calculate the absolute tolerance as a power of 10
    absolute = 10**-significand

    # NOTE:
    # The closest we can get to zero with 64-bits, the infinitesimal value,
    # is 10**-(16 - 1) for because the significand is 53-bits.
    # This becomes equivalent to calculating 10.0**-15.
    # We can pre-calculate this because it's a predictable constant value.
    epsilon = 0.000000000000001  # pow(10.0, -15)
    # Calculate the relative tolerance
    relative = epsilon * max(abs(a), abs(b))

    # Calculate the absolute difference between the input values
    difference = abs(a - b)

    # Calculate the relative inequality
    return difference <= max(relative, absolute)


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
