t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    dp = [x for x in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            dp[j] += dp[j-1]
    print(dp[-1])




