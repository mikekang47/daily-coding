#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v;
    int sum = 0;
    for (int i = 0; i < 9; ++i) {
        int temp;
        cin >> temp;
        v.push_back(temp);
        sum += temp;
    }
    int x, y;
    for(int i = 0; i < 8; i++) {
        for(int j = i +1; j < 9; j++) {
            if(sum - v[i] - v[j] == 100) {
                x= v[i];
                y = v[j];
            }
        }
    }
    sort(v.begin(), v.end());
    for(auto i : v) {
        if(i != x and i != y) {
            cout << i << "\n";
        }
    }

    return 0;
}
