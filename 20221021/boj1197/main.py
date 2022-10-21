v, e = map(int, input().split())
p = [i for i in range(v + 1)]


def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]


def union(p, a, b):
    a = find(p, a)
    b = find(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


graph = [list(map(int, input().split())) for _ in range(e)]
result = 0

graph.sort(key=lambda x: (x[2]))

for a, b, cost in graph:
    if find(p, a) != find(p, b):
        union(p, a, b)
        result += cost

print(result)
