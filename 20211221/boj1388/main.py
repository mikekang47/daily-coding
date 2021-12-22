n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
cnt = 0
graph = [input() for _ in range(n)]

def dfs(row, col):
    visited[row][col] = True
    global cnt
    if graph[row][col] == '-':
        if 0 <= col+1 < m:
            if graph[row][col+1] == '-':
                dfs(row, col+1)
            else:
                cnt += 1
        else:
            cnt += 1
    else:
        if 0 <= row+1 < n:
            if graph[row+1][col] == '|':
                dfs(row+1, col)
            else:
                cnt += 1
        else:
            cnt += 1


for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i,j)

print(cnt)
