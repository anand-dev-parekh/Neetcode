class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1

        res, x = 0, abs(x)
        while x != 0:
            res = res * 10 + x % 10
            x = x // 10

        if res > 2**31 - 1:
            return 0

        return res * sign
