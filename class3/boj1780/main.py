import sys

n = int(input())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = {-1: 0, 0: 0, 1: 0}


def func(k, i, j):
    p = a[i][j]
    for row in a[i:i + k]:
        if row[j:j + k] != [p] * k:
            break
    else:
        result[p] += 1
        return
    for d in range(3):
        for e in range(3):
            func(k // 3, i + d * k // 3, j + e * k // 3)
    return


func(n, 0, 0)
print(*result.values(), sep='\n')
