#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;
int n;
vector<string> arr;

bool compare(string &a, string &b) {
    if (a.length() == b.length()) {
        return a < b;
    } else {
        return a.length() < b.length();
    }
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        arr.push_back(s);
    }
    set<string> sets(arr.begin(), arr.end());
    vector<string> v(sets.begin(), sets.end());
    sort(v.begin(), v.end(), compare);
    for (const string &s: v) {
        cout << s << "\n";
    }
    return 0;
}
