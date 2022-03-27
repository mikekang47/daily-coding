#include <iostream>
#include <vector>
using namespace std;
int n, temp, root, r;
vector<int> v[54];

int dfs(int top) {
    int answer = 0;
    int leaf = 0;
    for(int node : v[top]) {
        if(node == r) continue;
        answer += dfs(node);
        leaf++;
    }
    if(leaf == 0) return 1;
    return answer;
}

int main() {
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> temp;
        if(temp == -1) root = i;
        else
            v[temp].push_back(i);
    }

    cin >> r;

    if(r == root) {
        cout << 0 << "\n";
        return 0;
    } else {
        cout << dfs(root) << "\n";
    }
}