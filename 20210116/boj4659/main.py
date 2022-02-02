while True:
    s = input()
    if s == "end":
        break
    good = True
    a = s
    for x in "aeiou":
        a = a.replace(x, "a")
    for x in "qwrtypsdfghjklzxvbnm":
        a = a.replace(x, "b")
    if sum(map(lambda x:s.count(x), "aeiou")) == 0:
        good = False
    if a.count("aaa") + a.count("bbb") > 0:
        good = False
    if sum(map(lambda x:s.count(x + x), "qwrtyuipasdfghjklzxcvbnm")) > 0:
        good = False
    print(("<%s> is acceptable." if good else "<%s> is not acceptable.") % s)

