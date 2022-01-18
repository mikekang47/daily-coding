h, w = map(int, input().split())
graph = []
for i in range(h):
    graph.append(list(input()))
cloud = []
for y in range(h):
    idx = None
    temp = []
    for x in range(w):
        if graph[y][x] == 'c':
            temp.append(0)
            idx = x
        else:
            if idx != None:
                temp.append(x-idx)
            else:
                temp.append(-1)
    cloud.append(temp)

for row in cloud:
    for col in row:
        print(col, end=' ')
    print()