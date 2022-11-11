n = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(1004)]

for i in range(n):
    dp[i] = 1
    for j in range(0, i):
        if A[j] < A[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))
