danji = []
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


cnt = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            danji.append(cnt)
            cnt = 0
print(len(danji))
for i in sorted(danji):
    print(i)
