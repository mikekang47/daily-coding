#include <iostream>
#include <algorithm>
using namespace std;
int n, m, a[150001], cnt;
int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> n;
    cin >> m;
    for(int i = 0 ; i < n; i++) {
        cin >> a[i];
    }
    sort(a, a+n);
    for(int i = 0; i < n; i++) {
        for(int j = i+1; j < n; j++) {
            if(a[i] + a[j] == m)
                cnt++;
        }
    }
    cout << cnt;
    return 0;
}
