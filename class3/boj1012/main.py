import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

sys.setrecursionlimit(10**6)
def dfs(y, x):
    visited[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and graph[ny][nx] == 1:
            dfs(ny, nx)


t = int(input())

for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j)
                cnt += 1

    print(cnt)
# print(graph)
