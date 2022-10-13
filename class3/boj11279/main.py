from heapq import *
import sys
n = int(sys.stdin.readline())
arr = []

for i in range(n):
    temp = int(sys.stdin.readline())
    if temp == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-heappop(arr))
    else:
        heappush(arr, -temp)

