t = int(input())
for _ in range(t):
    l = []
    r = []
    s = input()
    for i in s:
        if i == '<':
            if l:
                r.append(l.pop())
        elif i == '>':
            if r:
                l.append(r.pop())
        elif i == '-':
            if l:
                l.pop()
        else:
            l.append(i)
    print(''.join(l + r[::-1]))