cnt = 0
wcnt = 0
bcnt = 0
def splitter(stCol, stRow, n):
    flag = 0
    global wcnt
    global bcnt

    stColor = graph[stCol][stRow]
    for i in range(stCol, stCol+n):
        for j in range(stRow, stRow+n):
            if stColor != graph[i][j]:
                flag = -1
                break

        if flag == -1:
            break

    if flag != -1:
        if stColor == 0:
            wcnt += 1
        elif stColor == 1:
            bcnt += 1

    elif flag == -1:
        splitter(stCol, stRow, n//2)
        splitter(stCol+n//2, stRow, n//2)
        splitter(stCol, stRow+n//2, n//2)
        splitter(stCol + n//2, stRow + n//2, n//2)


n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
splitter(0,0, n)
print(wcnt, bcnt)

