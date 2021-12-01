import sys
from collections import defaultdict

n = int(sys.stdin.readline().strip())
x = defaultdict(int)
y = defaultdict(int)
for i in range(n):
    front, back = map(int, sys.stdin.readline().strip().split())
    x[front] += 1
    y[back] += 1
cnt = 0
for i in x.keys():
    if x[i] >= 2:
        cnt += 1
for i in y.keys():
    if y[i] >= 2:
        cnt += 1
print(cnt)
