#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int n, m, a[54][54], result = 999999999;
vector<vector<int>> chickenList;
vector<pair<int, int>> home, chicken;

void combination(int start, vector<int> v) {
    if(v.size() == m) {
        chickenList.push_back(v);
        return;
    }

    for(int i = start + 1; i < chicken.size(); i++) {
        v.push_back(i);
        combination(i, v);
        v.pop_back();
    }
    return;
}

int main() {
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> a[i][j];
            if(a[i][j] == 1) home.push_back({i,j});
            if(a[i][j] == 2) chicken.push_back({i, j});
        }
    }
    vector<int> v;
    combination(-1, v);
    for(vector<int> cList : chickenList) {
        int answer = 0;
        for(pair<int, int> h : home) {
            int _min = 987654321;
            for(int ch : cList) {
                int dist = abs(h.first - chicken[ch].first) + abs(h.second - chicken[ch].second);
                _min = min(_min, dist);
            }
            answer += _min;
        }
        result = min(result, answer);
    }
    cout << result << "\n";
    return 0;
}
