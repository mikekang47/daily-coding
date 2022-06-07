#include <iostream>
using namespace std;
int a, b, c, arr[101];
int main() {
    cin >> a >> b >> c;
    for(int i = 0; i < 3; i++) {
        int t, t1;
        cin >> t >> t1;
        for(int j = t; j < t1; j++) {
            arr[j]++;
        }
    }
    int sum = 0;
    for(int i : arr) {
        if(i == 1) {
            sum += a;
        } else if(i == 2) {
            sum += b * 2;
        } else if(i == 3) {
            sum += c * 3;
        }
    }
    cout << sum << "\n";
    return 0;
}
