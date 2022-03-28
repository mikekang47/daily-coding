#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;
deque<int> dq;
int n, m;

int main() {
    cin >> n >> m;
    for(int i = 0; i< n; i++) {
        int temp;
        cin >> temp;
        dq.push_back(temp);
    }

    return 0;
}
