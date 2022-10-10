import sys

dy = [-1, 0, 1, 0, 0]
dx = [0, 1, 0, -1, 0]

n, k = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(k):
    y, x = map(int, sys.stdin.readline().split())
    for i in range(5):
        ny = dy[i] + y - 1
        nx = dx[i] + x - 1
        if 0 <= ny < n and 0 <= nx < n:
            graph[ny][nx] += 1

print(sum(sum(graph, [])))
