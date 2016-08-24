# conan-yaml-cpp
[Conan](https://conan.io) package for the yaml-cpp library ([https://github.com/jbeder/yaml-cpp](https://github.com/jbeder/yaml-cpp)).

[![badge](https://img.shields.io/badge/conan.io-yaml--cpp%2F0.5.3-green.svg?logo=data:image/png;base64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAA1VBMVEUAAABhlctjlstkl8tlmMtlmMxlmcxmmcxnmsxpnMxpnM1qnc1sn85voM91oM11oc1xotB2oc56pNF6pNJ2ptJ8ptJ8ptN9ptN8p9N5qNJ9p9N9p9R8qtOBqdSAqtOAqtR%2BrNSCrNJ/rdWDrNWCsNWCsNaJs9eLs9iRvNuVvdyVv9yXwd2Zwt6axN6dxt%2Bfx%2BChyeGiyuGjyuCjyuGly%2BGlzOKmzOGozuKoz%2BKqz%2BOq0OOv1OWw1OWw1eWx1eWy1uay1%2Baz1%2Baz1%2Bez2Oe02Oe12ee22ujUGwH3AAAAAXRSTlMAQObYZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfgBQkREyOxFIh/AAAAiklEQVQI12NgAAMbOwY4sLZ2NtQ1coVKWNvoc/Eq8XDr2wB5Ig62ekza9vaOqpK2TpoMzOxaFtwqZua2Bm4makIM7OzMAjoaCqYuxooSUqJALjs7o4yVpbowvzSUy87KqSwmxQfnsrPISyFzWeWAXCkpMaBVIC4bmCsOdgiUKwh3JojLgAQ4ZCE0AMm2D29tZwe6AAAAAElFTkSuQmCC)](http://www.conan.io/source/yaml-cpp/0.5.3/moonforged/stable)

This package depends on [Boost/1.60.0@lasote/stable](https://www.conan.io/source/Boost/1.60.0/lasote/stable).

[![Build status](https://ci.appveyor.com/api/projects/status/k2pn92v72s4h86s3?svg=true)](https://ci.appveyor.com/project/MoonForged/conan-yaml-cpp)
[![Build Status](https://travis-ci.org/MoonForged/conan-yaml-cpp.svg?branch=master)](https://travis-ci.org/MoonForged/conan-yaml-cpp)

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
