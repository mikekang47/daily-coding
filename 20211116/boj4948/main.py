import math
INF = 123456

arr = [True] * (2 * INF + 1)
arr[0] = False
arr[1] = False

for i in range(2, int(math.sqrt(len(arr)))):
    if arr[i]:
        for j in range(i+i, len(arr), i):
            arr[j] = 0

while 1:
    n = int(input())

    if n == 0:
        break
    else:
        print(sum(arr[n+1:(2*n)+1]))
