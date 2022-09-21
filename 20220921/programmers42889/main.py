import unittest
from collections import Counter, defaultdict


def solution(N, stages):
    failure_rate = {}
    total = len(stages)

    for i in range(1, N + 1):
        if total != 0:
            count = stages.count(i)
            failure_rate[i] = count / total
            total -= count
        else:
            failure_rate[i] = 0

    return sorted(failure_rate, key=lambda x: failure_rate[x], reverse=True)


class Test(unittest.TestCase):

    def test_solution1(self):
        N = 4
        stages = [4, 4, 4, 4, 4]
        assert solution(N, stages) == [4, 1, 2, 3]

    def test_solution(self):
        N = 5
        stages = [2, 1, 2, 6, 2, 4, 3, 3]
        assert solution(N, stages) == [3, 4, 2, 1, 5]

    def test_solution2(self):
        N = 5
        stages = [4, 4, 4, 4, 3]
        assert solution(N, stages) == [4, 3, 1, 2, 5]

    def test_solution3(self):
        N = 6
        stages = [1, 2, 3, 4, 1, 1, 1]
        assert solution(N, stages) == [4, 1, 3, 2, 5, 6]
