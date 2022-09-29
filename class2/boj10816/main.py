import sys
from collections import defaultdict

n = int(sys.stdin.readline())
li = [0] * 20000001
temp = list(map(int, sys.stdin.readline().split()))
for i in temp:
    li[i + 10000000] += 1
m = int(sys.stdin.readline())
temp = list(map(int, sys.stdin.readline().split()))
s = ""
for i in temp:
    s += str(li[i + 10000000]) + " "
print(s.strip())