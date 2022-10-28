import sys

sys.setrecursionlimit(10 ** 6)
n = int(input())
li = [input() for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
am_visited = [[False for _ in range(n)] for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def color_dfs(y: int, x: int, color: str):
    visited[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and li[ny][nx] == color:
            color_dfs(ny, nx, color)


def amblyopia_dfs(y, x, color):
    am_visited[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and not am_visited[ny][nx] and li[ny][nx] == color:
            amblyopia_dfs(ny, nx, color)


cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            color_dfs(i, j, li[i][j])
            cnt += 1

result = [cnt]
cnt = 0
for i in range(n):
    li[i] = li[i].replace("R", "G")

for i in range(n):
    for j in range(n):
        if not am_visited[i][j]:
            amblyopia_dfs(i, j, li[i][j])
            cnt += 1
result.append(cnt)
print(*result)
