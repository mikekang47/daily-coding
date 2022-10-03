n = int(input())
stair = [int(input()) for _ in range(n)]
stair.append(0)
stair.append(0)
dp = [0] * 311
dp[0] = stair[0]
dp[1] = max(stair[1], stair[0] + stair[1])
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
for i in range(3, n):
    dp[i] = max(dp[i-2] + stair[i], stair[i] + stair[i-1] + dp[i-3])
print(dp[n-1])