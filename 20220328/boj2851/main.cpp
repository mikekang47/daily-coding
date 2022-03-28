#include <iostream>

using namespace std;
int arr[11];
int main() {
    int sum = 0;
    for(int i = 0; i < 10; i++) {
        cin >> arr[i];
    }
    for (int i = 0; i < 10; i++) {
        int a = sum;
        int b = sum + arr[i];
        if (b >= 100) {
            if (b - 100 <= 100 - a) {
                cout << b;
            } else if (b - 100 > 100 - a) {
                cout << a;
            }
            return 0;
        }
        sum = b;
    }
    cout << sum;
    return 0;
}
