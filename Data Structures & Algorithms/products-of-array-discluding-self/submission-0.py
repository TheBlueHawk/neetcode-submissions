class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_position = -1
        for i, num in enumerate(nums):
            if num == 0:
                if zero_position != -1: #2nd zero      
                    return [0]*len(nums)
                zero_position = i #1st zero position
                continue
            prod *= num
        if zero_position != -1:
            output = [0]*len(nums)
            output[zero_position] = prod
            return output
        return [int(prod/num) for num in nums]
