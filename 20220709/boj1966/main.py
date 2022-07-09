import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split()) # 문서의 갯수, 궁금한 것의 위치
    li = deque(map(int, sys.stdin.readline().split())) # 중요도
    li.insert(m+1, 0)
    cnt = 0

    while 1:
        li.rotate(-li.index(max(li)))
        li.popleft()
        cnt += 1

        if li[0] == 0:
            break
    print(cnt)




