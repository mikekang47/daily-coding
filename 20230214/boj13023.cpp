#include <iostream>
#include <vector>
#include <memory.h>
using namespace std;
int n, m, a, b;
vector<int> v[2001];
bool visited[2001];
bool arrive;

void dfs(int start, int depth) {
    if(depth == 5 || arrive) {
        arrive = true;
        return;
    }
    visited[start] = true;
    for(int i = 0; i < v[start].size(); i++) {
        int y = v[start][i];
        if(!visited[y]) {
            dfs(y, depth + 1);
        }
    }
    visited[start] = false;
}
int main()
{
    cin >> n >> m;
    v->resize(n+1);
    memset(visited, 0, sizeof(visited));
    for (int i = 0; i < m; i++)
    {
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    for(int i = 0; i < n; i++) {
        dfs(i, 1);
        if(arrive) {
            cout << 1;
            return 0;
        }
    }
    cout << 0;
    return 0;
}