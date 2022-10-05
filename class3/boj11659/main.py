from itertools import accumulate
import sys
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
arr = list(accumulate(li))
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a == 1:
        print(arr[b-1])
    else:
        print(arr[b-1] - arr[a-2])

