t = int(input())
for _ in range(t):
    dp = [[0 for _ in range(33)] for _ in range(33)]

    n, m = map(int, input().split())
    for i in range(1, m + 1):
        dp[1][i] = i

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

    print(dp[n][m])
