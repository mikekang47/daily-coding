n = int(input())
m = int(input())
result = abs(100-n)

if m:
    li = list(input().split())
else:
    li = list()

for i in range(1000001):
    for j in str(i):
        if j in li:
            break
    else:
        result = min(result, len(str(i)) + abs(i - n))
print(result)
