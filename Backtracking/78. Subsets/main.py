class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        def subset(arr, i):
            if i == len(nums):
                res.append(arr.copy())
                return

            arr.append(nums[i])
            subset(arr, i+1)
            arr.pop()
            subset(arr, i+1)

        subset([], 0)
        return res
