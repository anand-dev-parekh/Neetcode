import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        dis_arr = []

        for i, point in enumerate(points):
            dist = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(dis_arr, (-dist, i))
            if len(dis_arr) > k:
                heapq.heappop(dis_arr)
        
        
        return [points[dis[1]] for dis in dis_arr]