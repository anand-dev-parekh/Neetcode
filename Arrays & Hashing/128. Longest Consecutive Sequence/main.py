from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        map = defaultdict(lambda : 0)
        ans = 0
        for num in nums:
            if map[num] != 0: continue
            map[num] = 1 + map[num+1] + map[num-1]

            right_interval = map[num+1] + num
            left_interval = num - map[num-1]
            map[right_interval] = map[num]
            map[left_interval] = map[num]

            ans = max(ans, map[num])

        return ans
