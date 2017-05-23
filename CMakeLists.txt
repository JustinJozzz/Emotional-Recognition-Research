cmake_minimum_required(VERSION 2.8.12)

project(AddBoxesToData)

include(./dlib-19.4/dlib/cmake)
  
add_executable(AddBoxesToData AddBoxesToData.cpp)

target_link_libraries(AddBoxesToData dlib::dlib)
