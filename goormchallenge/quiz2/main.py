import sys
cnt = 0
n, name = sys.stdin.readline().split()
n = int(n)
for _ in range(n):
    temp = sys.stdin.readline()
    if name in temp:
        cnt += 1
print(cnt)
