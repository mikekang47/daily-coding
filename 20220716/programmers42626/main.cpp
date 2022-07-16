#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    int food = 0;
    priority_queue<int, vector<int>, greater<>> pq;
    for(auto i : scoville) {
        pq.push(i);
    }
    while(pq.top() < K) {
        if(pq.size() < 2)
            return -1;
        food += pq.top();
        pq.pop();
        food += 2 * pq.top();
        pq.pop();
        pq.push(food);
        food = 0;
        answer++;
    }
    return answer;
}

int main() {
//    vector<int> scoville = {1, 2, 3, 9, 10, 12};
//    int  K = 7;
q
}