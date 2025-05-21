class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

        res = []
        nums.sort()
        def subset(arr, i):
            for j in range(i+1, len(nums)):
                if i != j-1 and nums[j] == nums[j-1]:
                    continue

                arr.append(nums[j])
                subset(arr, j)
                arr.pop()
            res.append(arr.copy())

        subset([], -1)
        return res
