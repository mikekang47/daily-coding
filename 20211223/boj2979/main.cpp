#include <iostream>
using namespace std;
int main() {
    int arr[104] = {0};
    int a, b, c;
    cin >> a >> b >> c;
    for(int i = 0; i < 3; i++) {
        int x, y;
        cin >> x >> y;
        for(int j = x; j < y; j++) {
            arr[j] += 1;
        }
    }
    int sum = 0;
    for(int i : arr) {
        if(i == 1) {
            sum += a;
        } else if(i == 2) {
            sum += b * 2;
        } else if(i == 3){
            sum += c * 3;
        }
    }
    cout << sum;
    return 0;
}
