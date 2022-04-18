#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string number, int k) {
    while(k--) {
        int len = number.length();
        if(number.length() - k <= 1)
            break;
        for(int i = 0; i < number.size(); i++) {
            if(number[i] < number[i+1]) {
                number.erase(number.begin() + i);
                break;
            }
        }
        if(len == number.length()) {
            number.pop_back();
        }
    }

    return number;
}