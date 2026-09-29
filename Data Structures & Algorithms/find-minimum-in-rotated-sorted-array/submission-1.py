class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        lowest = nums[0]
        if nums[l] < nums[r]:
            return nums[l]
        while l < r-1:
            mid = l + (r - l) // 2
            print(nums[l], nums[mid], nums[r])
            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid
        return nums[r]
