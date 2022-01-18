n = int(input())
a = []
temp = ''
for i in range(n):
    l = list(input())
    while len(l) != 0:
        if l[0].isdigit():
            temp += l[0]
            l.pop(0)
        else:
            l.pop(0)
            if len(temp) :
                a.append(temp)
                temp = ''
    if len(temp) != 0:
        a.append(temp)
    temp = ''

a = list(map(int, a))
a.sort()
for i in a:
    print(i)
