import sys

m, n = map(int, input().split())
q = []
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])

while not len(q) == 0:
    y = q[0][0]
    x = q[0][1]
    q.pop(0)
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if (0 <= nx < m and 0 <= ny < n) and graph[ny][nx] == 0:
            graph[ny][nx] = graph[y][x] + 1
            q.append([ny, nx])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            sys.exit(0)
        if result < graph[i][j]:
            result = graph[i][j]

print(result - 1)