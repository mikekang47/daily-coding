import sys

n, m = map(int, sys.stdin.readline().split())
d1 = {}
d2 = {}
for i in range(1, n + 1):
    s = sys.stdin.readline()[:-1]
    d1[s] = i
    d2[i] = s
for i in range(m):
    s = sys.stdin.readline()[:-1]
    try:
        print(d1[s])
    except:
        print(d2[int(s)])

