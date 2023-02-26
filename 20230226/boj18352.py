import sys
from collections import deque
n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int , sys.stdin.readline().rstrip().split())
    graph[a].append(b)

visited = [-1 for _ in range(n+1)]
q = deque()
q.append(x)
visited[x] += 1 
while len(q) != 0:
    v = q.popleft()
    for nx in graph[v]:
        if visited[nx] == -1:
            visited[nx] = visited[v] + 1
            q.append(nx)
            
flag = False
for i in range(n+1):
    if visited[i] == k:
        print(i)   
        flag = True
        
if flag == False:
    print(-1)
        
    