import sys

sys.setrecursionlimit(100000)
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
cnt = 0


def dfs(x, y):
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0 <= ny <= n and 0 <= nx <= n and not visited[ny][nx]:
            temp = abs(arr[y][x] - arr[ny][nx])
            if l <= temp <= r:
                visited[ny][nx] = True
                st.append([ny, nx])
                dfs(ny, nx)


while True:
    flag = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            st = []
            if not visited[i][j]:
                st.append([i, j])
                dfs(i, j)
                if len(st) > 1:
                    flag = True
                    avg = sum([arr[y][x] for y, x in st]) // len(st)
                    for y, x in st:
                        arr[y][x] = avg
    if not flag:
        break
    cnt += 1

print(cnt)
