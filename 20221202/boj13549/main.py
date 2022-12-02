from collections import deque

def bfs():
    q = deque()
    q.append(n)
    dist[n] = 0
    while q:
        x = q.pop()
        if x == k:
            print(dist[x])
            return
        for nx in (x*2, x-1, x+1):
            if 0 <= nx <= MAX and dist[nx] == -1:
                if nx == x*2:
                    q.append(nx)
                    dist[nx] = dist[x]
                else:
                    q.appendleft(nx)
                    dist[nx] = dist[x]+1

MAX = 100000
n, k = map(int, input().split())
dist = [-1]*(MAX+1)
bfs()