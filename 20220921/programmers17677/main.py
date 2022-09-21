import re
import unittest
from collections import Counter

def detach(s: str):
    s1 = []
    for i in range(len(s) - 1):
        if s[i].isalpha() and s[i + 1].isalpha():
            s1.append(s[i:i + 2])

    return s1

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    a2 = detach(str2)
    a1 = detach(str1)

    c1 = Counter(a1)
    c2 = Counter(a2)
    if len(c1.items()) == 0 and len(c2.items()) == 0:
        return 65536

    jcard1 = sum((c1 | c2).values())
    jcard2 = sum((c1 & c2).values())

    # print(int((jcard2 / jcard1) * 65536))
    return int((jcard2 / jcard1) * 65536)





class Test(unittest.TestCase):
    def testSolution(self):
        str1 = "FRANCE"
        str2 = "french"
        assert solution(str1, str2) == 16384