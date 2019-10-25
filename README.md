# CMake Cross-Platform Starter

* Another minimal CMake example of Cross-Platform shared library (DLL)
* A little more than Hello World with ctest and python ctypes


## How to Run

```bash
# build simple toy shared library
cd build
cmake ..
make    # or cmake --build .

# run trivial test
ctest

# test from Python ctypes (libmylib.dylib on Mac)
# you need to setup pyenv to use .python-version
python testpy/test_mac_dylib.py

# note: ctypes only works for C functions (but not C++ classes)
# https://stackoverflow.com/questions/1615813

# try changing + to * (or whatever) in the add function
# then both ctest and ctypes test will fail as expected
```

__note: my Mac environment__

* macOS High Sierra 10.13.6
* cmake version 3.15.4
* GNU Make 3.81
* Python version 3.7.3
* VSCode 1.39.2


## Inspired By

* Introduction to CMake by Example
  - http://derekmolloy.ie/hello-world-introductions-to-cmake/
  - https://github.com/derekmolloy/exploringBB/tree/master/extras/cmake
* Markus Rothe CMAKE TUTORIAL - Testing
  - https://www.markusrothe.dev/Testing/
* CMake: Project structure with unit tests
  - https://stackoverflow.com/questions/14446495
* A Simple Example
  - https://cliutils.gitlab.io/modern-cmake/chapters/basics/example.html
* C++で簡易単体テスト。assert、静的解析
  - https://qiita.com/YukiMiyatake/items/c474dc57277ac892c135
* Writing a Cross-Platform Dynamic Library
  - https://atomheartother.github.io/c++/2018/07/12/CPPDynLib.html
