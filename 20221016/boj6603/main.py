import sys
from itertools import combinations
while 1:
    li = list(map(int, input().split()))
    if li[0] == 0:
        sys.exit(0)
    li.pop(0)
    for i in list(combinations(li,6)):
        print(*i)
    print()
