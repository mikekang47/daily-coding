#include <iostream>
#include <algorithm>

using namespace std;
int n;
int graph[101][101];
int visited[101][101];
int dy[4] = {0, 1, 0, -1};
int dx[4] = {1, 0, -1, 0};

void dfs(int y, int x, int height) {
    visited[y][x] = 1;
    for (int i = 0; i < 4; i++) {
        int ny = dy[i] + y;
        int nx = dx[i] + x;
        if (0 <= nx && 0 <= ny && nx < n && ny < n) {
            if (graph[ny][nx] > height && !visited[ny][nx]) {
                dfs(ny, nx, height);
            }
        }
    }
    return;
}

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> graph[i][j];
        }
    }
    int result = 1;
    for (int d = 1; d < 101; d++) {
        fill(&visited[0][0], &visited[0][0] + 101 * 101, 0);
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j] && graph[i][j] > d) {
                    dfs(i, j, d);
                    cnt++;
                }
            }
        }
        result = max(result, cnt);
    }
    cout << result << "\n";

    return 0;
}
