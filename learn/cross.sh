#!/bin/sh
export HOST=x86_64-w64-mingw32
export CC=$HOST-gcc
export CXX=$HOST-g++
export CPP=$HOST-cpp
export RANLIB=$HOST-ranlib
export PATH="/usr/$HOST/bin:/usr/$HOST/lib/qt/bin:$PATH"
