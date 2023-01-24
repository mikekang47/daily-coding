class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True
        x = abs(x)
        x = str(x)
        x = x[::-1]
        x = int(x)
        if flag:
            x = -x
        else:
            x = x
        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0
        else:
            return x
