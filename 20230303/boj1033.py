from math import lcm, gcd


class Node:
    def __init__(self, b: int, p: int, q: int):
        self.b = b
        self.p = p
        self.q = q


n = int(input())
graph = [[] for _ in range(n+1)]
result = [0] * (n+1)
visited = [False] * (n+1)

l = 1


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        next = i.b
        if not visited[next]:
            result[next] = result[v] * i.q // i.p
            dfs(next)


for _ in range(n-1):
    a, b, p, q = map(int, input().split())
    graph[a].append(Node(b, p, q))
    graph[b].append(Node(a, q, p))
    l *= lcm(p, q)

result[0] = l
dfs(0)
g = result[0]
for i in range(1, n+1):
    g = gcd(g, result[i])

for i in range(0, n):
    print(result[i] // g, end=' ')
