/**
 * Copyright © 2024 Austin Berrio
 *
 * @file float_is_close.c
 *
 * @brief Compare floating-point numbers with a given tolerance in pure C
 *
 * @note The 64-bit implementation is reverse compatible with the 32-bit
 * implementation. Whatever is true for the 64-bit implementation must then be
 * true for the 32-bit implementation.
 */

#include "float_is_close.h"

#include <stdbool.h>
#include <stdint.h>

// Determine a floating-point equality within a specified tolerance
bool double_is_close(double a, double b, int64_t significand) {
    // Numbers are equal
    if (a == b) {
        return true;
    }

    // Arguments are not numbers
    if (isinf(a) || isinf(b) || isnan(a) || isnan(b)) {
        return false;
    }

    // Calculate the minimum tolerance based on the significand
    significand          = (0.0 > significand) ? significand : -significand;
    double min_tolerance = pow(10.0, significand);
    // Calculate the maximum tolerance based on the scale of the numbers
    double max_tolerance = min_tolerance * fmax(fabs(a), fabs(b));

    // Compare the absolute difference between the numbers within the tolerance
    // range
    return fabs(a - b) <= fmax(max_tolerance, min_tolerance);
}

// Determine a floating-point equality within a specified tolerance
bool float_is_close(float a, float b, int32_t significand) {
    // Numbers are equal
    if (a == b) {
        return true;
    }

    // Arguments are not numbers
    if (isinf(a) || isinf(b) || isnan(a) || isnan(b)) {
        return false;
    }

    // Calculate the minimum tolerance based on the significand
    significand         = (0.0f > significand) ? significand : -significand;
    float min_tolerance = powf(10.0f, significand);
    // Calculate the maximum tolerance based on the scale of the numbers
    float max_tolerance = min_tolerance * fmaxf(fabsf(a), fabsf(b));

    // Compare the absolute difference between the numbers within the tolerance
    // range
    return fabsf(a - b) <= fmaxf(max_tolerance, min_tolerance);
}
