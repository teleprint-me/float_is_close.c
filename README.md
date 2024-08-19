# float-is-close.c
**Compare floating-point numbers with a given tolerance in C**

## Overview
`float-is-close.c` is a C library designed to accurately compare floating-point numbers with a configurable tolerance. It provides functions to compare both single-precision and double-precision floating-point numbers. This library is intended to be lightweight, efficient, and easy to integrate into existing C projects.

## Directory Structure
```plaintext
.
├── auto-build -> auto_build.sh
├── auto_build.sh
├── CMakeLists.txt
├── float_is_close.py
├── include
│   └── float_is_close.h
├── LICENSE
├── README.md
├── src
│   └── float_is_close.c
└── tests
    └── test_float_is_close.c
```

- **`auto-build`**: A symbolic link to `auto_build.sh`, which automates the build and test process.
- **`auto_build.sh`**: Shell script for automated build and testing.
- **`CMakeLists.txt`**: CMake configuration file for building the project.
- **`float_is_close.py`**: Python proof of concept or utility script.
- **`include/float_is_close.h`**: Header file containing the public API.
- **`LICENSE`**: The project is licensed under the AGPL.
- **`README.md`**: This file.
- **`src/float_is_close.c`**: Source file implementing the floating-point comparison functions.
- **`tests/test_float_is_close.c`**: Test cases for the implemented functions.

## Building the Project
To build the project, run the `auto_build.sh` script. This script automates the cleaning, building, and testing processes.

### Steps:
1. Clone the repository:
    ```sh
    git clone https://github.com/teleprint-me/float_is_close.c float-is-close
    cd float-is-close
    ```
2. Run the build script:
    ```sh
    ./auto-build
    ```
   This will configure and build the project using CMake, compile the source files, and run the tests.

### Build Output
After building, the structure of the `build/` directory will look like this:

```plaintext
build/
├── bin
│   └── test_float_is_close
├── lib
│   └── libfloat_is_close.so -> libfloat_is_close.so.0.1.0
└── ...
```

- **`build/bin/`**: Contains the test executable.
- **`build/lib/`**: Contains the shared library file.

## API Documentation
The primary API functions are defined in `include/float_is_close.h`.

### `double_is_close`
```c
bool double_is_close(double a, double b, size_t significand);
```
- **Parameters**:
  - `a`, `b`: The double-precision floating-point numbers to compare.
  - `significand`: The number of significant digits to consider (1-15).
- **Returns**: `true` if the numbers are close within the specified tolerance, otherwise `false`.

### `float_is_close`
```c
bool float_is_close(float a, float b, size_t significand);
```
- **Parameters**:
  - `a`, `b`: The single-precision floating-point numbers to compare.
  - `significand`: The number of significant digits to consider (1-7).
- **Returns**: `true` if the numbers are close within the specified tolerance, otherwise `false`.

### Macros
- **`FIC_MIN(a, b)`**: Returns the minimum of two values.
- **`FIC_MAX(a, b)`**: Returns the maximum of two values.
- **`FIC_CLAMP(value, lower, upper)`**: Clamps a value within a specified range.

## References

### Mathematical Background:
- [Calculus](https://math.libretexts.org/Bookshelves/Calculus/Calculus_3e_(Apex))
- [Discrete Mathematics](https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Discrete_Mathematics_(Levin))

### Original Papers:
- [APL comparison tolerance](https://dl.acm.org/doi/10.1145/800114.803685)
- [PEP-0485](https://peps.python.org/pep-0485/)

### Original Source Code:
- [Christopher Barker's Proof of Concept](https://github.com/PythonCHB/close_pep/blob/master/is_close.py)

## License
This project is licensed under the AGPL License - see the [LICENSE](LICENSE) file for details.
