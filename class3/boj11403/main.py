n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            graph[j][k] |= graph[j][i] & graph[i][k]

for x in graph:
    for y in x:
        print(y,end=" ")
    print()