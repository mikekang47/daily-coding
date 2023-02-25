import sys
import heapq

sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
degree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    
    degree[b] += 1
    graph[a].append(b)

q = []
    

for i in range(1, n+1):
    if degree[i] == 0:
        heapq.heappush(q, i)

while q:
    num = heapq.heappop(q)
    print(num, end=" ")
    
    for i in graph[num]:
        degree[i] -= 1
        
        if degree[i] == 0:
            heapq.heappush(q,i)
    
            
