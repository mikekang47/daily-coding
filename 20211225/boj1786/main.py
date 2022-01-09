import sys
t = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()
cnt = 0
arr = []
while t.find(p) != -1:
    cnt += 1
    arr.append(t.index(p)+1)
    t = t.replace(p, ' ', 1)
print(cnt)
for i in arr:
    print(i, end='')