class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, target in enumerate(nums):
            if target > 0:
                break
            
            if i > 0 and target == nums[i-1]:
                continue # skip repetitions

            l, r = i+1, len(nums) - 1
            while l < r:
                two_sum = nums[l] + nums[r]
                if two_sum > -target:
                    r -=1
                elif two_sum < -target:
                    l += 1
                else:
                    res.append([target, nums[l], nums[r]])
                    r -=1
                    l +=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1 
        return res