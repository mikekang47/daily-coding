one = 0
zero = 0


def slicing(x, y, height):
    s = graph[y][x]
    global one
    global zero
    for i in range(y, y + height):
        for j in range(x, x + height):
            if graph[i][j] != s:
                slicing(x, y, height // 2)
                slicing(x + height // 2, y, height // 2)
                slicing(x, y + height // 2, height // 2)
                slicing(x + height // 2, y + height // 2, height // 2)
                return
    if s == 1:
        one += 1
    else:
        zero += 1


n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

slicing(0, 0, n)
print(zero)
print(one)
