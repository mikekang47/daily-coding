from collections import deque

n = int(input())
li = deque([i for i in range(1, n+1)])
result = []

while len(li):
    result.append(li.popleft())
    if not len(li):
        break
    li.append(li.popleft())

print(*result)

