import sys

def check(num):
    cnt = 0
    for i in li:
        cnt += i // num
    return cnt

k, n = map(int, sys.stdin.readline().split())
li = [int(sys.stdin.readline()) for _ in range(k)]
li.sort()
hi = li[-1]
lo = 1
mid = 99999
result = 0
while lo <= hi:
    mid = (lo+hi) // 2
    if check(mid) < n:
        hi = mid - 1
    else:
        if result < mid:
            result = mid
        lo = mid + 1
print(result)