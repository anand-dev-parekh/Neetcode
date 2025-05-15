class Solution:
    def addIndex(self, val, inc, nums):
        prev = nums[val]
        val += inc
        while val < len(nums) and val >= 0 and nums[val] == prev:
            val += inc
        return val

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for i, num in enumerate(nums):

            if i > 0 and num == nums[i-1]: continue

            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[l] + nums[r] + num < 0:
                    l = self.addIndex(l, 1, nums)
                elif nums[l] + nums[r] + num > 0:
                    r = self.addIndex(r, -1, nums)
                else:

                    ans.append(sorted([nums[l], nums[r], num]))
                    l = self.addIndex(l, 1, nums)
                    r = self.addIndex(r, -1, nums)
        return ans
