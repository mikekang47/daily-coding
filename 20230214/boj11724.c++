#include <iostream>
#include <vector>
using namespace std;
int n, m, a, b;
vector<int> v[1001];
bool visited[1001];

void dfs(int start)
{
    if (visited[start])
        return;
    visited[start] = true;
    for (int i = 0; i < v[start].size(); i++)
    {
        if (!visited[v[start][i]])
        {
            dfs(v[start][i]);
        }
    }
}
int main()
{
    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    int cnt = 0;
    for (int i = 1; i <= n; i++)
    {
        if (!visited[i])
        {
            dfs(i);
            cnt += 1;
        }
    }
}