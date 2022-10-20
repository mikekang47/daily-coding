n = int(input())
s = int(input())
m = input()

cnt = 0
result = 0
i = 0
while i < s:
    if m[i:i + 3] == 'IOI':
        cnt += 1
        if cnt == n:
            cnt -= 1
            result += 1
        i += 1
    else:
        cnt = 0
    i += 1
print(result)
