class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def combination(subset, subset_sum, i):
            if subset_sum == target:
                res.append(subset.copy())
                return

            if subset_sum > target:
                return

            for j in range(i, len(candidates)):
                subset.append(candidates[j])
                combination(subset, subset_sum+candidates[j], j)
                subset.pop()

        combination([], 0, 0)
        return res
