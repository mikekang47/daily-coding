#include <iostream>

using namespace std;

int main() {
    int m, n, j;
    cin >> n >> m;
    cin >> j;
    int sum = 0;
    int left = 1;
    for (int i = 0; i < j; i++) {
        int x;
        int right = left + m - 1;
        cin >> x;
        if (left <= x && x <= right) {
            continue;
        } else {
            if (x < left) {
                sum += left - x;
                left = x;
            } else {
                left += x - right;
                sum += x - right;
            }
        }
    }
    cout << sum << endl;
}
