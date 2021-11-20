n = int(input())

num = []
graph = []

for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

cnt = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            num.append(cnt)
            result += 1
            cnt = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])