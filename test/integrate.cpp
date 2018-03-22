#include <iostream>

int main()
{
    int n = 1000000000;
    auto fib = new long[n];
    fib[0] = 1.0;
    fib[1] = 1.0;

    for (int i = 2; i < n; i++){
        fib[i] = fib[i-1] + fib[i-2];
    }
    std::cout << fib[999] << std::endl;
    delete fib;
    return 0;
}