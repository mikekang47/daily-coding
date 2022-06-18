t, w = map(int, input().split())

T = [[0,0]]

for i in range(t):
    b = [0,0]
    b[int(input())-1] = 1
    T.append(b)

dp = [[0] * (w+1)] * (t+1)
for i in range(1, t+1):
    dp[i][0] = dp[i-1][0] + T[i][0]
    for j in range(1, w+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + T[i][j % 2]

print(max(dp[t]))