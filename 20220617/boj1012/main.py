import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
T = int(input())

def bfs(x,y):
    if 0 <= x < N and 0 <= y < M and graph[x][y]:
        graph[x][y] = 0

        bfs(x+1,y)
        bfs(x,y+1)
        bfs(x-1,y)
        bfs(x,y-1)

for _ in range(T):
    N, M, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                bfs(i,j)
                cnt += 1

    print(cnt)