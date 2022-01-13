#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int m,n,k,x1, y1, x2, y2;
int _map[101][101] = {0,};
vector<int> ret;
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int dfs(int y, int x) {
    _map[y][x] = 1;
    int _ret = 1;
    for(int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if(nx < 0 || nx >=n || ny < 0 || ny >= m || _map[ny][nx] == 1) {
            continue;
        }
        _ret += dfs(ny,nx);
    }
    return _ret;
}
int main() {
    cin >> m >> n >> k;
    for(int i = 0; i < k; i++) {
        cin >> x1 >> y1 >> x2 >> y2;
        for(int x = x1; x < x2; x++) {
            for(int y = y1; y < y2; y++) {
                _map[y][x] = 1;
            }
        }
    }
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            if(_map[i][j] != 1) {
                ret.push_back(dfs(i,j));
            }
        }
    }
    cout << ret.size() << '\n';
    sort(ret.begin(), ret.end());
    for(int i : ret) {
        cout << i << ' ';
    }
    return 0;
}
