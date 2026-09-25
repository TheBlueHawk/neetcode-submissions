class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        mid = l+(r-l)//2 
        if nums[l] == target:
            return l
        elif nums[mid] == target:
            return mid
        elif nums[r] == target:
            return r

        while mid != l:
            if nums[mid] > target:
                r = mid
            else:
                l = mid  
            mid = l+(r-l)//2 
            if nums[mid] == target:
                return mid  
        return -1
  