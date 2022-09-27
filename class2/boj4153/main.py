import sys

while 1:
    li = list(map(int, input().split()))
    li.sort()
    a = li[0]
    b = li[1]
    c = li[2]
    if a == 0 and b == 0 and c == 0:
        sys.exit(0)
    if pow(a, 2) + pow(b, 2) == pow(c, 2):
        print("right")
    else:
        print("wrong")
