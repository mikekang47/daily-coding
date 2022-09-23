#include <iostream>
#include <stack>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;


int n, m, v;
bool dfsVisited[1001];
bool bfsVisited[1001];

vector<int> graph[1001];

void dfs(int start) {
    stack<int> st;
    st.push(start);

    while (!st.empty()) {
        int vertex = st.top();
        st.pop();

        if (!dfsVisited[vertex]) {
            dfsVisited[vertex] = true;
            cout << vertex << ' ';
        }

        for (int i = graph[vertex].size() - 1; i >= 0; i--) {
            int next = graph[vertex][i];
            if (!dfsVisited[next]) {
                st.push(next);
            }
        }

    }
    cout << "\n";
}

void bfs(int start) {
    queue<int> q;
    q.push(start);

    while (!q.empty()) {
        int vertex = q.front();
        q.pop();

        if (!bfsVisited[vertex]) {
            bfsVisited[vertex] = true;
            cout << vertex << ' ';
        }
        for (int next : graph[vertex]) {
            if (!bfsVisited[next])
                q.push(next);
        }
    }
    cout << "\n";
}


int main() {
    cin >> n >> m >> v;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    for (int i = 0; i <= n; i++) {
        sort(graph[i].begin(), graph[i].end());
    }
    dfs(v);
    bfs(v);
    return 0;
}
