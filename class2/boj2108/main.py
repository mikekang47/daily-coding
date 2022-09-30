import sys
import statistics

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()
print(round(statistics.mean(arr)))

print(int(statistics.median(arr)))

if len(statistics.multimode(arr)) > 1:
    print(statistics.multimode(arr)[1])
else:
    print(statistics.multimode(arr)[0])
print(arr[-1] - arr[0])
