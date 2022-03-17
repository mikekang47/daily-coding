#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int arr[104][104];
queue<pair<int,int>> q;
int n, m, y, x;
int visited[104][104];
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};


int main() {
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            scanf("%1d",&arr[i][j]);
        }
    }

    q.push({0,0});
    visited[0][0] = true;

    while(!q.empty()) {
        tie(y,x) = q.front();
        q.pop();

        for(int i = 0; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if(ny < 0 || ny >= n || nx < 0 || nx >= m || arr[ny][nx] == 0) continue;
            if(visited[ny][nx]) continue;
            visited[ny][nx] = visited[y][x] + 1;
            q.push({ny,nx});
        }
    }

    printf("%d", visited[n-1][m-1]);
    return 0;
}
