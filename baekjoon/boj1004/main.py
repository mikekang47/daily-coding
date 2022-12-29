import math

t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    li = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        li.append((x, y, r))
    result = 0
    # 거리 계산
    for i in range(n):
        d1 = (x1 - li[i][0]) ** 2 + (y1 - li[i][1]) ** 2
        d2 = (x2 - li[i][0]) ** 2 + (y2 - li[i][1]) ** 2
        if d1 < li[i][2] ** 2:
            if d2 > li[i][2] ** 2:
                result += 1

        if d2 < li[i][2] ** 2:
            if d1 > li[i][2] ** 2:
                result += 1
    print(result)


