from copy import deepcopy
import sys

n = int(sys.stdin.readline())
dic = {}
li = list(map(int, sys.stdin.readline().split()))
temp = deepcopy(li)
li = list(set(li))

for i in li:
    dic[i] = 0
li.sort()
for i in range(len(li)):
    if dic[li[i]] == 0:
        dic[li[i]] = i
    else:
        if dic[li[i]] > i:
            dic[li[i]] = i
t = []
for i in temp:
    t.append(dic[i])
print(*t)
