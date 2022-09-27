while 1:
    s = input()
    if s == "0":
        exit(0)
    temp = "".join(reversed(list(s)))
    if s == temp:
        print("yes")
    else:
        print("no")

