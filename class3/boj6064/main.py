t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    cnt = -1
    while x <= m *n:
        if x % n == y % n:
            cnt = x
            break
        x += m
    print(cnt)


