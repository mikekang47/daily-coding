#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    priority_queue<int, vector<int>, greater<>> pq;
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        int value;
        scanf("%d", &value);
        if(value == 0) {
            if(pq.empty()) {
                cout << "0\n";
            } else {
                printf("%d\n", pq.top());
                pq.pop();
            }
        } else {
            pq.push(value);
        }
    }
}
