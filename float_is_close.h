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
#include <stdint.h>

/**
 * @brief Determines if two floating-point values are approximately equal
 * within specified tolerances.
 *
 * @param[in]   a       The first floating-point value.
 * @param[in]   b       The second floating-point value.
 * @param[in]   tolerance Tolerance for comparing values (default:
 * FLOAT_TOLERANCE).
 *
 * @return true if the absolute difference between 'a' and 'b' is within the
 * tolerance bounds, false otherwise.
 */
bool float_is_close(float a, float b, int32_t significand);

bool double_is_close(double a, double b, int64_t significand);

#endif // FLOAT_IS_CLOSE_H
