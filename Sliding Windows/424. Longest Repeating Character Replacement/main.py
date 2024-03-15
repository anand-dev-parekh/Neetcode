class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        char_map = [0] * 26
        left_ptr = 0
        ans = 0

        for i in range(len(s)):
            char_map[ord(s[i]) - 65] += 1

            max_val = max(char_map)

            while(i - left_ptr - max_val + 1 > k):
                char_map[ord(s[left_ptr]) - 65] -= 1
                left_ptr += 1

            ans = max(ans, i-left_ptr+1)

        return ans
