n,m = map(int, input().split())
s = set(input() for _ in range(n))
s2 = set(input() for _ in range(m))
print(len(s.intersection(s2)))
for i in sorted(s.intersection(s2)):
    print(i)
