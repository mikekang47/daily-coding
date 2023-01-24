class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_length = len(s)
        max_polindrome = ''

        def palindrome_from(l, r):
            while (l >= 0) and (r < s_length) and (s[l] == s[r]):
                l -= 1
                r += 1
            return s[(l + 1):r]

        for i in range(s_length):
            max_polindrome = max(
                max_polindrome,
                palindrome_from(i, i),
                palindrome_from(i, i + 1),
                key=len
            )
        return max_polindrome