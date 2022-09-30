import sys

k, n = map(int, sys.stdin.readline().split())
li = [int(sys.stdin.readline()) for _ in range(k)]
hi = max(li)
lo = 1
while lo <= hi:
    mid = (lo + hi) // 2
    cnt = sum(i // mid for i in li)
    if cnt >= n:
        lo = mid + 1
    else:
        hi = mid-1
print(hi)
