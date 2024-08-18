#!/usr/bin/env python

# NOTE: Requires python 3.7 or greater

# NOTE: This is a minimalistic dependency.
#
# If tests, or further extentions are to be implemented,
# then there should be no other dependency than the builtin standard library.

# Proof of concept
from math import isinf, isnan


def float_is_close(
    a: float, b: float, significand: int, relative_tolerance: float = 1e-9
) -> bool:
    # Numbers are equal
    if a == b:
        return True

    # Arguments are not numbers
    if isinf(a) or isinf(b) or isnan(a) or isnan(b):
        return False

    absolute_tolerance = 10**-significand
    tolerance = max(
        relative_tolerance * max(abs(a), abs(b)), absolute_tolerance
    )
    diff = abs(a - b)

    return diff <= tolerance


# 1e-15 is not equal to 2e-15
result = float_is_close(1e-15, 2e-15, 15)
print(result is False)  # NOTE: This resolves to False
