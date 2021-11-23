import sys

n = int(input())
graph = []
visited = [[False] * n for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))
visited[0][0] = True

def dfs(x, y):
    num = graph[x][y]
    if num == -1:
        print("HaruHaru")
        sys.exit()

    if num + x < n and visited[num+x][y] != True:
        visited[num+x][y] = True
        dfs(num+x,y)

    if y+num < n and visited[x][y+num] != True:
        visited[x][y+num] = True
        dfs(x, y+num)



dfs(0,0)
print("Hing")


