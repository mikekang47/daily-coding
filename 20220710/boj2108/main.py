import statistics
import sys

n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]
li.sort()

print(round(statistics.mean(li)))
print(int(statistics.median(li)))
if len(statistics.multimode(li)) > 1:
    print(statistics.multimode(li)[1])
else:
    print(statistics.multimode(li)[0])
print(li[-1] - li[0])