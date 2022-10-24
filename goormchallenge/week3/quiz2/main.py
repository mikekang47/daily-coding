from collections import defaultdict
import sys
dic = {
    1 : "1.,?!",
    2 : "2ABC",
    3 : "3DEF",
    4 : "4GHI",
    5 : "5JKL",
    6 : "6MNO",
    7 : "7PQRS",
    8 : "8TUV",
    9 : "9WXYZ",
}

n = int(sys.stdin.readline())
s = sys.stdin.readline()

cnt = 0
result = ""
for i in range(n):
    if i == n:
        break
    else:
        if s[i+1] == s[i]:
            cnt += 1
            continue
        else:
            cnt %= len(dic[int(s[i])])
            result += dic[int(s[i])][cnt]
            cnt = 0
print(result)
