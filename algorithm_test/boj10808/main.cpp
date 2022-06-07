#include <iostream>
using namespace std;

int alpha[26] = {0,};
int main() {
    string s;
    cin >> s;
    for(char i : s) {
        alpha[i -'a']++;
    }
    for(int a : alpha) {
        cout << a << ' ';
    }
    return 0;
}
