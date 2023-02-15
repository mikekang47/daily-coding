n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
result = []
def dfs(start):
    visited[start] = True
    result.append(start)
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

def bfs(start):
    q = [start]
    visited[start] = True
    while len(q) != 0:
        t = q.pop(0)
        result.append(t)
        for i in graph[t]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])

dfs(v)
print(*result)
result = []
visited = [False for _ in range(n+1)]
bfs(v)
print(*result)