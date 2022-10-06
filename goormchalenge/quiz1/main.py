import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
result = 1
for i in li:
    result *= i
print(result)