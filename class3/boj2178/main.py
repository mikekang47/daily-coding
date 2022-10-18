n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

visited[0][0] = 1
q = [[0, 0]]

while len(q) != 0:
    y, x = q[0][0], q[0][1]
    q.pop(0)
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1 and not visited[ny][nx]:
            visited[ny][nx] = visited[y][x] + 1
            q.append([ny, nx])
print(visited[n-1][m-1])
