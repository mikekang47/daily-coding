N, M = map(int, input().split())

brd = [input() for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt = 0


def dfs(i, j):
    global cnt
    visited[i][j] = 1
    if brd[i][j] == '-':
        if 0 <= j+1 < M:
            if brd[i][j+1] == '-':
                dfs(i, j+1)
            else:
                cnt += 1
        else:
            cnt += 1
    else:
        if 0 <= i+1 < N:
            if brd[i+1][j] == '|':
                dfs(i+1, j)
            else:
                cnt += 1
        else:
            cnt += 1


for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            dfs(i, j)

print(cnt)