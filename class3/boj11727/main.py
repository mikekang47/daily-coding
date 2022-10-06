import sys
n = int(sys.stdin.readline())
dp = [1 for _ in range(1004)]
dp[2] = 3
dp[3] = 5
for i in range(4, n+1):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007
print(dp[n])
