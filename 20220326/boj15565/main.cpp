#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int n, k;

int main() {
    cin >> n >> k;
    vector<int> v;
    vector<int> idx;
    for(int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        if(temp == 1)
            idx.push_back(i);
        v.push_back(temp);
    }
//    0, 4, 6, 10
    int minValue = 99999999999;
    if(idx.size() < k) {
        cout << -1;
        return 0;
    }

    for(int i =0; i <= idx.size() - k; i++) {
        minValue = min(idx[i+k-1]-idx[i]+1, minValue);
    }
    cout << minValue;

    return 0;
}
