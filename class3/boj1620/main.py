import sys

n, m = map(int, sys.stdin.readline().split())
d1 = {}
for i in range(1, n + 1):
    s = sys.stdin.readline()[:-1]
    d1[s] = i
    d1[str(i)] = s
for i in range(m):
    s = sys.stdin.readline()[:-1]
    print(d1[s])

