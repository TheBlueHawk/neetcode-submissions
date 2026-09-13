class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        nums = sorted(list(set(nums)))
        print(nums)
        best = 1
        current = 1
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] == nums[j-1] + 1:
                current +=1
                j += 1
                best = max(best, current)
            else:
                j +=1
                i = j
                current = 1
        return best
