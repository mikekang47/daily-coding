import heapq
import sys

n, k = map(int, sys.stdin.readline().split())
li = []
for _ in range(n):
    li.append(tuple(map(int, sys.stdin.readline().split())))
li = sorted(li, reverse=True)
bags = sorted([int(sys.stdin.readline()) for _ in range(k)])
result = 0
q = []
for bag in bags:
    while li and li[-1][0] <= bag:
        heapq.heappush(q, -li.pop()[1])
    if q:
        result -= heapq.heappop(q)
print(result)
