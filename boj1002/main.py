t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 두 원이 일치할 때
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    # 두 원이 외접할 때
    elif (x1 - x2) ** 2 + (y1 - y2) ** 2 == (r1 + r2) ** 2:
        print(1)
    # 두 원이 내접할 때
    elif (x1 - x2) ** 2 + (y1 - y2) ** 2 == (r1 - r2) ** 2:
        print(1)
    # 두 원이 서로 떨어져 있고 만나지 않을 때
    elif (x1 - x2) ** 2 + (y1 - y2) ** 2 > (r1 + r2) ** 2:
        print(0)
    # 한 원이 다른 원의 내부에 있고 두 원이 만나지 않을 때
    elif (x1 - x2) ** 2 + (y1 - y2) ** 2 < (r1 - r2) ** 2:
        print(0)
    else:
        print(2)
