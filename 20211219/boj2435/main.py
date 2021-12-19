import sys

n, k = map(int, sys.stdin.readline().strip().split())
num = list(map(int, sys.stdin.readline().split()))
re = []
for i in range(n-k+1):
    temp = 0
    for j in range(i,i+k):
        temp += num[j]
    re.append(temp)
print(max(re))
