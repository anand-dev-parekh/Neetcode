from collections import deque

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operator_set = {"+", "-", "*", "/"}
        s = deque()
        for token in tokens:
            if token in operator_set:
                v1 = s.pop()
                v2 = s.pop()

                new_v = self.runOperation(v1, v2, token)
                s.append(new_v)
            else:
                s.append(int(token))

        return s.pop()

    def runOperation(self, v1: int, v2: int, token: chr) -> int:

        if token == "+":
            ans = v1 + v2
        elif token == "-":
            ans = v2 - v1
        elif token == "*":
            ans = v1 * v2
        else:
            ans = int(v2 / v1)

        return ans
