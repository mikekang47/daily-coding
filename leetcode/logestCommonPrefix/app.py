import unittest
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        strs.sort(key=lambda x: len(x))
        if strs[0] == "":
            return result
        for i in strs[0]:
            flag = True
            word = result + i
            for j in strs:
                if not j.startswith(word):
                    flag = False
                    break
            if not flag:
                break
            else:
                result += i

        return result


class Test(unittest.TestCase):
    def test_longestCommonPrefix1(self):
        strs = ["flower", "flow", "flight"]
        s = Solution()
        result = s.longestCommonPrefix(strs)
        print(result)
        assert result == "fl"

    def test_longestCommonPrefix2(self):
        strs = ["dog", "racecar", "car"]
        s = Solution()
        result = s.longestCommonPrefix(strs)
        print(result)
        assert result == ""
