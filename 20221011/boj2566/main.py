import sys
li = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
m = 0
y,x = 0,0
for i in range(9):
    for j in range(9):
        if li[i][j] >= m:
            m = li[i][j]
            y = i
            x = j
print(m)
print(y+1,x+1)