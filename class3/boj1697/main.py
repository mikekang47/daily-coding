import sys

n, k = map(int, input().split())
visited = [False for _ in range(1000001)]
q = [n]
cnt = 0
while len(q) != 0:
    for i in range(len(q)):
        v = q.pop(0)
        if v == k:
            print(cnt)
            sys.exit(0)
        if not visited[v + 1] and 0 <= v + 1 <= 100000:
            visited[v + 1] = True
            q.append(v + 1)
        if not visited[v - 1] and 0 <= v - 1 <= 100000:
            visited[v - 1] = True
            q.append(v - 1)
        if not visited[2 * v] and 0 <= 2 * v <= 100000:
            visited[2*v] = True
            q.append(2*v)
    cnt += 1
