cnt = 1
while 1:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    day = v // p
    rest = v % p
    if rest < l:
        print("Case", str(cnt)+":", day*l + rest)
    else:
        print("Case", str(cnt) + ":", day*l + l)
    cnt += 1