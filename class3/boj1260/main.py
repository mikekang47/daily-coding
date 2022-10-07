visited = [False for _ in range(1004)]
d = []
def dfs(start):
    visited[start] = True
    d.append(start)
    for i in range(len(graph[start])):
        nex = graph[start][i]
        if not visited[nex]:
            dfs(nex)

bf = []
def bfs(start):
    q = [start]

    while len(q) != 0:
        v = q.pop(0)

        if not visited[v]:
            visited[v] = True
            bf.append(v)
        for i in range(len(graph[v])):
            nex = graph[v][i]
            if not visited[nex]:
                q.append(nex)

n, m, v = map(int, input().split())
graph = [[] for _ in range(1004)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(len(graph)):
    graph[i].sort()

dfs(v)
print(*d)
visited = [False for _ in range(1004)]
bfs(v)
print(*bf)