import sys

t = int(sys.stdin.readline())
for i in range(t):
    sum = 0
    n = int(sys.stdin.readline())
    a = 5
    while a <= n:
        sum += n // a
        a *= 5
    print(sum)