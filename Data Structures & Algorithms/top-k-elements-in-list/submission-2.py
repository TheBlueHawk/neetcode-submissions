class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        bins = [[] for i in range(len(nums)+1)]
        for num, count in counts.items():
            bins[count].append(num)
        res = []
        for i in range(len(bins)-1,0,-1):
            for num in bins[i]:
                res.append(num)
                if len(res) == k:
                    return res
        