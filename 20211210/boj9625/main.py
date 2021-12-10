import sys

k = int(sys.stdin.readline().strip())
arr = [0, 1]
for i in range(1, k):
    arr.append(arr[i-1] + arr[i])
print(arr[-2], arr[-1])