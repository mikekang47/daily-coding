#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int n, w, k, temp;
vector<int> v;

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> temp;
        v.push_back(temp);
    }
    sort(v.begin(), v.end());
    int len = v.size();
    int max = len * v[0];
    int i = 1;
    for (int i = 1; i < n; i++) {
        len -= 1;
        if (v[i] * len > max) {
            max = v[i] * len;
        }
    }
    cout << max << "\n";
    return 0;
}
