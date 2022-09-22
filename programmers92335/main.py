import math
import unittest


def isPrime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def jinbup(n, k):
    arr = []
    while n:
        arr.append(n % k)
        n = n // k
    arr.reverse()

    return ''.join(list(map(str, arr)))


def solution(n, k):
    translated = jinbup(n, k)
    temp = translated.split("0")
    cnt = 0
    for i in temp:
        if i != "1" and i != ' ' and isPrime(int(i)):
            cnt += 1
    return cnt


class Test(unittest.TestCase):

    def test_solution(self):
        n = 437674
        k = 3
        assert solution(n, k) == 3
