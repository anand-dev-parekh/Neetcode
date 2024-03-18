from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = deque()
        for c in s:
            if c in close_to_open:
                if len(stack) == 0 or close_to_open[c] != stack.pop():
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
