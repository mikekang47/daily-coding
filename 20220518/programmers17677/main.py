import collections
import math


def detach(s: str):
    s1 = []
    for i in range(len(s)-1):
        if s[i].isalpha() and s[i+1].isalpha():
            s1.append(s[i:i + 2])

    return s1


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    if (str1 == "" and str2 == "") or str1 == str2:
        return 65536

    s1 = detach(str1)
    s2 = detach(str2)

    st1 = collections.Counter(s1)
    st2 = collections.Counter(s2)

    intersection = list((st1&st2).elements())
    union = list((st1|st2).elements())
    print(union)
    print(intersection)

    jcard = len(intersection) / len(union)

    return math.floor(jcard * 65536)


# str1 = "FRANCE"
# str2 = "french"

# str1 = "E=M*C^2"
# str2 = "e=m*c^2"

# str1 = "handshake"
# str2 = "shake hands"

str1 = "aa1+aa2"
str2 = "AAAA12"

print(solution(str1, str2))