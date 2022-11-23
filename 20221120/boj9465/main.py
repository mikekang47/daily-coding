import sys

input = sys.stdin.readline
t = int(input())

while t > 0:
    n = int(input())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    sumList = [a1, a2]
    dp = [[0 for _ in range(100000)] for _ in range(2)]

    dp[0][0] = sumList[0][0]
    dp[1][0] = sumList[1][0]
    dp[0][1] = dp[1][0] + sumList[0][1]
    dp[1][1] = dp[0][0] + sumList[1][1]
    dp[1][1] = dp[0][0] + sumList[1][1]
    for j in range(2, n):
        dp[0][j] = max(dp[1][j - 1], dp[1][j - 2]) + sumList[0][j]
        dp[1][j] = max(dp[0][j - 1], dp[0][j - 2]) + sumList[1][j]
    print(max(dp[0][n - 1], dp[1][n - 1]))
    t -= 1
