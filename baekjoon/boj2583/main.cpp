#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int m, n, k, cnt;
int graph[101][101];
int visited[101][101];
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};

void dfs(int y, int x) {
    visited[y][x] = 1;
    for (int i = 0; i < 4; i++) {
        int ny = dy[i] + y;
        int nx = dx[i] + x;
        if (0 <= ny && ny < m && 0 <= nx && nx < n) {
            if (graph[ny][nx] == 0 && visited[ny][nx] == 0) {
                dfs(ny, nx);
                cnt += 1;
            }
        }
    }
}

int main() {
    cin >> m >> n >> k;
    for (int d = 0; d < k; d++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        for (int i = y1; i < y2; i++) {
            for (int j = x1; j < x2; j++) {
                graph[i][j] = 1;
            }
        }
    }
    vector<int> area;
    int result = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (visited[i][j] == 0 && graph[i][j] == 0) {
                dfs(i, j);
                result++;
                area.push_back(cnt);
                cnt = 0;
            }
        }
    }
    cout << result << "\n";
    sort(area.begin(), area.end());
    for (int i = 0; i < area.size(); i++) {
        cout << area[i] + 1<< " ";
    }
    return 0;
}
