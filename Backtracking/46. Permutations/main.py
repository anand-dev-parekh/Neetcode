class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        res = []
        def permutation(subset, i):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for j, num in enumerate(nums):
                if num in subset:
                    continue

                subset.append(num)
                permutation(subset, j)
                subset.pop()

        permutation([], 0)
        return res
