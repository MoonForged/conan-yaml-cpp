# conan-yaml-cpp
[Conan](https://conan.io) package for the yaml-cpp library ([https://github.com/jbeder/yaml-cpp](https://github.com/jbeder/yaml-cpp)).

[//]: # (conan.io badge here)

This package depends on [Boost/1.60.0@lasote/stable](https://www.conan.io/source/Boost/1.60.0/lasote/stable).

[//]: # (AppVeyor badge)
[//]: # (Travis CI badge)

## Example

The following example shows how to use this Conan package with CMake.  See Conan's
documentation for other generators if you are not using CMake.

Add the package to your project's *conanfile.txt*:

```
[requires]
yaml-cpp/0.5.3@moonforged/stable

[generators]
cmake
```

Your *CMakeLists.txt*:

```CMake
project(YourProject)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})
```

And then your *example.cpp*:

```cpp
#include <yaml-cpp/yaml.h>

int main()
{
  YAML::Node node = YAML::Load("[1, 2, 3]");
  // ...
  return 0;
}
```

Then you can use it as:

```bash
$ mkdir build && cd build
$ conan install ..
$ cmake .. -G "Visual Studio 14 Win64"
$ cmake --build . --config Release
$ bin/example
```
