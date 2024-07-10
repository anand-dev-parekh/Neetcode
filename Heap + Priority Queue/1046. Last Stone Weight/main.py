import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-s for s in stones]

        heapq.heapify(stones)
        while len(stones) > 1:
            stone_one = heapq.heappop(stones)
            stone_two = heapq.heappop(stones)

            new_stone = stone_one - stone_two
            if new_stone < 0:
                heapq.heappush(stones, new_stone)
        
        return stones[0]*-1 if len(stones) > 0 else 0