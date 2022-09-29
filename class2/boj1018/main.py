n, m = map(int, input().split())
li = [list(input().strip()) for i in range(n)]
ans = n * m
WB = ["W", "B"]

for i in range(n):
    for j in range(m):
        li[i][j] = (li[i][j] == WB[(i + j) % 2])

for i in range(n - 7):
    for j in range(m - 7):
        a = sum([sum(li[k][j:j + 8]) for k in range(i, i + 8)])
        a = min(a, 64 - a)
        ans = min(ans, a)
print(ans)
