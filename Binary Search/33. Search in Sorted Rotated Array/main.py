class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l < r:

            m = (l+r) // 2 

            if nums[r] == target:
                return r

            if ((nums[m] > nums[r] and target > nums[m]) or 
                (nums[m] > nums[r] and target < nums[r]) or 
                (target > nums[m] and target < nums[r])):

                l = m+1
            else:
                r = m

        return l if nums[l] == target else -1