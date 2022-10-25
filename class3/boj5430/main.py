import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    command = input()
    n = int(input())
    s = input()[1:-1]
    li = [] if len(s) == 0 else s.split(',')
    rFlag = False
    for c in command:
        if c == 'R':
            rFlag = not rFlag
        else:
            if len(li) > 0 and rFlag:
                li.pop()
            elif len(li)> 0 and not rFlag:
                li.pop(0)
            else:
                print("error")
                break
    else:
        if rFlag:
            li.reverse()
        print("[" + ','.join(li) + "]")



