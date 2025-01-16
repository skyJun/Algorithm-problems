#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;

    if ((A == 1 && B == 2) ||
        (A == 2 && B == 3) ||
        (A == 3 && B == 1))
    {
        cout << "B" << endl;
    }
    else
    {
        cout << "A" << endl;
    }

    return 0;

}