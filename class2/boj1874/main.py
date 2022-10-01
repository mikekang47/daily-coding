n = int(input())
li = [int(input()) for _ in range(n)]
arr = []
temp = []
for i in range(1, n + 1):
    arr.append(i)
    temp.append("+")
    while len(arr) != 0:
        if li[0] == arr[-1]:
            li.pop(0)
            arr.pop(-1)
            temp.append("-")
        else:
            break

if len(arr) != 0:
    print("NO")
else:
    [print(i) for i in temp]
