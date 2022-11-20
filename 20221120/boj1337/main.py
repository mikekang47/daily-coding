n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
result = 1000000001
for i in range(len(arr)):
    limit = arr[i] + 5
    start = arr[i] + 1
    cnt = 0
    j = i + 1
    while start < limit:
        if len(arr) > j and arr[j] == start:
            j += 1
        else:
            cnt += 1

        start += 1
    result = min(cnt, result)
print(result)
