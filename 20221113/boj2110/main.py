import sys

n, c = map(int, sys.stdin.readline().split())
x = []
for _ in range(n):
    x.append(int(sys.stdin.readline()))
x.sort()

minReach = 1
maxReach = x[-1] - x[0]
answer = 0
while minReach <= maxReach:
    mid = (minReach + maxReach) // 2
    cur = x[0]
    cnt = 1
    for i in range(1, n):
        if x[i] - cur >= mid:
            cnt += 1
            cur = x[i]

    if cnt < c:
        maxReach = mid - 1
    elif cnt >= c:
        answer = mid
        minReach = mid + 1
print(answer)
