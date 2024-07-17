class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
    
        # Ignore last house
        prev, two_prev = max(nums[1],nums[0]), nums[0]
        for i in range(2, len(nums)-1):
            temp = max(prev, two_prev + nums[i])
            two_prev = prev
            prev = temp
        ignore_last_max = prev

        # Ignore first house
        nums[2] = max(nums[2], nums[1])
        for i in range(3, len(nums)):
            nums[i] = max(nums[i-1], nums[i-2] + nums[i])
        
        ignore_first_max = nums[-1]
        return max(ignore_first_max, ignore_last_max)
            
        