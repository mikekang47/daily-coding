n, m = map(int, input().split())
li = [int(input()) for _ in range(n)]
cnt = 0
while m != 0:
    if m / li[-1] > 0:
        cnt += m // li[-1]
        m = m % li[-1]
        li.pop(-1)
print(cnt)
