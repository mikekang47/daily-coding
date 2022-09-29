from collections import deque
n, k = map(int, input().split())
d = deque([i for i in range(1, n+1)])
cnt = 1
s = "<"
while len(d) != 0:
    if cnt == k:
        s += str(d.popleft()) + ", "
        cnt = 1
        continue
    d.append(d.popleft())
    cnt += 1
print(s[:-2]+">")
