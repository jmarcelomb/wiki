# CMake

## Options variables:
```bash
cmake -Doption_variable_name=OFF -S . -B build_dir
```

## Commands:
```bash
cmake -S source_dir -B build_dir
```

## Get submodules:
```cmake
find_package(Git QUIET)
if(GIT_FOUND AND EXISTS "${PROJECT_SOURCE_DIR}/.git")
# Update submodules as needed
    option(GIT_SUBMODULE "Check submodules during build" ON)
    if(GIT_SUBMODULE)
        message(STATUS "Submodule update")
        execute_process(COMMAND ${GIT_EXECUTABLE} submodule update --init --recursive
                        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                        RESULT_VARIABLE GIT_SUBMOD_RESULT)
        if(NOT GIT_SUBMOD_RESULT EQUAL "0")
            message(FATAL_ERROR "git submodule update --init --recursive failed with ${GIT_SUBMOD_RESULT}, please checkout submodules")
        endif()
    endif()
endif()

if(NOT EXISTS "${PROJECT_SOURCE_DIR}/extern/repo/CMakeLists.txt")
    message(FATAL_ERROR "The submodules were not downloaded! GIT_SUBMODULE was turned off or failed. Please update submodules and try again.")
endif()
```

## Versioning source code:
```cmake
project(project_name VERSION "1.0.0")

configure_file(file_name.h.in file_name.h) 

add_executable(...)

target_include_directories(${PROJECT_NAME} PUBLIC ${PROJECT_BINARY_DIR})
```

file_name.h.in

```cpp
#ifndef INCLUDE_GUARD
#define INCLUDE_GUARD

#define PROJECT_NAME "@PROJECT_NAME@"
#define PROJECT_VER  "@PROJECT_VERSION@"
#define PROJECT_VER_MAJOR "@PROJECT_VERSION_MAJOR@"
#define PROJECT_VER_MINOR "@PROJECT_VERSION_MINOR@"
#define PTOJECT_VER_PATCH "@PROJECT_VERSION_PATCH@"

#endif // INCLUDE_GUARD
```

## #cmakedefine
```cmake
# adder use logic
option(USE_ADDER "A simple library for adding 2 floats." ON)

if(USE_ADDER)
	add_subdirectory(Adder)

	list(APPEND EXTRA_LIB_DIRS "Adder")
	list(APPEND EXTRA_INCLUDE_DIRS "Adder")
	list(APPEND EXTRA_LINKS adder)

endif()

target_include_directories(${PROJECT_NAME} 
    PUBLIC external/glfw/include
	${EXTRA_INCLUDE_DIRS}
	${GLEW_INCLUDE_DIRS}
)

target_link_directories(${PROJECT_NAME} 
	PUBLIC external/glfw/src
	${EXTRA_LIB_DIRS}
)

target_link_libraries(${PROJECT_NAME} ${EXTRA_LINKS} glfw ${GLEW_LIBRARIES} GL GLU)
```

```cpp
#cmakedefine USE_ADDER
```

## Example of CMakeLists.txt:

```cmake
cmake_minimum_required(VERSION 3.13.4)

project(PROJECT_NAME)

add_executable(${PROJECT_NAME} main.cpp)

add_subdirectort(Adder) // Adds paths

target_include_directories(${PROJECT_NAME} PUBLIC Adder)

target_link_directories(${PROJECT_NAME} PRIVATE Adder)

target_link_libraries(${PROJECT_NAME} PRIVATE adder)
```