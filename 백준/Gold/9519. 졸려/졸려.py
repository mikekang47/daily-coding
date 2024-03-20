import sys


def solution(n, s):
    if len(list(set(s))) == 1:
        return s

    cnt = 0
    temp = s
    while True:
        temp = loop(temp)
        cnt += 1
        if temp == s:
            break
    answer = s
    for i in range(cnt - n % cnt):
        answer = loop(answer)
    return answer


def loop(s):
    idx = len(s) // 2 - 1
    j = 1
    half = half = len(s) // 2 + (len(s) & 1)
    str1 = list(s[:half])
    str2 = list(s[half:])
    while idx >= 0:
        str1.insert(j, str2[idx])
        idx -= 1
        j += 2
    str2 = str1[half:]
    str1 = str1[:half]
    return ''.join(str1 + str2)




n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
print(solution(n, s))
