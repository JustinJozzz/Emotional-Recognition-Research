# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/home/justin/Documents/Emotion Recognition"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/home/justin/Documents/Emotion Recognition/build"

# Include any dependencies generated for this target.
include CMakeFiles/AddBoxesToData.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/AddBoxesToData.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/AddBoxesToData.dir/flags.make

CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.o: CMakeFiles/AddBoxesToData.dir/flags.make
CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.o: ../AddBoxesToData.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/justin/Documents/Emotion Recognition/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.o -c "/home/justin/Documents/Emotion Recognition/AddBoxesToData.cpp"

CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/justin/Documents/Emotion Recognition/AddBoxesToData.cpp" > CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.i

CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/justin/Documents/Emotion Recognition/AddBoxesToData.cpp" -o CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.s

CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.o.requires:

.PHONY : CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.o.requires

CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.o.provides: CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.o.requires
	$(MAKE) -f CMakeFiles/AddBoxesToData.dir/build.make CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.o.provides.build
.PHONY : CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.o.provides

CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.o.provides.build: CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.o


# Object files for target AddBoxesToData
AddBoxesToData_OBJECTS = \
"CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.o"

# External object files for target AddBoxesToData
AddBoxesToData_EXTERNAL_OBJECTS =

AddBoxesToData: CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.o
AddBoxesToData: CMakeFiles/AddBoxesToData.dir/build.make
AddBoxesToData: dlib_build/libdlib.a
AddBoxesToData: /usr/lib/x86_64-linux-gnu/libnsl.so
AddBoxesToData: /usr/lib/x86_64-linux-gnu/libSM.so
AddBoxesToData: /usr/lib/x86_64-linux-gnu/libICE.so
AddBoxesToData: /usr/lib/x86_64-linux-gnu/libX11.so
AddBoxesToData: /usr/lib/x86_64-linux-gnu/libXext.so
AddBoxesToData: /home/justin/miniconda3/lib/libpng.so
AddBoxesToData: /home/justin/miniconda3/lib/libjpeg.so
AddBoxesToData: /home/justin/miniconda3/lib/libmkl_rt.so
AddBoxesToData: /home/justin/miniconda3/lib/libsqlite3.so
AddBoxesToData: CMakeFiles/AddBoxesToData.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/home/justin/Documents/Emotion Recognition/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable AddBoxesToData"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/AddBoxesToData.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/AddBoxesToData.dir/build: AddBoxesToData

.PHONY : CMakeFiles/AddBoxesToData.dir/build

CMakeFiles/AddBoxesToData.dir/requires: CMakeFiles/AddBoxesToData.dir/AddBoxesToData.cpp.o.requires

.PHONY : CMakeFiles/AddBoxesToData.dir/requires

CMakeFiles/AddBoxesToData.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/AddBoxesToData.dir/cmake_clean.cmake
.PHONY : CMakeFiles/AddBoxesToData.dir/clean

CMakeFiles/AddBoxesToData.dir/depend:
	cd "/home/justin/Documents/Emotion Recognition/build" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/home/justin/Documents/Emotion Recognition" "/home/justin/Documents/Emotion Recognition" "/home/justin/Documents/Emotion Recognition/build" "/home/justin/Documents/Emotion Recognition/build" "/home/justin/Documents/Emotion Recognition/build/CMakeFiles/AddBoxesToData.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/AddBoxesToData.dir/depend
