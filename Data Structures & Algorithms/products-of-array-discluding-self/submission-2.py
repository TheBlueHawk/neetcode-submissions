class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixes = [1]*n
        suffixes = [1]*n
        # prefix pass
        for i in range(1,n):
            prefixes[i] = prefixes[i-1]*nums[i-1]
        
        for i in range(n-2,-1,-1):
            suffixes[i] = suffixes[i+1]*nums[i+1]
        return [s*p for s,p in zip(suffixes,prefixes)]
