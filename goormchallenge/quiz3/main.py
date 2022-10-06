import sys
from itertools import permutations

li = list(map(int, sys.stdin.readline().split()))
per = list(permutations(li, 4))
m = 0
for i in range(len(per)):
    temp = abs(per[i][0] - per[i][2]) +  abs(per[i][1] - per[i][3])
    if temp > m:
        m = temp
print(m)



