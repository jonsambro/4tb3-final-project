#include <iostream>
using namespace std;

int main()
{
    int n = 1000000000;
    double a = 0;
    double b = 100.0;
    double r = 0;
    double ss = (b-a)/n;

    for (int i = 0; i < n; i++){
        double x = i*ss + a;
        double y = x*x + 3*x + 10.0;
        r = r + y*ss;
    }

    cout << r << endl;
    return 0;
}