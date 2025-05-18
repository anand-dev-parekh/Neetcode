class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def generateHelper(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return

            if left < n:
                generateHelper(left + 1, right, s + '(')

            if right < left:
                generateHelper(left, right + 1, s + ')')

        generateHelper(0, 0, '')
        return res
