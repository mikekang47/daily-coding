n, m = map(int, input().split())
s = set([input() for _ in range(n)])
# print(s)
cnt = 0
for i in range(m):
    p = input()
    if p in s:
        cnt += 1
print(cnt)