n, k = map(int, input().split())
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
knapsack = [[0,0]]
for _ in range(n):
    knapsack.append(list(map(int, input().split())))


for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = knapsack[i][0]
        value = knapsack[i][1]

        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
print(dp[n][k])
