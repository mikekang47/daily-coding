import re
from collections import Counter
import unittest

def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))




class Test(unittest.TestCase):
    def test_solution(self):
        s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
        assert solution(s) == [2, 1, 3, 4]
