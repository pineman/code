#!/bin/bash
export HOST=x86_64-w64-mingw32
export CC=$HOST-gcc
export CXX=$HOST-g++
export CPP=$HOST-cpp
export RANLIB=$HOST-ranlib
export AR=$HOST-ar
export LD=$HOST-ld
export AS=$HOST-as
export STRIP=$HOST-strip
export PKG_CONFIG=$HOST-pkg-config

export PATH="/usr/$HOST/bin:/usr/$HOST/lib/qt/bin:$PATH"
