from itertools import combinations
num = 0
n, m = map(int, input().split())
li = list(map(int, input().split()))
for x in map(sum, combinations(li, 3)):
    if x <= m:
        num = max(x, num)
print(num)