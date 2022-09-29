import sys
from collections import deque
li = deque([i for i in range(1, int(sys.stdin.readline())+1)])
while len(li) != 1:
    li.popleft()
    li.append(li.popleft())
print(li.popleft())