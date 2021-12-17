while 1:
    try:
        a, b = input().split()
        wA = list(a)
        wB = list(b)
        while wA:
            if len(wB) == 0:
                break
            if wA[0] == wB[0]:
                wA.pop(0)
                wB.pop(0)
            else:
                wB.pop(0)
        if len(wA) == 0:
            print("Yes")
        else:
            print("No")
    except:
        break
