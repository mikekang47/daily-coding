t = int(input())
for _ in range(t):
    arr = list(input())
    temp = []
    for i in arr:
        if len(temp) == 0:
            temp.append(i)
            continue
        if i == ')' and temp[-1] == '(':
            temp.pop(-1)
        else:
            temp.append(i)
    if len(temp) == 0:
        print("YES")
    else:
        print("NO")
