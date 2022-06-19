import itertools
import sys

dp = [[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)]

INF = sys.maxsize
n = int(input())
lst = list(map(int, input().split()))

def solve(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return 0

    if dp[a][b][c] != -1:
        return dp[a][b][c]

    dp[a][b][c] = INF
    for t in itertools.permutations([9, 3, 1]):
        dp[a][b][c] = min(dp[a][b][c], solve(max(0, a - t[0]), max(0, b - t[1]), max(0, c - t[2])))
    dp[a][b][c] += 1

    return dp[a][b][c]

print(solve(*lst + [0] * (3-n)))