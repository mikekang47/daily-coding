def solution(s):
    answer = 0
    if s == ''.join(reversed(s)):
        return len(s)
    mx = 1
    for i in range(1, len(s)):
        for j in range(len(s)):
            if list(s[j:j+i]) == list(reversed(s[j:j+i])) and len(s[j:j+i]) > mx:
                mx = len(s[j:j+i])
    answer = mx
    return answer


s = "abacde"
print(solution(s))