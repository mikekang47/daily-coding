from heapq import heappush, heappop
import sys
n = int(sys.stdin.readline())
h = []
for _ in range(n):
    heappush(h, int(input()))
result = 0
while len(h) != 1:
    a = heappop(h)
    b = heappop(h)
    result += a + b
    heappush(h, a + b)
print(result)