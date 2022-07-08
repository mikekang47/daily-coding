import sys

m, n = map(int, sys.stdin.readline().split())
li = [True for _ in range(n+1)]
li[1] = False
for i in range(2, n + 1):
    if li[i]:
        for j in range(2*i, n+1, i):
            li[j] = False

for i in range(m, n+1):
    if li[i]:
        print(i)


