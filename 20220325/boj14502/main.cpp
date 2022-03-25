#include <iostream>
#include <vector>

using namespace std;
int n, m;
vector<pair<int,int>> v;
int graph[8][8];
bool visited[8][8];

int dx[4]= {1, 0, -1, 0};
int dy[4]= {0, -1, 0, 1};

void dfs(int x, int y) {
    if(graph[x][y] == 1 || visited[x][y]) return;
    visited[x][y] = true;
    for(int i = 0; i < 4; i++) {
        int nx = dx[i] + x;
        int ny = dy[i] + y;
        if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
        dfs(nx, ny);
    }
}

int solve() {
    memset(visited, 0, sizeof(visited));
    for(int i = 0; i <n; i++) {
        for(int j = 0; j < m; j++) {
            if(graph[i][j] == 2) dfs(i,j);
        }
    }
    int result = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(!visited[i][j] && graph[i][j] == 0)
                result++;
        }
    }
    return result;
}

int main() {
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> graph[i][j];
            if(!graph[i][j]) v.push_back({i,j});
        }
    }
    int result = 0;
    for(int i = 0; i < v.size(); i++) {
        for(int j = 0; j < i; j++) {
            for(int k = 0; k < j; k++) {
                graph[v[i].first][v[i].second] = graph[v[j].first][v[j].second] = graph[v[k].first][v[k].second] = 1;
                result = max(result, solve());
                graph[v[i].first][v[i].second] = graph[v[j].first][v[j].second] = graph[v[k].first][v[k].second] = 0;
            }
        }
    }
    cout << result;
    return 0;
}
