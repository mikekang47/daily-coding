#include <iostream>
using namespace std;
int arr[11];

int main() {
    for(int i = 0; i < 10; i++) {
        cin >> arr[i];
    }
    int sum = 0;
    for(int i = 0; i < 10; i++) {
        int a = sum;
        int b = sum + arr[i];
        if(b < 100) {
            sum = b;
        } else if(b == 100){
            cout << b;

        } else {
            if(b - 100 > 100 - a) {
                cout << a;

            } else if(b - 100 == 100 -a) {
               cout << b;

            } else {
                cout << b;
            }
        }
    }
    return 0;
}
