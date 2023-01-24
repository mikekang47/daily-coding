class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ""
        for i in range(numRows):
            for j in range(i, len(s), 2 * numRows - 2):
                result += s[j]
                if i != 0 and i != numRows - 1 and j + 2 * numRows - 2 - 2 * i < len(s):
                    result += s[j + 2 * numRows - 2 - 2 * i]
        return result

s = Solution()
ans = s.convert("PAYPALISHIRING", 3)
print(ans)