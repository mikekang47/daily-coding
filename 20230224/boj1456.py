import sys, math

a,b = map(int, sys.stdin.readline().split())
li = list(range(10000001))
li[1] = 0
for i in range(2, int(math.sqrt(10000001)) + 1):
    if li[i] == 0:
        continue
    for j in range(i*2, 10000001, i):
        li[j] = 0
        
result = 0
for i in range(2, 10000001):
    if li[i] != 0:
        temp = li[i]
        while li[i] <= b / temp:
            if li[i] >= a / temp:
                result += 1
            temp *= li[i]
print(result)