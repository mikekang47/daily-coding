import sys
from collections import deque


def bfs(a, b, cost, n):
    q = deque()
    q.append(a-1)
    visited = [-1] * n
    visited[a-1] = 0
    while q:
        node = q.popleft()
        for i in range(n):
            if (i-node) % cost[node] == 0 and visited[i] == -1:
                q.append(i)
                visited[i] = visited[node] + 1
                if i == b-1:
                    return visited[i]
    return -1


n = int(input())
cost = list(map(int, input().split()))
a, b = map(int, input().split())
cnt = 1
print(bfs(a, b, cost, n))
