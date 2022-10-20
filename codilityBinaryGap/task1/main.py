def solution(N: int):
    binN = bin(N)[2:]
    zero = "0"
    l = 0
    for i in range(1, len(binN)):
        if zero in binN:
            if binN.find(zero) + len(zero) < len(binN):
                if binN[binN.find(zero) + len(zero)] == "1":
                    l = len(zero)
        zero += "0"
    print(l)


solution(1041)
