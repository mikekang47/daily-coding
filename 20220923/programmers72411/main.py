import unittest
from collections import defaultdict, Counter
from itertools import  combinations


def solution(orders, course):
    answer = []
    for c in course:
        comb = []
        for order in orders:
            comb += combinations(sorted(order), c)

        most_ordered = Counter(comb).most_common()
        answer += [j for j, v in most_ordered if v > 1 and v == most_ordered[0][1]]

    return [''.join(i) for i in sorted(answer)]


class Test(unittest.TestCase):
    def test_solution(self):
        orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
        course = [2, 3, 4]
        assert solution(orders, course) == ["AC", "ACDE", "BCFG", "CDE"]
