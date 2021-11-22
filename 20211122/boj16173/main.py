n = int(input())
graph = [[0]]
visited = [[False]]
for i in range(n):
    graph.append(list(map(int, input().split())))
    visited.append([False] * n)


def dfs(x, y):
    if x >= n or y >= n:
        return False

    if visited[x][y]:
        return False

    if graph[x][y] == -1:
        return True
    else:
        visited[x][y] = True
        dfs(x + graph[x][y], y)
        dfs(x, y + graph[x][y])


if dfs(1, 1):
    print("HaruHaru")
else:
    print("Hing")
