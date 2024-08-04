class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        res = nums[0]

        cur_max = nums[0]
        cur_min = nums[0]

        for i, num in enumerate(nums):
            if i == 0: continue

            if num >= 0:
                cur_max = max(num, cur_max*num)
                cur_min = min(num, cur_min*num)
            else:
                tmp = cur_max
                cur_max = max(num, cur_min*num)
                cur_min = min(num, tmp*num)
            
            res = max(cur_max, res)
        
        return res