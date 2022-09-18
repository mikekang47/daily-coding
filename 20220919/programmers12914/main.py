def solution(n):
    gongcha = 1
    li = [0, 1, 2]
    if n <= 2:
        return li[n]
    for i in range(2, n):
        li.append(li[i] + li[i-1])
        gongcha += 1

    return li[n] % 1234567
