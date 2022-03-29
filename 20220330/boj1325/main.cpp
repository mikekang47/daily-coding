#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n, m, mx;
vector<int> v[10004];
int dp[10004];
int visited[10004];

int dfs(int start) {
    visited[start] = 1;
    int answer = 1;
    for(int next : v[start]) {
        if(visited[next]) continue;
        answer += dfs(next);
    }
    return answer;
}

int main() {
    cin >> n >> m;
    for(int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        v[b].push_back(a);
    }

    for(int i = 1; i <=n; i++) {
        memset(visited, 0, sizeof(visited));
        dp[i] = dfs(i);
        mx = max(dp[i], mx);
    }
    for(int i = 1; i <= n; i++) {
        if(mx == dp[i])
            cout << i << " ";
    }


    return 0;
}
