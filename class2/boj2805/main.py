n, m = map(int, input().split())
li = list(map(int, input().split()))
hi = max(li)
lo = 1
while lo <= hi:
    mid = (lo + hi) // 2
    result = sum(i - mid for i in li if i - mid > 0)
    if result < m:
        hi = mid - 1
    else:
        lo = mid + 1
print(hi)