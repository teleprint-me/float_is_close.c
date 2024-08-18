cmake_minimum_required(VERSION 3.14)

project(
    float_is_close
    VERSION 0.1.0
    DESCRIPTION "Compare floating-point numbers with a given tolerance"
)

# Set C standard rules
set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS ON)

# Set the output directory for built binaries
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin)
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR}/lib)

option(BUILD_SHARED_LIBS "Build using shared libraries" ON)

# Main library
add_library(
    float_is_close
    float_is_close.c
)

set_target_properties(
    float_is_close PROPERTIES 
    VERSION ${PROJECT_VERSION}
    RUNTIME_OUTPUT_DIRECTORY ${EXECUTABLE_OUTPUT_PATH}
    PUBLIC_HEADER float_is_close.h
)

target_include_directories(float_is_close PUBLIC include)

# Add test executable
add_executable(test_float_is_close test_is_float_close.c)
target_link_libraries(test_float_is_close float_is_close m)

# Install rules for the library
install(
    TARGETS float_is_close
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    PUBLIC_HEADER DESTINATION include
)

# Add a custom target to run tests
add_custom_target(
    run_tests
    COMMAND ${EXECUTABLE_OUTPUT_PATH}/test_float_is_close
    DEPENDS test_float_is_close
    COMMENT "Running tests for float_is_close"
)

enable_testing()
add_test(
    NAME float_is_close
    COMMAND ${EXECUTABLE_OUTPUT_PATH}/test_float_is_close
)
