import sys
import statistics
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    record = list(map(int, sys.stdin.readline().split()))
    mean = statistics.mean(record)
    cnt = len(list(filter(lambda x: x >= mean, record)))
    print(str(cnt)+"/"+str(len(record)))

