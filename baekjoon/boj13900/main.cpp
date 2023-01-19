#include <iostream>
#include <stack>

using namespace std;
stack<long long> st;
long long n, sum, result;

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        st.push(temp);
    }
    sum = st.top();
    st.pop();
    while (!st.empty()) {
        int current = st.top();
        st.pop();
        result += sum * current;
        sum += current;
    }
    cout << result << "\n";

    return 0;
}
