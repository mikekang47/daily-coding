import sys

n, k = map(int, sys.stdin.readline().split())
li = [sys.stdin.readline().split() for _ in range(n)]
li.sort(key=lambda x: (x[0], x[1]))
print(' '.join(li[k-1]))
