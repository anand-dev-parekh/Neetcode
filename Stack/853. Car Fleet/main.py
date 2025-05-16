class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        slowest_time = 0
        fleets = 0
        for pos, spd in sorted(zip(position, speed), reverse=True):
            time_taken = (target - pos) / spd

            if time_taken > slowest_time:
                slowest_time = time_taken
                fleets += 1

        return fleets
