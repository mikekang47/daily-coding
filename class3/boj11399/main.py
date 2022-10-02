from itertools import accumulate

n = int(input())
li = list(map(int, input().split()))
li.sort()
print(sum(accumulate(li)))