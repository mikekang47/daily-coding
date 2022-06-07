import sys

n = int(sys.stdin.readline())

li = [list(input()) for _ in range(n)]
visited = [[-1] * n] * n

print(visited)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
cnt = 0

def dfs(y, x, color):
    global cnt
    if li[y][x] != color:
        return True

    visited[y][x] = 1
    type = li[y][x]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or nx >= n or ny >= n or visited[ny][nx] == 1:
            continue
        dfs(ny,nx, type)
    return False


for i in range(len(li)):
    for j in range(len(li)):
        if not dfs(j, i, li[j][i]):
            cnt += 1


print(cnt)
