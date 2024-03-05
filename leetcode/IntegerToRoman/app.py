import unittest


class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        romans = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        # 주어진 숫자를  roman의 key로 나눈 몫이 0보다 크다면 계속 루프 회전.
        # 클 때, 그 value를 result 에 하나씩 append
        for number, roman in romans.items():
            if num // number > 0:
                divisor = num // number
                num = num % number
                result += roman * divisor

        return result

class Test(unittest.TestCase):
    def test_intToRoman(self):
        s = Solution()
        result = s.intToRoman(3)
        assert result == "III"

    def test_2(self):
        s = Solution()
        result = s.intToRoman(58)
        assert result == "LVIII"

    def test_3(self):
        s = Solution()
        result = s.intToRoman(1994)
        assert result == "MCMXCIV"