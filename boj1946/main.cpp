#include <iostream>

using namespace std;
int t, n, a, b, temp;
int arr[100001];

int main() {
    cin >> t;
    while (t--) {
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> a >> b;
            arr[a] = b;
        }
        temp = arr[1];
        int cnt = 1;
        for(int i = 2; i <= n; i++) {
            if(temp >= arr[i]) {
                cnt += 1;
                temp = arr[i];
            }
        }
        cout << cnt << "\n";

    }

    return 0;
}
