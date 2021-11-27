s = int(input())
i = 1
cnt = 0
while s - i >= 0:
    s -= i
    i += 1
    cnt += 1
print(cnt)
