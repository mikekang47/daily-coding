#include <iostream>

using namespace std;
int arr[11];
int main() {
    int sum = 0;
    for(int i = 0; i < 10; i++) {
        cin >> arr[i];
    }
    for(int i = 0; i < 10; i++) {
        int a = sum;
        int b = sum + arr[i];
        if(b == 100) {
            cout << b;
            return 0;
        } else {
            if(b < 100) {
                sum += arr[i];
            } else {
              if(a + b == 200) {
                  cout << b;
                  return 0;
              } else {
                  if(b - 100 < 100 - a) {
                      cout << b;
                      return 0;
                  } else {
                      cout << a;
                      return 0;
                  }
              }
            }
        }
    }

    return 0;
}
