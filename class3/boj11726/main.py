n = int(input())
li = [0 for _ in range(10001)]
li[1] = 1
li[2] = 2
for i in range(3, n+1):
    li[i] = li[i-1] + li[i-2]
print(li[n] % 10007)