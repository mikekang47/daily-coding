t = int(input())

for i in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    m = arr[-1]
    result = 0
    for j in range(n - 2, -1, -1):
        if arr[j] >= m:
            m = arr[j]
        else:
            result += m - arr[j]
    print(f'#{i}', result)
