#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;
char graph[65][65];
string s;

string quard(int y, int x, int size) {
    if (size == 1) {
        return string(1, graph[y][x]);
    }
    char b = graph[y][x];
    string ret = "";
    for (int i = y; i < y + size; i++) {
        for (int j = x; j < x + size; j++) {
            if (b != graph[i][j]) {
                ret += "(";
                ret += quard(y, x, size / 2);
                ret += quard(y, x + size / 2, size / 2);
                ret += quard(y + size / 2, x, size / 2);
                ret += quard(y + size / 2, x + size / 2, size / 2);
                ret += ")";
                return ret;
            }
        }
    }
    return string(1, graph[y][x]);
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> s;
        for (int j = 0; j < n; j++) {
            graph[i][j] = s[j];
        }
    }
    cout << quard(0, 0, n) << "\n";

    return 0;
}
