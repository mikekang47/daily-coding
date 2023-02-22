#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int v, from, to, value;
vector<pair<int, int>> graph[100001];
int visited[][100001];
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> v;
    for (int i = 0; i < v; i++)
    {
        cin >> from;
        while (1)
        {
            cin >> to;
            if (to == -1)
            {
                break;
            }
            cin >> value;
            graph[from].push_back({to, value});
        }
    }
    queue<int> q;
    q.push(1);
    while (!q.empty())
    {
        int node = q.front();
        q.pop();
        for (auto n : graph[node])
        {
            pair<int, int> object = n;
            
        }
    }
}