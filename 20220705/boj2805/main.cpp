#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n, m, temp;
long long result;
vector<int> arr;

bool possible(long long mid) {
    long long cnt = 0;
    for(auto i : arr) {
        if(i - mid > 0)
            cnt += i - mid;
    }
    if(cnt >= m)
        return true;
    else
        return false;
}

int main() {
    cin >> n >> m;
    for(int i = 0; i< n; i++) {
        cin >> temp;
        arr.push_back(temp);
    }
    sort(arr.begin(), arr.end());
    result = 0;
    long long low = 1;
    long long high = *max_element(arr.begin(), arr.end());
    while (low <= high) {
        long long mid = (low + high) / 2;
        if(possible(mid)) {
            if(result < mid)
                result = mid;
            low = mid + 1;
        }
        else
            high = mid - 1;
    }
    cout << result;
    return 0;
}
