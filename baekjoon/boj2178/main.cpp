#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int graph[101][101];
int visited[101][101];
int dy[4] = {0, 0, 1, -1};
int dx[4] = {1, -1, 0, 0};
int n, m;

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%1d", &graph[i][j]);
        }
    }
    queue<pair<int, int>> q;
    q.push(make_pair(0, 0));
    visited[0][0] = 1;
    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++) {
            int ny = dy[i] + y;
            int nx = dx[i] + x;
            if (ny < 0 || ny >= n || nx < 0 || nx >= m || graph[ny][nx] == 0 || visited[ny][nx] != 0) {
                continue;
            }
            visited[ny][nx] = visited[y][x] + 1;
            q.push(make_pair(ny, nx));
        }
    }
    cout << visited[n - 1][m - 1] << endl;
    return 0;
}
