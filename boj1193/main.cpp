#include <iostream>

using namespace std;
int x;
int a, b;

int main() {
    cin >> x;
    int i = 1;
    while (x > i) {
        x -= i;
        i += 1;
    }
    if (i % 2 == 0) {
        a = x;
        b = i - x + 1;
    } else {
        a = i - x + 1;
        b = x;
    }
    cout << a << "/" << b << endl;
    return 0;
}
