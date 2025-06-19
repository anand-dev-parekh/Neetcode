class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:

        max_diff = -100000
        ret_idx = -1
        cur_diff = 0
        for i in range(len(gas)-1, -1, -1):
            cur_diff = cur_diff + gas[i] - cost[i]

            if cur_diff >= max_diff:
                ret_idx = i
                max_diff = cur_diff

        return ret_idx if cur_diff >= 0 else -1
