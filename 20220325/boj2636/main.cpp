#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, m, cnt, cnt2, a[104][104];
int visited[104][104];
int dx[4] = {-1 ,0 ,1, 0};
int dy[4] = {0 ,1 ,0, -1};

vector<pair<int, int>> v;

void dfs(int y, int x) {
    if(a[y][x] == 1) {
        v.push_back({y,x});
        return;
    }

    for(int i = 0; i < 4; i++) {
        int nx = dx[i] + x;
        int ny = dy[i] + y;
        if(nx < 0 || nx >= m || ny < 0 || ny >= n || visited[ny][nx]) continue;
        visited[ny][nx] = true;
        dfs(ny, nx);
    }
}

int main() {
    cnt = 0;
    cnt2 = 0;
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> a[i][j];
        }
    }

    while(true) {
        cnt2 = 0;
        fill(&visited[0][0], &visited[0][0] + 104*104, 0);
        v.clear();

        dfs(0,0);
        for(pair<int, int>b : v) {
            if(a[b.first][b.second] == 1) cnt2++;
        }

        for(pair<int, int>b : v) {
            a[b.first][b.second] = 0;
        }
        cnt++;
        bool flag = false;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(a[i][j] != 0) flag = true;
            }
        }
        if(!flag)
            break;
    }
    cout << cnt << "\n";
    cout << cnt2<<"\n";


    return 0;
}
