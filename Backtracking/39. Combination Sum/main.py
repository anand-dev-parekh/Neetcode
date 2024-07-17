class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        output = []
        subset = []

        def subsets(i):
            if i >= len(nums):
                output.append(subset.copy())
                return

            subset.append(nums[i]) 
            subsets(i+1)
            subset.pop()
            subsets(i+1)

        subsets(0) 
        return output