#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;
int n, m;
vector<long long> v1;
inline std::string& rtrim(std::string& s, const char* t = " \t\n\r\f\v")
{
    s.erase(s.find_last_not_of(t) + 1);
    return s;
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        long long temp;
        cin >> temp;
        v1.push_back(temp);
    }
    for (int i = 0; i < m; i++) {
        long long temp;
        cin >> temp;
        v1.push_back(temp);
    }
    sort(v1.begin(), v1.end());
    string s;
    for (auto i: v1) {
        s += to_string(i);
        s += " ";
    }
    cout << rtrim(s);
    return 0;
}
