/**
 * Copyright © 2024 Austin Berrio
 *
 * @file float_is_close.h
 *
 * @brief Compare floating-point numbers with a given tolerance in pure C
 */

#ifndef FLOAT_IS_CLOSE_H
#define FLOAT_IS_CLOSE_H

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

/**
 * @brief The smallest difference between two distinct double-precision
 *        floating-point numbers (optional).
 *
 * @note For 64-bit doubles with a 53-bit significand, this is approximately
 *       10**-15.
 */
#define DOUBLE_EPSILON               1e-15

/**
 * @brief The smallest difference between two distinct single-precision
 *        floating-point numbers (optional).
 *
 * @note For 32-bit floats with a 24-bit significand, this is approximately
 *       10**-7.
 */
#define SINGLE_EPSILON               1e-7

/**
 * @brief Get the minimum of two values.
 *
 * @note This macro compares two arguments and returns the smaller one.
 */
#define min(a, b)                    (((a) < (b)) ? (a) : (b))

/**
 * @brief Get the maximum of two values.
 *
 * @note This macro compares two arguments and returns the larger one.
 */
#define max(a, b)                    (((a) > (b)) ? (a) : (b))

/**
 * @brief Clamp a value to a specified range.
 *
 * @note This macro ensures that a value stays within a given range by
 *       clamping it to the specified minimum and maximum values.
 */
#define clamp(val, min_val, max_val) (min(max((val), (min_val)), (max_val)))

/**
 * @brief Determine if two double-precision floating-point numbers are close
 *        within a specified tolerance.
 *
 * @param a           The first floating-point number.
 * @param b           The second floating-point number.
 * @param significand The number of significant digits to consider (must be
 *                    in the range 1 to 15 inclusive). This determines the
 *                    absolute tolerance.
 *
 * @return            True if the numbers are close within the specified
 *                    tolerance, false otherwise.
 *
 * @note The significand is clamped if it is out of range.
 */
bool double_is_close(double a, double b, size_t significand);

/**
 * @brief Determine if two single-precision floating-point numbers are close
 *        within a specified tolerance.
 *
 * @param a           The first floating-point number.
 * @param b           The second floating-point number.
 * @param significand The number of significant digits to consider (must be
 *                    in the range 1 to 15 inclusive). This determines the
 *                    absolute tolerance.
 *
 * @return            True if the numbers are close within the specified
 *                    tolerance, false otherwise.
 */
bool float_is_close(float a, float b, size_t significand);

#endif // FLOAT_IS_CLOSE_H
