#include <iostream>

using namespace std;
int n, m;
int graph[9][9];
int visited[9][9];

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> graph[i][j];
        }
    }
    return 0;
}
