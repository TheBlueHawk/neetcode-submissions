class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        req_h = None
        lowest = max(piles)
        while l <= r:
            mid = l + (r - l) // 2
            req_h = sum([math.ceil(p / mid) for p in piles])
            print(mid, req_h)
            if req_h > h:
                l = mid + 1
            else:
                r = mid - 1
                lowest = min(lowest, mid)
        return lowest 
