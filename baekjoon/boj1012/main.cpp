#include <iostream>
#include <vector>

using namespace std;

int graph[51][51];
bool visited[51][51];
int dy[4] = {0, 0, 1, -1};
int dx[4] = {1, -1, 0, 0};

int t, m, n, k;

void dfs(int y, int x) {
    visited[y][x] = true;
    for (int i = 0; i < 4; i++) {
        int ny = dy[i] + y;
        int nx = dx[i] + x;
        if (ny >= 0 && ny < n && nx >= 0 && nx < m) {
            if (graph[ny][nx] == 1 && !visited[ny][nx]) {
                dfs(ny, nx);
            }
        }
    }
}


int main() {
    cin.tie(NULL); cout.tie(NULL);
    cin >> t;
    while (t--) {
        fill(&graph[0][0], &graph[0][0] + 51 * 51, 0);
        fill(&visited[0][0], &visited[0][0] + 51 * 51, 0);
        cin >> m >> n >> k;
        for (int j = 0; j < k; j++) {
            int y, x;
            cin >> x >> y;
            graph[y][x] = 1;
        }
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j] && graph[i][j] == 1) {
                    dfs(i, j);
                    cnt++;
                }
            }
        }
        cout << cnt << "\n";
    }
    return 0;
}
