import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
if m == 1:
    [print(i) for i in arr]
else:
    for i in list(permutations(arr, m)):
        print(*i)
