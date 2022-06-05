import sys

sys.setrecursionlimit(1004)
def solution(n):
    mem = [-1 for i in range(1004)]

    def dp(n):
        if mem[n] != -1: return mem[n]
        if n == 0: return 1
        if n == 1: return 1
        mem[n] = (dp(n-1) + 2 * dp(n-2)) % 10007
        return mem[n]
    return dp(n)

n = int(input())
print(solution(n))