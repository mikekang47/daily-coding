import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A, B = A-1, B-1
    graph[A].append(B)
    graph[B].append(A)

res = []
for i in range(N):
    queue = [i]
    visited = [0]*N
    visited[i] = 1
    while queue:
        idx = queue.pop(0)
        for j in graph[idx]:
            if not visited[j]:
                visited[j] = visited[idx]+1
                queue.append(j)
    res.append([sum(visited)-N, i+1])
print(sorted(res)[0][1])