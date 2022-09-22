import unittest

dic = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}


def jinbup(n, k):
    arr = []
    if n == 0:
        return '0'
    while n:
        a = n % k
        if a < 10:
            arr.append(a)
        else:
            arr.append(dic[a])
        n = n // k
    arr.reverse()

    return ''.join(list(map(str, arr)))


def solution(n, t, m, p):
    answer = ""
    i = 0
    while len(answer) < t * m:
        answer += jinbup(i, n)
        i += 1
    return answer[p-1::m][:t]


class Test(unittest.TestCase):
    def test_solution(self):
        n = 2
        t = 4
        m = 2
        p = 1
        assert solution(n, t, m, p) == "0111"

    def test_solution2(self):
        n = 16
        t = 16
        m = 2
        p = 2
        assert solution(n, t, m, p) == "13579BDF01234567"
