#include <iostream>
#include <cmath>
using namespace std;
int n, k;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> n;
    cin >> k;
    int result =0;
    int left = 1;
    int right = k;
    while(left <= right) {
        int middle = (left + right) / 2;
        int cnt = 0;
        for(int i = 1; i<= n; i++) {
            cnt += min(middle/i, n);
        }
        if(cnt < k) {
            left = middle + 1;
        } else {
            result = middle;
            right = middle - 1;
        }
    }
    cout << result;
}