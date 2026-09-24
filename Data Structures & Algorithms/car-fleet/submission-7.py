class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sorting cars by position
        ps = sorted(zip(position, speed), reverse=True)
        fleets = 0
        slowest = 0.0
        for p, s in ps:
            t = (target - p) /s
            if t > slowest:
                slowest = t
                fleets += 1
        return fleets
