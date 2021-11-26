import sys

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
blist = []
if len(arr) < 2:
    print(0)
    sys.exit()
else:
    value = arr[0]
    blist = arr[1:]
    blist.sort(reverse=True)
    cnt = 0
    while value <= blist[0]:
        value += 1
        blist[0] -= 1
        cnt += 1
        blist.sort(reverse=True)
    print(cnt)
