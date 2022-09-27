import math

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:
        p = h
    else:
        p = n % h
    print(p * 100 + math.ceil(n / h))
