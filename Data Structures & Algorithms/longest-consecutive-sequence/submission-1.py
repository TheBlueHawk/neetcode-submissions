class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        nums = set(nums)
        best = 1
        start_list = [num for num in nums if num-1 not in nums]
        for start in start_list:
            current = 1
            num = start
            while num+1 in nums:
                num += 1
                current +=1
            best = max(best, current) 
        return best