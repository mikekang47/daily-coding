n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

visited = [0 for _ in range(n+1)]

q = [1]
while len(q) != 0:
    v = q.pop(0)
    for i in graph[v]:
        # print(i)
        if visited[i] == 0:
            q.append(i)
            visited[i] += visited[v] + 1
# print(visited)
if 0 < visited[n] <= k:
    print("YES")
else:
    print("NO")