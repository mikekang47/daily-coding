def palindrome(s, left:int, right:int):
    while left >= 0 and right < len(s):
        if s[left] != s[right]:break
        left -= 1
        right += 1
    return right - left - 1


def solution(s):
    answer = 0
    for i in range(len(s)):
        odd = palindrome(s, i, i)
        even = palindrome(s, i-1, i)
        maxV = max(odd, even)
        answer = max(answer, maxV)
    return answer
s = "eabacde"
print(solution(s))