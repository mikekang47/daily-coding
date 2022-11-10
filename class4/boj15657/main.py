import sys
from itertools import combinations_with_replacement
from collections import defaultdict

dic = defaultdict(int)
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
perm = list(combinations_with_replacement(arr, m))
if n == 1:
    [print(i) for i in arr]
else:
    for i in perm:
        print(*i)
