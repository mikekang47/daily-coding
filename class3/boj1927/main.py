import sys
import heapq

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    command = int(sys.stdin.readline())
    if command == 0:
        if len(li) == 0:
            print(0)
        else:
            print(heapq.heappop(li))
    else:
        heapq.heappush(li, command)
