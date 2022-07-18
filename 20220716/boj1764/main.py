from collections import defaultdict
n, m = map(int, input().split())
d = set()
d2 = set()
for _ in range(n):
    d.add(input())
for _ in range(m):
    d2.add(input())


li = sorted(list(d.intersection(d2)))
print(len(li))
for i in li:
    print(i)





