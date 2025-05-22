class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []

        letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        def combo(subset, i):
            if i == len(digits):
                res.append(''.join(subset))
                return

            for c in letter_map[digits[i]]:
                subset.append(c)
                combo(subset, i+1)
                subset.pop()

        combo([], 0)
        return res
