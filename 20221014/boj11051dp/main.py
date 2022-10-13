n,k = map(int, input().split())
dp = [[0 for _ in range(n+2)]for _ in range(n+2)]

for i in range(1, n+2):
    for j in range(1, n+2):
        if j == 0:
            dp[i][j] = 1
        elif i == j:
            dp[i][j] = 1
        elif j == 1:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
print(dp[n+1][k+1] % 10007)
