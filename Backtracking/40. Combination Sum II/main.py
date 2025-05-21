class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        candidates.sort()
        def combination(subset, subset_sum, i):
            if subset_sum == target:
                res.append(subset.copy())
                return

            if subset_sum > target:
                return

            for j in range(i+1, len(candidates)):
                if j-1 != i and candidates[j] == candidates[j-1]:
                    continue
                subset.append(candidates[j])
                combination(subset, subset_sum+candidates[j], j)
                subset.pop()

        combination([], 0, -1)
        return res
