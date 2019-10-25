#include <assert.h>
#include "exported.h"
#include "mylib.h"

void TestCase0()
{
    int x = add(1, 2);

    assert(x == 3);
    assert(x > 0);
    assert(x < 5);
}

int main(int argc, char *argv[])
{
    TestCase0();
}
