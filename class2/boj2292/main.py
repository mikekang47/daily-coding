# 1 7 19 37
n = int(input())
i = 1
cnt = 1
six = 6
while 1:
    if n <= i:
        break
    i += six * cnt
    cnt += 1
print(cnt)