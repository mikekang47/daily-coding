#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int bfs(int a, int b, vector<int> cost, int n) {
    queue<int> q;
    q.push(a-1);
    vector<int> visited(n, -1);
    visited[a-1] = 0;
    while(!q.empty()) {
        int node = q.front();
        q.pop();
        for(int i = 0; i < n; i++) {
            if((i - node) % cost[node] == 0 && visited[i] == -1) {
                q.push(i);
                visited[i] = visited[node] + 1;
                if(i  == b-1) {
                     return visited[i];
                }
            }
        }
    }
    return -1;
}


int main() {
    int n;
    cin >> n;
    vector<int> cost;
    for(int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        cost.push_back(temp);
    }
    int a, b;
    cin >> a >> b;
    cout << bfs(a, b, cost, n);
    return 0;
}
