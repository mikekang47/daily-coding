class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s):
            return 0
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        res = 0

        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        res = res * sign
        if res > 2**31 - 1:
            return 2**31 - 1
        if res < -2**31:
            return -2**31
        return res


s = Solution()
n = s.myAtoi("-91283472332")
print(n)
