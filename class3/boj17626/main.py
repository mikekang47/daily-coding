import math
import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(500008)]
dp[1] = 1
for i in range(2, n + 1):
    temp = 99999999
    for j in range(1, int(math.sqrt(i)) + 1):
        temp = min(temp, dp[i - j*j])
    dp[i] = temp + 1
print(dp[n])
