n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
q = [[0,0]]
graph[0][0] = 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    x, y = q[0][0], q[0][1]
    q.pop(0)
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            q.append([nx,ny])
print(graph[n-1][m-1])

