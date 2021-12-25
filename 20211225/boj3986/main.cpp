#include <iostream>
#include <string>
#include <algorithm>
#include <stack>
using namespace std;
int n, cnt;
string s;
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> s;
        stack<char> st;
        for(auto c : s) {
            if(st.size() && st.top() == c)
                st.pop();
            else
                st.push(c);
        }
        if(!st.size())
            cnt++;
    }
    cout << cnt;
    return 0;
}
