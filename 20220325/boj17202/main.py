a = input()
b = input()
li = []
for i, j in zip(list(a),list(b)):
    li.append(int(i))
    li.append(int(j))

for i in range(0, 14):
    temp = []
    start = li[0]
    li.pop(0)
    while len(li) != 0:
        start += li[0]
        if start >= 10:
            start = start % 10
        temp.append(start)
        start = li[0]
        li.pop(0)
    li = temp

print(''.join(map(str, li)))


