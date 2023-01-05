t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    result = 0
    for i in arr:
        if i % 2 != 0:
            result += i
    print(result)