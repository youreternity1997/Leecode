// C++ code
#include <iostream>
using namespace std;

int main() {
    int n = 10;
    int m = 20;
    int* const p = &n;
    cout << p << endl; // 0x61ff04 
    p = &m; // error: assignment of read-only variable 'p'
    cout << p << endl;
    return 0;
}



