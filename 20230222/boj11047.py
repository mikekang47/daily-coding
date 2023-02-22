n, k = map(int, input().split())
li = [int(input()) for _ in range(n)]
cnt = 0
li.sort()
li.reverse()
for i in li:
    if k >= i:
        cnt += k // i
        k = k % i
print(cnt)
    