class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        left_ptr = 0
        window = {}
        for right_ptr, c in enumerate(s):

            if c in window and window[c] >= left_ptr:
                left_ptr = window[c] + 1

            window[c] = right_ptr
            ans = max(1 + right_ptr - left_ptr, ans)

        return ans
