#include <iostream>
#include <string>
using namespace std;
char mid;
int flag;
int alpha[200];
string input, ret;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> input;
    for(char i : input) {
        alpha[i]++;
    }
    for(int i = 'Z'; i >= 'A'; i--) {
        if(alpha[i]) {
            if(alpha[i] & 1) {
                mid = char(i);
                flag++;
                alpha[i]--;
            }
            if(flag == 2)break;
            for(int j = 0; j < alpha[i]; j += 2) {
                ret = char(i) + ret;
                ret += char(i);
            }
        }

    }
    if(mid) ret.insert(ret.begin() + ret.size() / 2, mid);
    if(flag == 2) cout << "I'm Sorry Hansoo\n";
    else cout << ret << "\n";
    return 0;
}
