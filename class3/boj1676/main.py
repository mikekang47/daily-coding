import math
n = int(input())
s = str(math.factorial(n))
cnt = 0
for i in range(len(s)-1, 0, -1):
    if s[i] == "0":
        cnt += 1
    else:
        break
print(cnt)
