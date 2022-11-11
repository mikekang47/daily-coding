import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
q = deque()
q.append([a, 1])
while q:
    v, cnt = q.popleft()

    if v == b:
        print(cnt)
        sys.exit(0)

    if 1 <= v * 2 <= 10 ** 9:
        q.append([v * 2, cnt + 1])
    if 1 <= int(str(v) + "1") <= 10 ** 9:
        q.append([int(str(v) + "1"), cnt + 1])
print(-1)
