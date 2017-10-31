project(viennagrid_test)
cmake_minimum_required(VERSION 3.2)
set(CMAKE_CXX_STANDARD 11)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

#test building with CMake module
find_package(ViennaGrid REQUIRED)

add_executable(package_test main.cpp)
target_include_directories(package_test PUBLIC ${VIENNAGRID_INCLUDE_DIR})

add_executable(package_test2 main.cpp)
target_link_libraries(package_test2 CONAN_PKG::viennagrid)

#test building with cmake targets
