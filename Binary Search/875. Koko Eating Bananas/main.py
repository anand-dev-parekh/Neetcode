class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            m = (l+r) // 2

            if self.is_feasible(piles, h, m):
                r = m
            else:
                l = m+1

        return l

    def is_feasible(self, piles: list[int], h: int, k: int) -> bool:

        for p in piles:

            time = (p // k)
            time += 1 if time != p / k else 0
            h -= time
        
        return h >= 0



        