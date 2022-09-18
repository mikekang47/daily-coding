def solution(s):
    answer = []
    zeroes = 0
    cnt = 0
    while s != "1":
        zeroes += s.count("0")
        s = s.replace("0","")
        s = str(bin(len(s)))[2:]
        cnt += 1
    answer.append(cnt)
    answer.append(zeroes)
    return answer

print(solution("01110"))


