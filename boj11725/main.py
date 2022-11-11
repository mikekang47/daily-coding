import sys
from collections import deque


def bfs(n: int, li):
    q = deque([1])
    parent = [0] * (n + 1)
    while q:
        v = q.popleft()
        for i in li[v]:
            if parent[i] == 0 and i != 1:
                parent[i] = v
                q.append(i)
    for i in range(2, n + 1):
        print(parent[i])


n = int(sys.stdin.readline())
li = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    li[a].append(b)
    li[b].append(a)

bfs(n, li)
