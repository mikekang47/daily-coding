#include <iostream>
#include <string>

using namespace std;

int main() {
    string s, t, ret;
    cin >> s >> t;
    for (char a: s) {
        ret += a;
        if (ret.size() >= t.size() && ret.substr(ret.size() - t.size(), t.size()) == t) {
            ret.erase(ret.end() - t.size(), ret.end());
        }
    }
    if(ret.empty()) {
        cout << "FRULA" << endl;
    } else {
        cout << ret << "\n";
    }
    return 0;
}
