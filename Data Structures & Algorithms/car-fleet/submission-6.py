class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sorting cars by position
        ps = sorted(zip(position, speed), reverse=True)
        fleets = 1
        turns = None
        for p, s in ps:
            if not turns:
                turns = (target-p)/s
            d = p + turns * s
            if d < target:
                turns = (target-p)/s
                fleets += 1
        return fleets
