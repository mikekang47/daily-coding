import sys

n = int(sys.stdin.readline())
li = [0 for i in range(10001)]
for i in range(n):
    temp = int(sys.stdin.readline())
    li[temp] += 1
for i in range(10001):
    for _ in range(li[i]):
        print(i)
