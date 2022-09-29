n = int(input())
cnt = 0
dp = [9999999] * 5001
dp[3] = 1
dp[5] = 1
for i in range(6, n + 1):
    dp[i] = min(dp[i - 3] + 1, dp[i - 5] + 1)
if dp[n] >= 999999:
    print(-1)
else:
    print(dp[n])
