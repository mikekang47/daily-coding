n = int(input())
l = list(input() for _ in range(n))

def f(x, y, s):
    t = l[y][x]
    for r in l[y:y+s]:
        for c in r[x:x+s]:
            if c != t:
                s //= 2
                return '(' + f(x, y, s) + f(x + s, y, s) + f(x, y + s, s) + f(x + s, y + s, s) + ')'
            t = c
    return str(t)
print(f(0,0,n))
