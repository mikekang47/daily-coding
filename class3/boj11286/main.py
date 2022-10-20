import heapq
t = int(input())
q = []
for _ in range(t):
    t = int(input())
    if t != 0:
        heapq.heappush(q,(abs(t),t))
    else:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
