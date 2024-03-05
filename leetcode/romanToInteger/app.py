import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        romans = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        for roman, number in romans.items():
            while s.startswith(roman):
                s = s.removeprefix(roman)
                result += number
        return result


class Test(unittest.TestCase):
    def test_romanToInt1(self):
        s = Solution()
        result = s.romanToInt("III")
        assert result == 3

    def test_romanToInt2(self):
        s = Solution()
        result = s.romanToInt("LVIII")
        assert result == 58

    def test_romanToInt3(self):
        s = Solution()
        result = s.romanToInt("MCMXCIV")
        assert result == 1994
