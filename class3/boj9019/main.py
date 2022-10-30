import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    visited = [False for _ in range(10001)]
    q = deque()
    q.append((a, ""))
    while len(q) != 0:
        v, s = q.popleft()
        if v == b:
            print(s)
            break

        temp = (v * 2) % 10000
        if not visited[temp]:
            q.append((temp, s + "D"))
            visited[temp] = True

        temp = v - 1 if v != 0 else 9999
        if not visited[temp]:
            q.append((temp, s + "S"))
            visited[temp] = True

        temp = (v % 1000) * 10 + (v // 1000)
        if not visited[temp]:
            q.append((temp, s + "L"))
            visited[temp] = True

        temp = (v % 10) * 1000 + (v // 10)
        if not visited[temp]:
            q.append((temp, s + "R"))
            visited[temp] = True
