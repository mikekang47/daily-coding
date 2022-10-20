n = int(input())
s = int(input())
m = input()

cnt = 0
result = 0
for i in range(1, s - 1):
    if m[i - 1] == 'I' and m[i] == 'O' and m[i + 1] == 'I':
        cnt += 1
        if cnt == n:
            cnt -= 1
            result += 1
        i += 1
    else:
        cnt = 0
print(result)