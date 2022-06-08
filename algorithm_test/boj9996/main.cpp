#include <iostream>
#include <vector>

using namespace std;
int n;
string s;

int main() {
    cin >> n;
    cin >> s;
    int index = s.find("*");
    string front = s.substr(0, index);
    string back = s.substr(index+1);
    for(int i = 0; i < n; i++) {
        string temp;
        cin >> temp;
        if(front.size() + back.size() > temp.size())
            cout << "NE" << "\n";
        else {
            if(front == temp.substr(0, front.size()) && back == temp.substr(temp.size() - back.size())) {
                cout << "DA\n";
            } else {
                cout << "NE\n";
            }
        }

    }
    return 0;
}
