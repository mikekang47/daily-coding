#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
const int max_n = 104;
int n, m, graph[max_n][max_n], y, x, visited[max_n][max_n];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int main() {
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            scanf("%1d", &graph[i][j]);
        }
    }
    queue<pair<int, int>> q;
    q.push({0,0});
    visited[0][0] = 1;
    while(!q.empty()) {
        tie(y,x) = q.front();
        q.pop();
        for(int i = 0; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if(ny < 0 || ny >= n || nx < 0 || nx >= m || graph[ny][nx] == 0) continue;
            if(visited[ny][nx]) continue;
            visited[ny][nx] = visited[y][x] + 1;
            q.push({ny, nx});
        }
    }
    printf("%d", visited[n-1][m-1]);
    return 0;
}
