#include <iostream>
#include <queue>
#include <algorithm>
#include <memory.h>
using namespace std;
int n, m;
char v[54][54];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int visited[54][54];
int maxValue = 0;

void bfs(int y, int x) {
    memset(visited, 0, sizeof(visited));
    visited[y][x] = 1;
    queue<pair<int, int>> q;
    q.push({y,x});
    while(!q.empty()) {
        tie(y,x) = q.front(); q.pop();
        for(int i = 0; i < 4; i++) {
            int nx = dx[i] + x;
            int ny = dy[i] + y;
            if(nx < 0 || nx >= m || ny < 0 || ny >= n) {
                continue;
            }
            if(visited[ny][nx]) continue;
            if(v[ny][nx] == 'W') continue;
            visited[ny][nx] = visited[y][x] + 1;
            q.push({ny, nx});
            maxValue = max(maxValue, visited[ny][nx]);
        }
    }
    return;
}

int main() {
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> v[i][j];
        }
    }
    for(int i =0; i < n; i++) {
        for(int j =0; j < m; j++) {
            if(v[i][j] == 'L') bfs(i,j);
        }
    }
    cout << maxValue - 1 << "\n";
    return 0;
}
