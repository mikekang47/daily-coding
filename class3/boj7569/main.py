import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
li = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if li[i][j][k] == 1:
                q.append([i, j, k])
while len(q) != 0:
    z, y, x = q.popleft()
    for j in range(6):
        nz = dz[j] + z
        ny = dy[j] + y
        nx = dx[j] + x
        if (0 <= ny < n and 0 <= nx < m and 0 <= nz < h) and li[nz][ny][nx] == 0:
            li[nz][ny][nx] = li[z][y][x] + 1
            q.append([nz, ny, nx])

result = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if li[i][j][k] == 0:
                print(-1)
                sys.exit(0)
            if result < li[i][j][k]:
                result = li[i][j][k]
print(result - 1)
