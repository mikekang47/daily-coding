n, m = map(int, input().split())
num = int(input())
l = 1
cnt = 0
for i in range(num):
    temp = int(input())
    r = l + m - 1
    if l <= temp <= r:
        continue
    else:
        if temp < l:
            cnt += l - temp
            l = temp
        else:
            l += temp-r
            cnt += temp - r

print(cnt)




