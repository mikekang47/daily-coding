#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n, m;
vector<int> datas;
vector<int> objects;

int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        datas.push_back(temp);
    }
    cin >> m;
    for (int i = 0; i < m; i++)
    {
        int temp;
        cin >> temp;
        objects.push_back(temp);
    }
    sort(datas.begin(), datas.end());
    for (int i = 0; i < m; i++)
    {
        int temp = objects[i];
        cout << binary_search(datas.begin(), datas.end(), temp) << "\n";
    }
}