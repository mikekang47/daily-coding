import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    visited = ["" for _ in range(10001)]
    q = [a]
    s = ""
    while len(q) != 0:
        v = q.pop(0)

        if visited[(v * 2) % 10000] == "":
            q.append((v * 2) % 10000)
            visited[int((v * 2) % 10000)] = visited[v] + "D"
        if visited[v - 1 if v - 1 != 0 else 9999] == "":
            q.append(v - 1 if v - 1 != 0 else 9999)
            visited[v - 1 if v - 1 != 0 else 9999] = visited[v] + "S"

        l = deque(str(v))
        l.rotate(-1)

        if visited[int(''.join(list(l)))] == "":
            q.append(int(''.join(list(l))))
            visited[int(''.join(list(l)))] = visited[v] + "L"
        l.rotate(2)
        if visited[int(''.join(list(l)))] == "":
            q.append(int(''.join(list(l))))
            visited[int(''.join(list(l)))] = visited[v] + "R"
        if v == b:
            break
    print(visited[b])
