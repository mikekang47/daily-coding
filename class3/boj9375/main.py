from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    dic = defaultdict(int)
    for _ in range(n):
        a, b = input().split()
        dic[b] += 1
    result = 1
    for i in dic.values():
        result *= (i + 1)
    print(result - 1)
'''
    한번 입었던 옷들의 조합을 절대 다시 입지 않는다.
    힌트: x + y + z + xy + yz + zx + xyz
       = x + z + y + xy + zy + zx + zxy
       = (x + z) + y + y(x + z) + zx(1 + y)
       = (x + z)(1 + y) + y + zx(1 + y)
       = (x + z)(1 + y) + zx(1 + y) + (1 + y) - 1
       = (x + z + zx + 1)(1 + y) - 1
       = (z + zx + 1 + x)(1 + y) - 1
       = (z(1 + x) + (1 + x))(1 + y) - 1
       = (1 + x)(1 + z)(1 + y) - 1
'''
# 몰랐다. 이런 식이 있는지
