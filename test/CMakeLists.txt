file(GLOB TESTSOURCES "*.cpp")
add_executable(mylib_test ${TESTSOURCES})

target_link_libraries(mylib_test
    PRIVATE
        MyLibrary::mylib
)

add_test(
    NAME mylib_test
    COMMAND mylib_test
)
