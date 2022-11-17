cmake_minimum_required(VERSION 3.17)
include(ExternalProject)

project(aoc2020)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_EXTENSIONS OFF)
if(CMAKE_BUILD_TYPE STREQUAL Release)
    set(MAIN main.cpp)
else()
    set(MAIN test_main.cpp)
endif()
add_executable(aoc2020 ${MAIN} cenas.cpp cenas.h)

ExternalProject_Add(
        doctest
        GIT_REPOSITORY https://github.com/doctest/doctest.git
        GIT_TAG v2.4.9
        CONFIGURE_COMMAND ""
        BUILD_COMMAND ""
        INSTALL_COMMAND ""
)
ExternalProject_Get_Property(doctest source_dir)
set(DOCTEST_INCLUDE_DIR ${source_dir}/doctest CACHE INTERNAL "Path to include folder for doctest")
target_include_directories(aoc2020 PRIVATE ${DOCTEST_INCLUDE_DIR})
if(CMAKE_BUILD_TYPE STREQUAL Release)
    target_compile_definitions(aoc2020 PRIVATE DOCTEST_CONFIG_DISABLE)
endif()
add_dependencies(aoc2020 doctest)
