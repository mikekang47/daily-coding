cnt = 0

def dfs(n: int):
    visited[n] = True
    global cnt
    for e in range(len(graph[n])):
        nextElement = graph[n][e]
        if not visited[nextElement]:
            # print(nextElement)
            dfs(nextElement)
            cnt += 1


n = int(input())
pair = int(input())
graph = []
for _ in range(n + 1):
    graph.append([])

for i in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited = [False] * (n + 1)
dfs(1)
print(cnt)