class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}

        for i, num in enumerate(nums):
            if (target - num in dict):
                return [dict[target - num], i]
            dict[num] = i
        return [-1, -1]
