def slicing(y, x, length):
    s = ""
    start = li[y][x]
    for i in range(y, y + length):
        for j in range(x, x + length):
            if start != li[i][j]:
                return '(' + slicing(y, x, length // 2) + slicing(y, x + length // 2, length // 2) + slicing(
                    y + length // 2, x, length // 2) + slicing(y + length // 2, x + length // 2, length // 2) + ')'
            start = li[i][j]
    return str(start)


n = int(input())
li = [list(map(int, list(input()))) for _ in range(n)]
print(slicing(0, 0, n))
