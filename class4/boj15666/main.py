from itertools import product,combinations_with_replacement

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for i in sorted(list(set(list(combinations_with_replacement(arr, m))))):
    print(*i)
